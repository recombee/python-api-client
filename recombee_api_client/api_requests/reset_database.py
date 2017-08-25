from recombee_api_client.api_requests.request import Request
import uuid

DEFAULT = uuid.uuid4()

class ResetDatabase(Request):
    """
    Completely erases all your data, including items, item properties, series, user database, purchases, ratings, detail views, and bookmarks. Make sure the request to be never executed in production environment! Resetting your database is irreversible.

    """

    def __init__(self):
        """
        """
        self.timeout = 239000
        self.ensure_https = False
        self.method = 'delete'
        self.path = "/" % ()

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
