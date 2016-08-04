from recombee_api_client.api_requests.request import Request

class ListUserBookmarks(Request):
    """
    List all the bookmarks ever made by a given user.
    """

    def __init__(self,user_id):
        """
        Required parameters:
        @param user_id: ID of the user whose bookmarks are to be listed.
        
        """
        self.user_id = user_id
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'get'
        self.path = "/{databaseId}/users/%s/bookmarks/" % (self.user_id)

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
