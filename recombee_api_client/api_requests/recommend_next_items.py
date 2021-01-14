from recombee_api_client.api_requests.request import Request
import uuid

DEFAULT = uuid.uuid4()

class RecommendNextItems(Request):
    """
    Returns items that shall be shown to a user as next recommendations when the user e.g. scrolls the page down (*infinite scroll*) or goes to a next page.
    
    It accepts `recommId` of a base recommendation request (e.g. request from the first page) and number of items that shall be returned (`count`).
    The base request can be one of:
      - [Recommend items to item](https://docs.recombee.com/api.html#recommend-items-to-item)
      - [Recommend items to user](https://docs.recombee.com/api.html#recommend-items-to-user)
      - [Search items](https://docs.recombee.com/api.html#search-items)
    
    All the other parameters are inherited from the base request.
    
    *Recommend next items* can be called many times for a single `recommId` and each call returns different (previously not recommended) items.
    The number of *Recommend next items* calls performed so far is returned in the `numberNextRecommsCalls` field.
    
    *Recommend next items* can be requested up to 30 minutes after the base request or a previous *Recommend next items* call.
    
    For billing purposes, each call to *Recommend next items* is counted as a separate recommendation request.
    
    Required parameters:
    
    :param recomm_id: ID of the base recommendation request for which next recommendations should be returned
    
    :param count: Number of items to be recommended
    
    

    """

    def __init__(self, recomm_id, count):
        self.recomm_id = recomm_id
        self.count = count
        self.timeout = 3000
        self.ensure_https = False
        self.method = 'post'
        self.path = "/recomms/next/items/%s" % (self.recomm_id)

    def get_body_parameters(self):
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p['count'] = self.count
        return p

    def get_query_parameters(self):
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
