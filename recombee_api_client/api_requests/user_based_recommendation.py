from recombee_api_client.api_requests.request import Request

class UserBasedRecommendation(Request):
    """
    Based on user's past interactions (purchases, ratings, etc.) with the items, recommends top-N items that are most likely to be of high value for a given user.

    """

    def __init__(self,user_id, count, filter=None, booster=None, allow_nonexistent=None, cascade_create=None, scenario=None, return_properties=None, included_properties=None, diversity=None, min_relevance=None, rotation_rate=None, rotation_time=None):
        """
        Required parameters:
        @param user_id: ID of the user whose personalized recommendations are to be generated.
        
        @param count: Number of items to be recommended (N for the top-N recommendation).
        
        
        Optional parameters:
        @param filter: Boolean-returning [ReQL](https://docs.recombee.com/reql.html) expression which allows you to filter recommended items based on the values of their attributes.
        
        @param booster: Number-returning [ReQL](https://docs.recombee.com/reql.html) expression which allows you to boost recommendation rate of some items based on the values of their attributes.
        
        @param allow_nonexistent: If the user does not exist in the database, returns a list of non-personalized recommendations instead of causing HTTP 404 error. It doesn't create the user in the database.
        
        @param cascade_create: If the user does not exist in the database, returns a list of non-personalized recommendations and creates the user in the database. This allows for example rotations in the following recommendations for that user, as the user will be already known to the system.
        
        @param scenario: Scenario defines a particular application of recommendations. It can be for example "homepage" or "cart". The AI which optimizes models in order to get the best results may optimize different scenarios separately, or even use different models in each of the scenarios.
        
        @param return_properties: With `returnProperties=true`, property values of the recommended items are returned along with their IDs in a JSON dictionary. The acquired property values can be used for easy displaying of the recommended items to the user. 
        
        
        Example response:
        
        ```
        
        [
        
        E{lb}
        
        "itemId": "tv-178",
        
        "description": "4K TV with 3D feature",
        
        "categories":   ["Electronics", "Televisions"],
        
        "price": 342,
        
        "url": "myshop.com/tv-178"
        E{rb},
        
        E{lb}
        
        "itemId": "mixer-42",
        
        "description": "Stainless Steel Mixer",
        
        "categories":   ["Home & Kitchen"],
        
        "price": 39,
        
        "url": "myshop.com/mixer-42"
        E{rb}
        
        ]
        
        ```
        
        
        @param included_properties: Allows to specify, which properties should be returned when `returnProperties=true` is set. The properties are given as a comma-separated list. 
        
        
        Example response for `includedProperties=description,price`:
        
        ```
        
        [
        
        E{lb}
        
        "itemId": "tv-178",
        
        "description": "4K TV with 3D feature",
        
        "price": 342
        E{rb},
        
        E{lb}
        
        "itemId": "mixer-42",
        
        "description": "Stainless Steel Mixer",
        
        "price": 39
        E{rb}
        
        ]
        
        ```
        
        
        @param diversity: **Expert option** Real number from [0.0, 1.0] which determines how much mutually dissimilar should the recommended items be. The default value is 0.0, i.e., no diversification. Value 1.0 means maximal diversification.
        
        
        @param min_relevance: **Expert option** Specifies the threshold of how much relevant must the recommended items be to the user. Possible values one of: "low", "medium", "high". The default value is "low", meaning that the system attempts to recommend number of items equal to *count* at any cost. If there are not enough data (such as interactions or item properties), this may even lead to bestseller-based recommendations to be appended to reach the full *count*. This behavior may be suppressed by using "medium" or "high" values. In such case, the system only recommends items of at least the requested qualit, and may return less than *count* items when there is not enough data to fulfill it.
        
        
        @param rotation_rate: **Expert option** If your users browse the system in real-time, it may easily happen that you wish to offer them recommendations multiple times. Here comes the question: how much should the recommendations change? Should they remain the same, or should they rotate? Recombee API allows you to control this per-request in backward fashion. You may penalize an item for being recommended in the near past. For the specific user, `rotationRate=1` means maximal rotation, `rotationRate=0` means absolutely no rotation. You may also use, for example `rotationRate=0.2` for only slight rotation of recommended items.
        
        
        @param rotation_time: **Expert option** Taking *rotationRate* into account, specifies how long time it takes to an item to fully recover from the penalization. For example, `rotationTime=7200.0` means that items recommended more than 2 hours ago are definitely not penalized anymore. Currently, the penalization is linear, so for `rotationTime=7200.0`, an item is still penalized by `0.5` to the user after 1 hour.
        
        
        """
        self.user_id = user_id
        self.count = count
        self.filter = filter
        self.booster = booster
        self.allow_nonexistent = allow_nonexistent
        self.cascade_create = cascade_create
        self.scenario = scenario
        self.return_properties = return_properties
        self.included_properties = included_properties
        self.diversity = diversity
        self.min_relevance = min_relevance
        self.rotation_rate = rotation_rate
        self.rotation_time = rotation_time
        self.timeout = 3000
        self.ensure_https = False
        self.method = 'get'
        self.path = "/{databaseId}/users/%s/recomms/" % (self.user_id)

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
        params['count'] = self.count
        if self.filter is not None:
            params['filter'] = self.filter
        if self.booster is not None:
            params['booster'] = self.booster
        if self.allow_nonexistent is not None:
            params['allowNonexistent'] = self.allow_nonexistent
        if self.cascade_create is not None:
            params['cascadeCreate'] = self.cascade_create
        if self.scenario is not None:
            params['scenario'] = self.scenario
        if self.return_properties is not None:
            params['returnProperties'] = self.return_properties
        if self.included_properties is not None:
            params['includedProperties'] = self.included_properties
        if self.diversity is not None:
            params['diversity'] = self.diversity
        if self.min_relevance is not None:
            params['minRelevance'] = self.min_relevance
        if self.rotation_rate is not None:
            params['rotationRate'] = self.rotation_rate
        if self.rotation_time is not None:
            params['rotationTime'] = self.rotation_time
        return params
