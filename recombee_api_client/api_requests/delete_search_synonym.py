from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class DeleteSearchSynonym(Request):
    """
    Deletes synonym of the given `id`. This synonym is no longer taken into account in the [Search items](https://docs.recombee.com/api.html#search-items).
    
    Required parameters:
    
    :param id: ID of the synonym that should be deleted.
    

    """

    def __init__(self, id: str):
        super().__init__(path="/synonyms/items/%s" % (id), method='delete', timeout=10000, ensure_https=False)
        self.id = id

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
