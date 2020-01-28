from recombee_api_client.api_requests.request import Request
import uuid

DEFAULT = uuid.uuid4()

class SearchItems(Request):
    """
    Full-text personalized search. The results are based on the provided `searchQuery` and also on the user's past interactions (purchases, ratings, etc.) with the items (items more suitable for the user are preferred in the results).
    
    All the string and set item properties are indexed by the search engine.
    
    This endpoint should be used in a search box at your website/app. It can be called multiple times as the user is typing the query in order to get the most viable suggestions based on current state of the query, or once after submitting the whole query. 
    
    It is also possible to use POST HTTP method (for example in case of very long ReQL filter) - query parameters then become body parameters.
    
    The returned items are sorted by relevancy (first item being the most relevant).

    """

    def __init__(self, user_id, search_query, count, scenario=DEFAULT, cascade_create=DEFAULT, return_properties=DEFAULT, included_properties=DEFAULT, filter=DEFAULT, booster=DEFAULT, logic=DEFAULT, expert_settings=DEFAULT, return_ab_group=DEFAULT):
        """
        Required parameters:
        @param user_id: ID of the user for whom personalized search will be performed.
        
        @param search_query: Search query provided by the user. It is used for the full-text search.
        
        @param count: Number of items to be returned (N for the top-N results).
        
        
        Optional parameters:
        @param scenario: Scenario defines a particular search field in your user interface.
        
        
        You can set various settings to the [scenario](https://docs.recombee.com/scenarios.html) in the [Admin UI](https://admin.recombee.com). You can also see performance of each scenario in the Admin UI separately, so you can check how well each field performs.
        
        
        The AI which optimizes models in order to get the best results may optimize different scenarios separately, or even use different models in each of the scenarios.
        
        
        @param cascade_create: If the user does not exist in the database, returns a list of non-personalized search results and creates the user in the database. This allows for example rotations in the following recommendations for that user, as the user will be already known to the system.
        
        @param return_properties: With `returnProperties=true`, property values of the recommended items are returned along with their IDs in a JSON dictionary. The acquired property values can be used for easy displaying of the recommended items to the user. 
        
        
        Example response:
        
        ```
        
        E{lb}
        
        "recommId": "ce52ada4-e4d9-4885-943c-407db2dee837",
        
        "recomms": 
        
        [
        
        E{lb}
        
        "id": "tv-178",
        
        "values": E{lb}
        
        "description": "4K TV with 3D feature",
        
        "categories":   ["Electronics", "Televisions"],
        
        "price": 342,
        
        "url": "myshop.com/tv-178"
        E{rb}
        E{rb},
        
        E{lb}
        
        "id": "mixer-42",
        
        "values": E{lb}
        
        "description": "Stainless Steel Mixer",
        
        "categories":   ["Home & Kitchen"],
        
        "price": 39,
        
        "url": "myshop.com/mixer-42"
        E{rb}
        E{rb}
        
        ]
        E{rb}
        
        ```
        
        
        @param included_properties: Allows to specify, which properties should be returned when `returnProperties=true` is set. The properties are given as a comma-separated list. 
        
        
        Example response for `includedProperties=description,price`:
        
        ```
        
        E{lb}
        
        "recommId": "a86ee8d5-cd8e-46d1-886c-8b3771d0520b",
        
        "recomms":
        
        [
        
        E{lb}
        
        "id": "tv-178",
        
        "values": E{lb}
        
        "description": "4K TV with 3D feature",
        
        "price": 342
        E{rb}
        E{rb},
        
        E{lb}
        
        "id": "mixer-42",
        
        "values": E{lb}
        
        "description": "Stainless Steel Mixer",
        
        "price": 39
        E{rb}
        E{rb}
        
        ]
        E{rb}
        
        ```
        
        
        @param filter: Boolean-returning [ReQL](https://docs.recombee.com/reql.html) expression which allows you to filter recommended items based on the values of their attributes.
        
        
        Filters can be also assigned to a [scenario](https://docs.recombee.com/scenarios.html) in the [Admin UI](https://admin.recombee.com).
        
        
        @param booster: Number-returning [ReQL](https://docs.recombee.com/reql.html) expression which allows you to boost recommendation rate of some items based on the values of their attributes.
        
        
        Boosters can be also assigned to a [scenario](https://docs.recombee.com/scenarios.html) in the [Admin UI](https://admin.recombee.com).
        
        
        @param logic: Logic specifies particular behavior of the recommendation models. You can pick tailored logic for your domain and use case.
        
        See [this section](https://docs.recombee.com/recommendation_logics.html) for list of available logics and other details.
        
        
        The difference between `logic` and `scenario` is that `logic` specifies mainly behavior, while `scenario` specifies the place where recommendations are shown to the users.
        
        
        Logic can be also set to a [scenario](https://docs.recombee.com/scenarios.html) in the [Admin UI](https://admin.recombee.com).
        
        
        @param expert_settings: Dictionary of custom options.
        
        
        @param return_ab_group: If there is a custom AB-testing running, return name of group to which the request belongs.
        
        
        """
        self.user_id = user_id
        self.search_query = search_query
        self.count = count
        self.scenario = scenario
        self.cascade_create = cascade_create
        self.return_properties = return_properties
        self.included_properties = included_properties
        self.filter = filter
        self.booster = booster
        self.logic = logic
        self.expert_settings = expert_settings
        self.return_ab_group = return_ab_group
        self.timeout = 3000
        self.ensure_https = False
        self.method = 'post'
        self.path = "/search/users/%s/items/" % (self.user_id)

    def get_body_parameters(self):
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p['searchQuery'] = self.search_query
        p['count'] = self.count
        if self.scenario is not DEFAULT:
            p['scenario'] = self.scenario
        if self.cascade_create is not DEFAULT:
            p['cascadeCreate'] = self.cascade_create
        if self.return_properties is not DEFAULT:
            p['returnProperties'] = self.return_properties
        if self.included_properties is not DEFAULT:
            p['includedProperties'] = self.included_properties
        if self.filter is not DEFAULT:
            p['filter'] = self.filter
        if self.booster is not DEFAULT:
            p['booster'] = self.booster
        if self.logic is not DEFAULT:
            p['logic'] = self.logic
        if self.expert_settings is not DEFAULT:
            p['expertSettings'] = self.expert_settings
        if self.return_ab_group is not DEFAULT:
            p['returnAbGroup'] = self.return_ab_group
        return p

    def get_query_parameters(self):
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
