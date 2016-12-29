# -*- coding: utf-8 -*-

from recombee_api_client.api_requests.request import Request

class Batch(Request):
    """
    Batch request for submitting an arbitrary sequence of requests

    In many cases, it may be desirable to execute multiple requests at once. By example, when synchronizing the catalog of items in periodical manner, you would have to execute a sequence of thousands of separate POST requests, which is very ineffective and may take a very long time to complete. Most notably, network latencies can make execution of such a sequence very slow and even if executed in multiple parallel threads, there will still be unreasonable overhead caused by the HTTP(s). To avoid the problems mentioned, batch processing may be used, encapsulating a sequence of requests into a single HTTP request.
    Batch processing allows you to submit arbitrary sequence of requests in form of JSON array. Any type of request from the above documentation may be used in the batch, and the batch may combine different types of requests arbitrarily as well.
    Note that:
    - executing the requests in a batch is equivalent as if they were executed one-by-one individually; there are, however, many optimizations to make batch execution as fast as possible,
    - the status code of the batch request itself is 200 even if the individual requests result in error - you have to inspect the code values in the resulting array,
    - if the status code of the whole batch is not 200, then there is an error in the batch request itself; in such a case, the error message returned should help you to resolve the problem,
    """

    def __init__(self, requests, distinctRecomms=None):
        """
        @param requests: List of Requests.
        @param distinctRecomms: Makes all the recommended items for a certain user distinct among multiple recommendation requests in the batch.
        """
        self.requests = requests
        self.distinctRecomms = distinctRecomms
        self.timeout = sum([req.timeout for req in self.requests])
        self.ensure_https = True
        self.method = 'post'
        self.path = '/{databaseId}/batch/'

    def get_body_parameters(self):
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        reqs = []
        for r in self.requests:
            reqs.append(self.__request_to_batch_dict(r))
        result = {'requests': reqs}
        if self.distinctRecomms is not None:
            result['distinctRecomms'] = self.distinctRecomms
        return result

    def __request_to_batch_dict(self, req):

        path = req.path
        path = path[len('/{databaseId}'):]
        bd = {
            'method': req.method.upper(),
            'path':path
        }
        params = req.get_query_parameters()

        if len(req.get_body_parameters()) > 0:
            params.update(req.get_body_parameters())
            
        if len(params) > 0:
            bd['params'] = params
        return bd

    def get_query_parameters(self):
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        return dict()