from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class AddGroup(Request):
    """
    Creates a new group in the database.
    Required parameters:
    
    :param group_id: ID of the group to be created.
    

    """

    def __init__(self, group_id: str):
        super().__init__(path="/groups/%s" % (group_id), method='put', timeout=1000, ensure_https=False)
        self.group_id = group_id

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
