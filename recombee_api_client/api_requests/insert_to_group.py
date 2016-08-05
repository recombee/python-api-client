from recombee_api_client.api_requests.request import Request

class InsertToGroup(Request):
    """
    Inserts an existing item/group into group of given `groupId`.

    """

    def __init__(self,group_id, item_type, item_id, cascade_create=None):
        """
        Required parameters:
        @param group_id: ID of the group to be inserted into.
        
        @param item_type: `item` iff the regular item from the catalog is to be inserted, `group` iff group is inserted as the item.
        
        @param item_id: ID of the item iff `itemType` is `item`. ID of the group iff `itemType` is `group`.
        
        
        Optional parameters:
        @param cascade_create: Indicates that any non-existing entity specified within the request should be created (as is corresponding PUT requests were invoked). This concerns both the `groupId` and the `groupId`. If `cascadeCreate` is set true, the behavior also depends on the `itemType`. Either items or group may be created if not present in the database.
        
        """
        self.group_id = group_id
        self.item_type = item_type
        self.item_id = item_id
        self.cascade_create = cascade_create
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'post'
        self.path = "/{databaseId}/groups/%s/items/" % (self.group_id)

    def get_body_parameters(self):
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p['itemType'] = self.item_type
        p['itemId'] = self.item_id
        if self.cascade_create is not None:
            p['cascadeCreate'] = self.cascade_create
        return p

    def get_query_parameters(self):
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
