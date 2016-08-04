from recombee_api_client.api_requests.request import Request

class RemoveFromGroup(Request):
    """
    Removes an existing group item from the group.
    """

    def __init__(self,group_id, item_type, item_id):
        """
        Required parameters:
        @param group_id: ID of the group from which a group item is to be removed.
        
        @param item_type: Type of the item to be removed.
        
        @param item_id: ID of the item iff `itemType` is `item`. ID of the group iff `itemType` is `group`.
        
        """
        self.group_id = group_id
        self.item_type = item_type
        self.item_id = item_id
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'delete'
        self.path = "/{databaseId}/groups/%s/items/" % (self.group_id)

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
        params['itemType'] = self.item_type
        params['itemId'] = self.item_id
        return params
