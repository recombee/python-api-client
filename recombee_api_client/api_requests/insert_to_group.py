from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class InsertToGroup(Request):
    """
    Inserts an existing item/group into a group of the given `groupId`.
    
    Required parameters:
    
    :param group_id: ID of the group to be inserted into.
    
    :param item_type: `item` iff the regular item from the catalog is to be inserted, `group` iff group is inserted as the item.
    
    :param item_id: ID of the item iff `itemType` is `item`. ID of the group iff `itemType` is `group`.
    
    
    Optional parameters:
    
    :param cascade_create: Indicates that any non-existing entity specified within the request should be created (as if corresponding PUT requests were invoked). This concerns both the `groupId` and the `groupId`. If `cascadeCreate` is set to true, the behavior also depends on the `itemType`. Either items or group may be created if not present in the database.
    

    """

    def __init__(self, group_id: str, item_type: str, item_id: str, cascade_create: bool = DEFAULT):
        super().__init__(path="/groups/%s/items/" % (group_id), method='post', timeout=1000, ensure_https=False)
        self.group_id = group_id
        self.item_type = item_type
        self.item_id = item_id
        self.cascade_create = cascade_create

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p['itemType'] = self.item_type
        p['itemId'] = self.item_id
        if self.cascade_create is not DEFAULT:
            p['cascadeCreate'] = self.cascade_create
        return p

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
