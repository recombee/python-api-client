from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class RemoveFromGroup(Request):
    """
    Removes an existing group item from the group.
    Required parameters:
    
    :param group_id: ID of the group from which a group item is to be removed.
    
    :param item_type: Type of the item to be removed.
    
    :param item_id: ID of the item iff `itemType` is `item`. ID of the group iff `itemType` is `group`.
    

    """

    def __init__(self, group_id: str, item_type: str, item_id: str):
        super().__init__(path="/groups/%s/items/" % (group_id), method='delete', timeout=1000, ensure_https=False)
        self.group_id = group_id
        self.item_type = item_type
        self.item_id = item_id

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
        params['itemType'] = self.item_type
        params['itemId'] = self.item_id
        return params
