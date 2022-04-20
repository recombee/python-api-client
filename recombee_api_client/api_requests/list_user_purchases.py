from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class ListUserPurchases(Request):
    """
    List all the purchases ever made by a given user.
    Required parameters:
    
    :param user_id: ID of the user whose purchases are to be listed.
    

    """

    def __init__(self, user_id: str):
        super().__init__(path="/users/%s/purchases/" % (user_id), method='get', timeout=100000, ensure_https=False)
        self.user_id = user_id

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
        return params
