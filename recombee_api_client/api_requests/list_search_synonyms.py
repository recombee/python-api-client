from recombee_api_client.api_requests.request import Request
import uuid

DEFAULT = uuid.uuid4()

class ListSearchSynonyms(Request):
    """
    Gives the list of synonyms defined in the database.
    
    Optional parameters:
    
    :param count: The number of synonyms to be listed.
    
    :param offset: Specifies the number of synonyms to skip (ordered by `term`).
    

    """

    def __init__(self, count=DEFAULT, offset=DEFAULT):
        self.count = count
        self.offset = offset
        self.timeout = 100000
        self.ensure_https = False
        self.method = 'get'
        self.path = "/synonyms/items/" % ()

    def get_body_parameters(self):
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        return p

    def get_query_parameters(self):
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        if self.count is not DEFAULT:
            params['count'] = self.count
        if self.offset is not DEFAULT:
            params['offset'] = self.offset
        return params
