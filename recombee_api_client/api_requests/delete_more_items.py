from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class DeleteMoreItems(Request):
    """
    Deletes all the items that pass the filter.
    
    If an item becomes obsolete/no longer available, it is meaningful to **keep it in the catalog** (along with all the interaction data, which are very useful) and **only exclude the item from recommendations**. In such a case, use [ReQL filter](https://docs.recombee.com/reql.html) instead of deleting the item completely.
    Required parameters:
    
    :param filter: A [ReQL](https://docs.recombee.com/reql.html) expression, which returns `true` for the items that shall be updated.
    

    """

    def __init__(self, filter: str):
        super().__init__(path="/more-items/", method='delete', timeout=1000, ensure_https=False)
        self.filter = filter

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p['filter'] = self.filter
        return p

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
