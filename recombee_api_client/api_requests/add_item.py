from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class AddItem(Request):
    """
    Adds new item of the given `itemId` to the items catalog.
    
    All the item properties for the newly created items are set to null.
    
    Required parameters:
    
    :param item_id: ID of the item to be created.
    

    """

    def __init__(self, item_id: str):
        super().__init__(path="/items/%s" % (item_id), method='put', timeout=1000, ensure_https=False)
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
        return params
