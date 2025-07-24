from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class MergeUsers(Request):
    """
    Merges interactions (purchases, ratings, bookmarks, detail views ...) of two different users under a single user ID. This is especially useful for online e-commerce applications working with anonymous users identified by unique tokens such as the session ID. In such applications, it may often happen that a user owns a persistent account, yet accesses the system anonymously while, e.g., putting items into a shopping cart. At some point in time, such as when the user wishes to confirm the purchase, (s)he logs into the system using his/her username and password. The interactions made under anonymous session ID then become connected with the persistent account, and merging these two becomes desirable.
    
    
    Merging happens between two users referred to as the *target* and the *source*. After the merge, all the interactions of the source user are attributed to the target user, and the source user is **deleted**.
    
    By default, the *Merge Users* request is only available from server-side integrations for security reasons, to prevent potential abuse.
    If you need to call this request from a client-side environment (such as a web or mobile app), please contact our support and request access to enable this feature for your database.
    
    Required parameters:
    
    :param target_user_id: ID of the target user.
    
    :param source_user_id: ID of the source user.
    
    
    Optional parameters:
    
    :param cascade_create: Sets whether the user *targetUserId* should be created if not present in the database.
    

    """

    def __init__(self, target_user_id: str, source_user_id: str, cascade_create: bool = DEFAULT):
        super().__init__(path="/users/%s/merge/%s" % (target_user_id,source_user_id), method='put', timeout=10000, ensure_https=False)
        self.target_user_id = target_user_id
        self.source_user_id = source_user_id
        self.cascade_create = cascade_create

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
        if self.cascade_create is not DEFAULT:
            params['cascadeCreate'] = self.cascade_create
        return params
