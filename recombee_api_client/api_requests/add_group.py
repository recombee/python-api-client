from recombee_api_client.api_requests.request import Request

class AddGroup(Request):
    """
    Creates new group in the database.
    """

    def __init__(self,group_id):
        """
        Required parameters:
        @param group_id: ID of the group to be created.
        
        """
        self.group_id = group_id
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'put'
        self.path = "/{databaseId}/groups/%s" % (self.group_id)

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
