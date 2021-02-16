from recombee_api_client.api_requests.request import Request
import uuid

DEFAULT = uuid.uuid4()

class DeleteSearchSynonym(Request):
    """
    Deletes synonym of given `id` and this synonym is no longer taken into account in the [Search items](https://docs.recombee.com/api.html#search-items).
    
    Required parameters:
    
    :param id: ID of the synonym that should be deleted.
    

    """

    def __init__(self, id):
        self.id = id
        self.timeout = 10000
        self.ensure_https = False
        self.method = 'delete'
        self.path = "/synonyms/items/%s" % (self.id)

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
        return params
