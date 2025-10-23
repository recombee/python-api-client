from recombee_api_client.api_requests.request import Request
from recombee_api_client.utils.serialize_to_json import serialize_to_json
from typing import Union, List
from datetime import datetime
import uuid

DEFAULT = uuid.uuid4()


class ListSearchSynonyms(Request):
    """
    Gives the list of synonyms defined in the database.

    Optional parameters:

    :param count: The number of synonyms to be listed.

    :param offset: Specifies the number of synonyms to skip (ordered by `term`).

    """

    def __init__(self, count: int = DEFAULT, offset: int = DEFAULT):
        super().__init__(
            path="/synonyms/items/", method="get", timeout=100000, ensure_https=False
        )
        self.count = count
        self.offset = offset

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
        if self.count is not DEFAULT:
            params["count"] = serialize_to_json(self.count)
        if self.offset is not DEFAULT:
            params["offset"] = serialize_to_json(self.offset)

        return params
