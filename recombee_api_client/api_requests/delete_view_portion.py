from recombee_api_client.api_requests.request import Request
import uuid

DEFAULT = uuid.uuid4()

class DeleteViewPortion(Request):
    """
    The view portions feature is currently experimental.
    
    Deletes an existing view portion specified by (`userId`, `itemId`, `sessionId`) from the database.

    """

    def __init__(self, user_id, item_id, session_id=DEFAULT):
        """
        Required parameters:
        @param user_id: ID of the user who rated the item.
        
        @param item_id: ID of the item which was rated.
        
        
        Optional parameters:
        @param session_id: Identifier of a session.
        
        """
        self.user_id = user_id
        self.item_id = item_id
        self.session_id = session_id
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'delete'
        self.path = "/viewportions/" % ()

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
        if self.session_id is not DEFAULT:
            params['sessionId'] = self.session_id
        return params
