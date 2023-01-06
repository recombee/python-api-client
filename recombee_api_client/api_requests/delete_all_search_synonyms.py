from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class DeleteAllSearchSynonyms(Request):
    """
    Deletes all synonyms defined in the database.
    

    """

    def __init__(self):
        super().__init__(path="/synonyms/items/", method='delete', timeout=10000, ensure_https=False)

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
