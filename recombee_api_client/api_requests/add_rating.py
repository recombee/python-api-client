from recombee_api_client.api_requests.request import Request

class AddRating(Request):
    """
    Adds a rating of given item made by a given user.

    """

    def __init__(self,user_id, item_id, rating, timestamp=None, cascade_create=None):
        """
        Required parameters:
        @param user_id: User who submitted the rating
        
        @param item_id: Rated item
        
        @param rating: Rating rescaled to interval [-1.0,1.0], where -1.0 means the worst rating possible, 0.0 means neutral, and 1.0 means absolutely positive rating. For example, in the case of 5-star evaluations, rating = (numStars-3)/2 formula may be used for the conversion.
        
        
        Optional parameters:
        @param timestamp: UTC timestamp of the rating as ISO8601-1 pattern or UTC epoch time. The default value is the current time.
        
        @param cascade_create: Sets whether the given user/item should be created if not present in the database.
        
        """
        self.user_id = user_id
        self.item_id = item_id
        self.rating = rating
        self.timestamp = timestamp
        self.cascade_create = cascade_create
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'post'
        self.path = "/{databaseId}/ratings/" % ()

    def get_body_parameters(self):
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p['userId'] = self.user_id
        p['itemId'] = self.item_id
        p['rating'] = self.rating
        if self.timestamp is not None:
            p['timestamp'] = self.timestamp
        if self.cascade_create is not None:
            p['cascadeCreate'] = self.cascade_create
        return p

    def get_query_parameters(self):
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
