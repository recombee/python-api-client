from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class DeleteUser(Request):
    """
    Deletes a user of the given *userId* from the database.
    
    If there are any purchases, ratings, bookmarks, cart additions or detail views made by the user present in the database, they will be deleted in cascade as well.
    
    Required parameters:
    
    :param user_id: ID of the user to be deleted.
    

    """

    def __init__(self, user_id: str):
        super().__init__(path="/users/%s" % (user_id), method='delete', timeout=1000, ensure_https=False)
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
