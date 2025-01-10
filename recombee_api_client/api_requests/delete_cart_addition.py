from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class DeleteCartAddition(Request):
    """
    Deletes an existing cart addition uniquely specified by `userId`, `itemId`, and `timestamp` or all the cart additions with the given `userId` and `itemId` if `timestamp` is omitted.
    
    Required parameters:
    
    :param user_id: ID of the user who made the cart addition.
    
    :param item_id: ID of the item which was added to the cart.
    
    
    Optional parameters:
    
    :param timestamp: Unix timestamp of the cart addition. If the `timestamp` is omitted, then all the cart additions with the given `userId` and `itemId` are deleted.
    

    """

    def __init__(self, user_id: str, item_id: str, timestamp: Union[str, int] = DEFAULT):
        super().__init__(path="/cartadditions/", method='delete', timeout=3000, ensure_https=False)
        self.user_id = user_id
        self.item_id = item_id
        self.timestamp = timestamp

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
        if self.timestamp is not DEFAULT:
            params['timestamp'] = self.timestamp
        return params
