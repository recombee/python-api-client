from recombee_api_client.api_requests.request import Request

class AddItem(Request):
    """
    Adds new item of given `itemId` to the items catalog.
    
    All the item properties for the newly created items are set null.

    """

    def __init__(self,item_id):
        """
        Required parameters:
        @param item_id: ID of the item to be created.
        
        """
        self.item_id = item_id
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'put'
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
