from recombee_api_client.api_requests.request import Request

class ListSeriesItems(Request):
    """
    List all the items present in the given series, sorted according to their time index values.
    """

    def __init__(self,series_id):
        """
        Required parameters:
        @param series_id: ID of the series items of which are to be listed.
        
        """
        self.series_id = series_id
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'get'
        self.path = "/{databaseId}/series/%s/items/" % (self.series_id)

    def get_body_parameters(self):
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        return p

    def get_query_parameters(self):
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
