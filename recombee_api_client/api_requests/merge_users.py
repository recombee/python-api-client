from recombee_api_client.api_requests.request import Request

class MergeUsers(Request):
    """
    Merges purchases, ratings, bookmarks, and detail views of two different users under a single user ID. This is especially useful for online e-commerce applications working with anonymous users identified by unique tokens such as the session ID. In such applications, it may often happen that a user owns a persistent account, yet accesses the system anonymously while, e.g., putting items into a shopping cart. At some point in time, such as when the user wishes to confirm the purchase, (s)he logs into the system using his/her username and password. The interactions made under anonymous session ID then become connected with the persistent account, and merging these two together becomes desirable.
    
    
    Merging happens between two users referred to as the *source* and the *target*. After the merge, all the interactions of the source user are attributed to the target user, and the source user is **deleted** unless special parameter `keepSourceUser` is set `true`.

    """

    def __init__(self,target_user_id, source_user_id, keep_source_user=None):
        """
        Required parameters:
        @param target_user_id: ID of the source user.
        
        @param source_user_id: ID of the target user.
        
        
        Optional parameters:
        @param keep_source_user: If true, the source user will not be deleted, but also kept in the database..
        
        """
        self.target_user_id = target_user_id
        self.source_user_id = source_user_id
        self.keep_source_user = keep_source_user
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'put'
        self.path = "/{databaseId}/users/%s/merge/%s" % (self.target_user_id,self.source_user_id)

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
        if self.keep_source_user is not None:
            params['keepSourceUser'] = self.keep_source_user
        return params
