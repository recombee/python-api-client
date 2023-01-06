from recombee_api_client.api_requests.request import Request
from typing import Union, List
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
        super().__init__(path="/synonyms/items/", method='get', timeout=100000, ensure_https=False)
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
            params['count'] = self.count
        if self.offset is not DEFAULT:
            params['offset'] = self.offset
        return params
