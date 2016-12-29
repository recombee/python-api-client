import os
import time
import hmac
import json
from hashlib import sha1
import requests

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote

from recombee_api_client.exceptions import ApiTimeoutException, ResponseException
from recombee_api_client.api_requests import Batch

class RecombeeClient:
    """
    Client for sending requests to Recombee recommender system
    """
    BATCH_MAX_SIZE = 10000

    def __init__(self, database_id, token, protocol = 'http', options = {}):
        """
        @param database_id: Name of your database_id at Recombee
        @param token: Secret token obtained from Recombee for signing requests
        @param protocol: Default protocol for sending requests. Possible values: 'http', 'https'.
        """
        self.database_id = database_id
        self.token = token
        self.protocol = protocol

        self.base_uri = os.environ.get('RAPI_URI')
        if self.base_uri is None:
            self.base_uri =  options.get('base_uri')
        if self.base_uri is None:
            self.base_uri = 'rapi.recombee.com'


    def send(self, request):
        """
        @param request: Request to be sent to Recombee recommender
        """
        
        if isinstance(request, Batch) and len(request.requests) > self.BATCH_MAX_SIZE:
            return self.__send_multipart_batch(request)

        timeout = request.timeout / 1000
        uri = self.__process_request_uri(request)
        uri = self.__sign_url(uri)
        protocol = 'https' if request.ensure_https else self.protocol
        uri = protocol + '://' + self.base_uri + uri
        try:
            if request.method == 'put':
                return self.__put(request, uri, timeout)
            elif request.method == 'get':
                return self.__get(request, uri, timeout)
            elif request.method == 'post':
                return self.__post(request, uri, timeout)
            elif request.method == 'delete':
                return self.__delete(request, uri, timeout)
        except requests.exceptions.Timeout:
            raise ApiTimeoutException(request)

    def __put(self, request, uri, timeout):
        response = requests.put(uri, timeout=timeout)
        self.__check_errors(response, request)
        return response.json()

    def __get(self, request, uri, timeout):
        response = requests.get(uri, timeout=timeout)
        self.__check_errors(response, request)
        return response.json()

    def __post(self, request, uri, timeout):
        response = requests.post(uri, data=json.dumps(request.get_body_parameters()), 
                                            headers={'Content-Type': 'application/json'},
                                            timeout=timeout)
        self.__check_errors(response, request)
        return response.json()

    def __delete(self, request, uri, timeout):
        response = requests.delete(uri, timeout=timeout)
        self.__check_errors(response, request)
        return response.json()


    def __check_errors(self, response, request):
        status_code = response.status_code
        if status_code == 200 or status_code == 201:
            return
        raise ResponseException(request, status_code, response.text)

    @staticmethod
    def __get_list_chunks(l, n):
        """Yield successive n-sized chunks from l."""

        try: #Python 2/3 compatibility
            xrange
        except NameError:
            xrange = range

        for i in xrange(0, len(l), n):
            yield l[i:i + n]

    def __send_multipart_batch(self, batch):
        requests_parts = [rqs for rqs in self.__get_list_chunks(batch.requests, self.BATCH_MAX_SIZE)]
        responses = [self.send(Batch(rqs)) for rqs in requests_parts]
        return sum(responses, [])

    def __process_request_uri(self, request):
        uri = request.path
        uri = uri[len('/{databaseId}/'):]
        uri += self.__query_parameters_to_url(request)
        return uri


    def __query_parameters_to_url(self, request):
            ps = ''
            query_params = request.get_query_parameters()
            for name in query_params:
                val = query_params[name]
                ps += '&' if ps.find('?')!=-1 else '?'
                ps += "%s=%s" % (name, self.__format_query_parameter_value(val))
            return ps

    def __format_query_parameter_value(self, value):
            if isinstance(value, list):
                return ','.join([quote(str(v)) for v in value])
            return quote(str(value))

    # Sign request with HMAC, request URI must be exacly the same
    # We have 30s to complete request with this token
    def __sign_url(self, req_part):
        uri = '/' + self.database_id + '/' + req_part
        time = self.__hmac_time(uri)
        sign = self.__hmac_sign(uri, time)
        res = uri + time + '&hmac_sign=' +sign
        return res

    def __hmac_time(self, uri):
        res = '&' if uri.find('?')!=-1 else '?'
        res += "hmac_timestamp=%s" % int(time.time())
        return res

    def __hmac_sign(self, uri, time):
        url = uri + time
        sign = hmac.new(str.encode(self.token), str.encode(url), sha1).hexdigest()
        return sign