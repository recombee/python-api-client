from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class RecommendItemsToUser(Request):
    """
    Based on the user's past interactions (purchases, ratings, etc.) with the items, recommends top-N items that are most likely to be of high value for the given user.
    
    The most typical use cases are recommendations on the homepage, in some "Picked just for you" section, or in email.
    
    The returned items are sorted by relevance (the first item being the most relevant).
    
    Besides the recommended items, also a unique `recommId` is returned in the response. It can be used to:
    
    - Let Recombee know that this recommendation was successful (e.g., user clicked one of the recommended items). See [Reported metrics](https://docs.recombee.com/admin_ui.html#reported-metrics).
    - Get subsequent recommended items when the user scrolls down (*infinite scroll*) or goes to the next page. See [Recommend Next Items](https://docs.recombee.com/api.html#recommend-next-items).
    
    It is also possible to use POST HTTP method (for example in the case of a very long ReQL filter) - query parameters then become body parameters.
    
    Required parameters:
    
    :param user_id: ID of the user for whom personalized recommendations are to be generated.
    
    :param count: Number of items to be recommended (N for the top-N recommendation).
    
    
    
    Optional parameters:
    
    :param scenario: Scenario defines a particular application of recommendations. It can be, for example, "homepage", "cart", or "emailing".
    
    
    You can set various settings to the [scenario](https://docs.recombee.com/scenarios.html) in the [Admin UI](https://admin.recombee.com). You can also see the performance of each scenario in the Admin UI separately, so you can check how well each application performs.
    
    
    The AI that optimizes models to get the best results may optimize different scenarios separately or even use different models in each of the scenarios.
    
    
    :param cascade_create: If the user does not exist in the database, returns a list of non-personalized recommendations and creates the user in the database. This allows, for example, rotations in the following recommendations for that user, as the user will be already known to the system.
    
    
    :param return_properties: With `returnProperties=true`, property values of the recommended items are returned along with their IDs in a JSON dictionary. The acquired property values can be used to easily display the recommended items to the user. 
    
    
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
    
    ],
    
    "numberNextRecommsCalls": 0
    E{rb}
    
    ```
    
    
    :param included_properties: Allows specifying which properties should be returned when `returnProperties=true` is set. The properties are given as a comma-separated list.
    
    
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
    
    ],
    
    "numberNextRecommsCalls": 0
    E{rb}
    
    ```
    
    
    :param filter: Boolean-returning [ReQL](https://docs.recombee.com/reql.html) expression, which allows you to filter recommended items based on the values of their attributes.
    
    
    Filters can also be assigned to a [scenario](https://docs.recombee.com/scenarios.html) in the [Admin UI](https://admin.recombee.com).
    
    
    :param booster: Number-returning [ReQL](https://docs.recombee.com/reql.html) expression, which allows you to boost the recommendation rate of some items based on the values of their attributes.
    
    
    Boosters can also be assigned to a [scenario](https://docs.recombee.com/scenarios.html) in the [Admin UI](https://admin.recombee.com).
    
    
    :param logic: Logic specifies the particular behavior of the recommendation models. You can pick tailored logic for your domain and use case.
    
    See [this section](https://docs.recombee.com/recommendation_logics.html) for a list of available logics and other details.
    
    
    The difference between `logic` and `scenario` is that `logic` specifies mainly behavior, while `scenario` specifies the place where recommendations are shown to the users.
    
    
    Logic can also be set to a [scenario](https://docs.recombee.com/scenarios.html) in the [Admin UI](https://admin.recombee.com).
    
    
    :param diversity: **Expert option** Real number from [0.0, 1.0], which determines how mutually dissimilar the recommended items should be. The default value is 0.0, i.e., no diversification. Value 1.0 means maximal diversification.
    
    
    :param min_relevance: **Expert option** Specifies the threshold of how relevant must the recommended items be to the user. Possible values one of: "low", "medium", "high". The default value is "low", meaning that the system attempts to recommend a number of items equal to *count* at any cost. If there is not enough data (such as interactions or item properties), this may even lead to bestseller-based recommendations to be appended to reach the full *count*. This behavior may be suppressed by using "medium" or "high" values. In such a case, the system only recommends items of at least the requested relevance and may return less than *count* items when there is not enough data to fulfill it.
    
    
    :param rotation_rate: **Expert option** If your users browse the system in real-time, it may easily happen that you wish to offer them recommendations multiple times. Here comes the question: how much should the recommendations change? Should they remain the same, or should they rotate? Recombee API allows you to control this per request in a backward fashion. You may penalize an item for being recommended in the near past. For the specific user, `rotationRate=1` means maximal rotation, `rotationRate=0` means absolutely no rotation. You may also use, for example, `rotationRate=0.2` for only slight rotation of recommended items. Default: `0`.
    
    
    :param rotation_time: **Expert option** Taking *rotationRate* into account, specifies how long it takes for an item to recover from the penalization. For example, `rotationTime=7200.0` means that items recommended less than 2 hours ago are penalized. Default: `7200.0`.
    
    
    :param expert_settings: Dictionary of custom options.
    
    
    :param return_ab_group: If there is a custom AB-testing running, return the name of the group to which the request belongs.
    
    

    """

    def __init__(self, user_id: str, count: int, scenario: str = DEFAULT, cascade_create: bool = DEFAULT, return_properties: bool = DEFAULT, included_properties: list = DEFAULT, filter: str = DEFAULT, booster: str = DEFAULT, logic: Union[str, dict] = DEFAULT, diversity: float = DEFAULT, min_relevance: str = DEFAULT, rotation_rate: float = DEFAULT, rotation_time: float = DEFAULT, expert_settings: dict = DEFAULT, return_ab_group: bool = DEFAULT):
        super().__init__(path="/recomms/users/%s/items/" % (user_id), method='post', timeout=3000, ensure_https=False)
        self.user_id = user_id
        self.count = count
        self.scenario = scenario
        self.cascade_create = cascade_create
        self.return_properties = return_properties
        self.included_properties = included_properties
        self.filter = filter
        self.booster = booster
        self.logic = logic
        self.diversity = diversity
        self.min_relevance = min_relevance
        self.rotation_rate = rotation_rate
        self.rotation_time = rotation_time
        self.expert_settings = expert_settings
        self.return_ab_group = return_ab_group

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
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
        if self.return_ab_group is not DEFAULT:
            p['returnAbGroup'] = self.return_ab_group
        return p

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
