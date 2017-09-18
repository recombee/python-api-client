from recombee_api_client.api_requests.request import Request
import uuid

DEFAULT = uuid.uuid4()

class ListUserViewPortions(Request):
    """
    The view portions feature is currently experimental.
    
    List all the view portions ever submitted by a given user.

    """

    def __init__(self, user_id):
        """
        Required parameters:
        @param user_id: ID of the user whose view portions are to be listed.
        
        """
        self.user_id = user_id
        self.timeout = 100000
        self.ensure_https = False
        self.method = 'get'
        self.path = "/users/%s/viewportions/" % (self.user_id)

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
