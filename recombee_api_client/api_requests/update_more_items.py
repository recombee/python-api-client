from recombee_api_client.api_requests.request import Request
from recombee_api_client.utils.serialize_to_json import serialize_to_json
from typing import Union, List
from datetime import datetime
import uuid

DEFAULT = uuid.uuid4()


class UpdateMoreItems(Request):
    """
    Updates (some) property values of all the items that pass the filter.

    Example: *Setting all the items that are older than a week as unavailable*

      ```json
        {
          "filter": "'releaseDate' < now() - 7*24*3600",
          "changes": {"available": false}
        }
      ```

    Required parameters:

    :param filter: A [ReQL](https://docs.recombee.com/reql) expression, which returns `true` for the items that shall be updated.

    :param changes: A dictionary where the keys are properties that shall be updated.

    """

    def __init__(self, filter: str, changes: dict):
        super().__init__(
            path="/more-items/", method="post", timeout=100000, ensure_https=False
        )
        self.filter = filter
        self.changes = changes

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p["filter"] = serialize_to_json(self.filter)
        p["changes"] = serialize_to_json(self.changes)

        return p

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()

        return params
