from recombee_api_client.api_requests.request import Request

class GetItemValues(Request):
    """
    Get all the current property values of a given item.

    """

    def __init__(self,item_id):
        """
        Required parameters:
        @param item_id: ID of the item properties of which are to be obtained.
        
        
        """
        self.item_id = item_id
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'get'
        self.path = "/{databaseId}/items/%s" % (self.item_id)

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
