from recombee_api_client.api_requests.request import Request

class DeleteUser(Request):
    """
    Deletes a user of given *userId* from the database.
    
    If there are any purchases, ratings, bookmarks, cart additions or detail views made by the user present in the database, they will be deleted in cascade as well.

    """

    def __init__(self,user_id):
        """
        Required parameters:
        @param user_id: ID of the user to be added.
        
        """
        self.user_id = user_id
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'delete'
        self.path = "/{databaseId}/users/%s" % (self.user_id)

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
