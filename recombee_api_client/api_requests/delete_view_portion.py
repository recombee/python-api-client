from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class DeleteViewPortion(Request):
    """
    Deletes an existing view portion specified by (`userId`, `itemId`, `sessionId`) from the database.
    
    Required parameters:
    
    :param user_id: ID of the user who rated the item.
    
    :param item_id: ID of the item which was rated.
    
    
    Optional parameters:
    
    :param session_id: Identifier of a session.
    

    """

    def __init__(self, user_id: str, item_id: str, session_id: str = DEFAULT):
        super().__init__(path="/viewportions/", method='delete', timeout=3000, ensure_https=False)
        self.user_id = user_id
        self.item_id = item_id
        self.session_id = session_id

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        return p

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        params['userId'] = self.user_id
        params['itemId'] = self.item_id
        if self.session_id is not DEFAULT:
            params['sessionId'] = self.session_id
        return params
