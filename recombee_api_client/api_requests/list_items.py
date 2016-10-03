from recombee_api_client.api_requests.request import Request

class ListItems(Request):
    """
    Gets a list of IDs of items currently present in the catalog.
    """

    def __init__(self,filter=None):
        """
        
        Optional parameters:
        @param filter: Boolean-returning [ReQL](https://docs.recombee.com/reql.html) expression, which allows you to filter items to be listed. Only the items for which the expression is *true* will be returned.
        
        """
        self.filter = filter
        self.timeout = 30000
        self.ensure_https = False
        self.method = 'get'
        self.path = "/{databaseId}/items/list/" % ()

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
        if self.filter is not None:
            params['filter'] = self.filter
        return params
