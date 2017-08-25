from recombee_api_client.api_requests.request import Request
import uuid

DEFAULT = uuid.uuid4()

class UserBasedRecommendation(Request):
    """
    Based on user's past interactions (purchases, ratings, etc.) with the items, recommends top-N items that are most likely to be of high value for a given user.
    
    It is also possible to use POST HTTP method (for example in case of very long ReQL filter) - query parameters then become body parameters.

    """

    def __init__(self, user_id, count, filter=DEFAULT, booster=DEFAULT, allow_nonexistent=DEFAULT, cascade_create=DEFAULT, scenario=DEFAULT, return_properties=DEFAULT, included_properties=DEFAULT, diversity=DEFAULT, min_relevance=DEFAULT, rotation_rate=DEFAULT, rotation_time=DEFAULT, expert_settings=DEFAULT):
        """
        Required parameters:
        @param user_id: ID of the user whose personalized recommendations are to be generated.
        
        @param count: Number of items to be recommended (N for the top-N recommendation).
        
        
        Optional parameters:
        @param filter: Boolean-returning [ReQL](https://docs.recombee.com/reql.html) expression which allows you to filter recommended items based on the values of their attributes.
        
        @param booster: Number-returning [ReQL](https://docs.recombee.com/reql.html) expression which allows you to boost recommendation rate of some items based on the values of their attributes.
        
        @param allow_nonexistent: If the user does not exist in the database, returns a list of non-personalized recommendations instead of causing HTTP 404 error. It doesn't create the user in the database.
        
        @param cascade_create: If the user does not exist in the database, returns a list of non-personalized recommendations and creates the user in the database. This allows for example rotations in the following recommendations for that user, as the user will be already known to the system.
        
        @param scenario: Scenario defines a particular application of recommendations. It can be for example "homepage", "cart" or "emailing". You can see each scenario in the UI separately, so you can check how well each application performs. The AI which optimizes models in order to get the best results may optimize different scenarios separately, or even use different models in each of the scenarios.
        
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
        
        
        @param rotation_time: **Expert option** Taking *rotationRate* into account, specifies how long time it takes to an item to recover from the penalization. For example, `rotationTime=7200.0` means that items recommended less than 2 hours ago are penalized.
        
        
        @param expert_settings: Dictionary of custom options.
        
        
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
        self.expert_settings = expert_settings
        self.timeout = 3000
        self.ensure_https = False
        self.method = 'post'
        self.path = "/users/%s/recomms/" % (self.user_id)

    def get_body_parameters(self):
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p['count'] = self.count
        if self.filter is not DEFAULT:
            p['filter'] = self.filter
        if self.booster is not DEFAULT:
            p['booster'] = self.booster
        if self.allow_nonexistent is not DEFAULT:
            p['allowNonexistent'] = self.allow_nonexistent
        if self.cascade_create is not DEFAULT:
            p['cascadeCreate'] = self.cascade_create
        if self.scenario is not DEFAULT:
            p['scenario'] = self.scenario
        if self.return_properties is not DEFAULT:
            p['returnProperties'] = self.return_properties
        if self.included_properties is not DEFAULT:
            p['includedProperties'] = self.included_properties
        if self.diversity is not DEFAULT:
            p['diversity'] = self.diversity
        if self.min_relevance is not DEFAULT:
            p['minRelevance'] = self.min_relevance
        if self.rotation_rate is not DEFAULT:
            p['rotationRate'] = self.rotation_rate
        if self.rotation_time is not DEFAULT:
            p['rotationTime'] = self.rotation_time
        if self.expert_settings is not DEFAULT:
            p['expertSettings'] = self.expert_settings
        return p

    def get_query_parameters(self):
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
