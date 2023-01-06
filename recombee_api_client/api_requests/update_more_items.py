from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class UpdateMoreItems(Request):
    """
    Updates (some) property values of all the items that pass the filter.
    
    Example: *Setting all the items that are older than a week as unavailable*
    
      ```
        {
          "filter": "'releaseDate' < now() - 7*24*3600",
          "changes": {"available": false}
        }
      ```
    
    Required parameters:
    
    :param filter: A [ReQL](https://docs.recombee.com/reql.html) expression, which returns `true` for the items that shall be updated.
    
    :param changes: A dictionary where the keys are properties that shall be updated.
    

    """

    def __init__(self, filter: str, changes: dict):
        super().__init__(path="/more-items/", method='post', timeout=1000, ensure_https=False)
        self.filter = filter
        self.changes = changes

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p['filter'] = self.filter
        p['changes'] = self.changes
        return p

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
