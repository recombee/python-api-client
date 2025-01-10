import os
import time
import json
import hmac
from typing import Union
from enum import Enum

import requests
from hashlib import sha1
from urllib.parse import quote

from recombee_api_client.exceptions import ApiTimeoutException, ResponseException
from recombee_api_client.api_requests import Batch, Request


class Region(Enum):
    """
    Region of the Recombee cluster
    """
    AP_SE = 1
    CA_EAST = 2
    EU_WEST = 3
    US_WEST = 4


class RecombeeClient:
    """
    Client for sending requests to Recombee recommender system

    :param database_id: Name of your database_id at Recombee
    
    :param token: Secret token obtained from Recombee for signing requests
    
    :param protocol: Default protocol for sending requests. Possible values: 'http', 'https'.

    :param region: region of the Recombee cluster where the database is located
    """
    BATCH_MAX_SIZE = 10000

    def __init__(self, database_id: str, token: str, protocol: str = 'https', options: dict = None, region: Region = None):
        self.database_id = database_id
        self.token = token
        self.protocol = protocol

        self.base_uri = self.__get_base_uri(options=options or {}, region=region)

    def send(self, request: Request) -> Union[dict, str, list]:
        """
        :param request: Request to be sent to Recombee recommender
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

    @staticmethod
    def __get_regional_base_uri(region: Region) -> str:
        uri = {
            Region.AP_SE: 'rapi-ap-se.recombee.com',
            Region.CA_EAST: 'rapi-ca-east.recombee.com',
            Region.EU_WEST: 'rapi-eu-west.recombee.com',
            Region.US_WEST: 'rapi-us-west.recombee.com'
          }.get(region)

        if uri is None:
            raise ValueError('Unknown region given')
        return uri

    @staticmethod
    def __get_base_uri(options: dict, region: str) -> str:
        base_uri = os.environ.get('RAPI_URI') or options.get('base_uri')
        if region is not None:
            if base_uri:
                raise ValueError('base_uri and region cannot be specified at the same time')
            base_uri = RecombeeClient.__get_regional_base_uri(region)

        return base_uri or 'rapi.recombee.com'

    @staticmethod
    def __get_http_headers(additional_headers: dict = None) -> dict:
        headers = {'User-Agent': 'recombee-python-api-client/5.0.0'}
        if additional_headers:
            headers.update(additional_headers)
        return headers

    def __put(self, request: Request, uri: str, timeout: int):
        response = requests.put(uri, 
                                data=json.dumps(request.get_body_parameters()),
                                headers=self.__get_http_headers({'Content-Type': 'application/json'}),
                                timeout=timeout)
        self.__check_errors(response, request)
        return response.json()

    def __get(self, request: Request, uri: str, timeout: int):
        response = requests.get(uri,
                                headers=self.__get_http_headers(),
                                timeout=timeout)
        self.__check_errors(response, request)
        return response.json()

    def __post(self, request: Request, uri: str, timeout: int):
        response = requests.post(uri,
                                 data=json.dumps(request.get_body_parameters()),
                                 headers=self.__get_http_headers({'Content-Type': 'application/json'}),
                                 timeout=timeout)
        self.__check_errors(response, request)
        return response.json()

    def __delete(self, request: Request, uri: str, timeout: int):
        response = requests.delete(uri,
                                   data=json.dumps(request.get_body_parameters()),
                                   headers=self.__get_http_headers({'Content-Type': 'application/json'}),
                                   timeout=timeout)
        self.__check_errors(response, request)
        return response.json()

    def __check_errors(self, response, request: Request):
        status_code = response.status_code
        if status_code == 200 or status_code == 201:
            return
        raise ResponseException(request, status_code, response.text)

    @staticmethod
    def __get_list_chunks(l: list, n: int) -> list:
        """Yield successive n-sized chunks from l."""

        for i in range(0, len(l), n):
            yield l[i:i + n]

    def __send_multipart_batch(self, batch: Batch) -> list:
        requests_parts = [rqs for rqs in self.__get_list_chunks(batch.requests, self.BATCH_MAX_SIZE)]
        responses = [self.send(Batch(rqs)) for rqs in requests_parts]
        return sum(responses, [])

    def __process_request_uri(self, request: Request) -> str:
        uri = request.path
        uri += self.__query_parameters_to_url(request)
        return uri

    def __query_parameters_to_url(self, request: Request) -> str:
        ps = ''
        query_params = request.get_query_parameters()
        for name in query_params:
            val = query_params[name]
            ps += '&' if ps.find('?') != -1 else '?'
            ps += "%s=%s" % (name, self.__format_query_parameter_value(val))
        return ps

    @staticmethod
    def __format_query_parameter_value(value) -> str:
        if isinstance(value, list):
            return ','.join([quote(str(v)) for v in value])
        return quote(str(value))

    # Sign request with HMAC, request URI must be exactly the same
    # We have 30s to complete request with this token
    def __sign_url(self, req_part: str) -> str:
        uri = '/' + self.database_id + req_part
        time_part = self.__hmac_time(uri)
        sign = self.__hmac_sign(uri, time_part)
        res = uri + time_part + '&hmac_sign=' + sign
        return res

    def __hmac_time(self, uri: str) -> str:
        res = '&' if uri.find('?') != -1 else '?'
        res += "hmac_timestamp=%s" % int(time.time())
        return res

    def __hmac_sign(self, uri: str, time_part: str) -> str:
        url = uri + time_part
        sign = hmac.new(str.encode(self.token), str.encode(url), sha1).hexdigest()
        return sign
