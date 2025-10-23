from recombee_api_client.api_requests.request import Request
from recombee_api_client.utils.serialize_to_json import serialize_to_json
from typing import Union, List
from datetime import datetime
import uuid

DEFAULT = uuid.uuid4()


class ListSegmentations(Request):
    """
    Return all existing items Segmentations.

    Required parameters:

    :param source_type: List Segmentations based on a particular type of data. Currently only `items` are supported.

    """

    def __init__(self, source_type: str):
        super().__init__(
            path="/segmentations/list/", method="get", timeout=10000, ensure_https=False
        )
        self.source_type = source_type

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
        params["sourceType"] = serialize_to_json(self.source_type)

        return params
