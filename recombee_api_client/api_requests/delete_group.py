from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class DeleteGroup(Request):
    """
    Deletes the group of the given `groupId` from the database.
    
    Deleting a group will only delete the assignment of items to it, not the items themselves!
    
    Required parameters:
    
    :param group_id: ID of the group to be deleted.
    

    """

    def __init__(self, group_id: str):
        super().__init__(path="/groups/%s" % (group_id), method='delete', timeout=1000, ensure_https=False)
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
