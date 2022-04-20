from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class GetUserValues(Request):
    """
    Get all the current property values of a given user.
    
    Required parameters:
    
    :param user_id: ID of the user properties of which are to be obtained.
    
    

    """

    def __init__(self, user_id: str):
        super().__init__(path="/users/%s" % (user_id), method='get', timeout=1000, ensure_https=False)
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
