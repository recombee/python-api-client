from recombee_api_client.api_requests.request import Request

class DeleteItem(Request):
    """
    Deletes an item of given `itemId` from the catalog.
    
    If there are any *purchases*, *ratings*, *bookmarks*, *cart additions* or *detail views* of the item present in the database, they will be deleted in cascade as well. Also, if the item is present in some *series*, it will be removed from all the *series* where present.
    
    If an item becomes obsolete/no longer available, it is often meaningful to keep it in the catalog (along with all the interaction data, which are very useful), and only exclude the item from recommendations. In such a case, use [ReQL filter](https://docs.recombee.com/reql.html) instead of deleting the item completely.

    """

    def __init__(self,item_id):
        """
        Required parameters:
        @param item_id: ID of the item to be deleted.
        
        """
        self.item_id = item_id
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'delete'
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
