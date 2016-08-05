from recombee_api_client.api_requests.request import Request

class DeleteRating(Request):
    """
    Deletes an existing rating specified by (`userId`, `itemId`, `timestamp`) from the database or all the ratings with given `userId` and `itemId` if `timestamp` is omitted.

    """

    def __init__(self,user_id, item_id, timestamp=None):
        """
        Required parameters:
        @param user_id: ID of the user who rated the item.
        
        @param item_id: ID of the item which was rated.
        
        
        Optional parameters:
        @param timestamp: Unix timestamp of the rating. If the `timestamp` is omitted, then all the ratings with given `userId` and `itemId` are deleted.
        
        """
        self.user_id = user_id
        self.item_id = item_id
        self.timestamp = timestamp
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'delete'
        self.path = "/{databaseId}/ratings/" % ()

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
        params['userId'] = self.user_id
        params['itemId'] = self.item_id
        if self.timestamp is not None:
            params['timestamp'] = self.timestamp
        return params
