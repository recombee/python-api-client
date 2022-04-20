from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class RecommendItemsToItem(Request):
    """
    Recommends set of items that are somehow related to one given item, *X*. Typical scenario  is when user *A* is viewing *X*. Then you may display items to the user that he might be also interested in. Recommend items to item request gives you Top-N such items, optionally taking the target user *A* into account.
    
    The returned items are sorted by relevance (first item being the most relevant).
    
    Besides the recommended items, also a unique `recommId` is returned in the response. It can be used to:
    
    - Let Recombee know that this recommendation was successful (e.g. user clicked one of the recommended items). See [Reported metrics](https://docs.recombee.com/admin_ui.html#reported-metrics).
    - Get subsequent recommended items when the user scrolls down (*infinite scroll*) or goes to the next page. See [Recommend Next Items](https://docs.recombee.com/api.html#recommend-next-items).
    
    It is also possible to use POST HTTP method (for example in case of very long ReQL filter) - query parameters then become body parameters.
    
    Required parameters:
    
    :param item_id: ID of the item for which the recommendations are to be generated.
    
    :param target_user_id: ID of the user who will see the recommendations.
    
    
    Specifying the *targetUserId* is beneficial because:
    
    
    * It makes the recommendations personalized
    
    * Allows the calculation of Actions and Conversions
    
    in the graphical user interface,
    
    as Recombee can pair the user who got recommendations
    
    and who afterwards viewed/purchased an item.
    
    
    If you insist on not specifying the user, pass `null`
    
    (`None`, `nil`, `NULL` etc. depending on language) to *targetUserId*.
    
    Do not create some special dummy user for getting recommendations,
    
    as it could mislead the recommendation models,
    
    and result in wrong recommendations.
    
    
    For anonymous/unregistered users it is possible to use for example their session ID.
    
    
    :param count: Number of items to be recommended (N for the top-N recommendation).
    
    
    Optional parameters:
    
    :param scenario: Scenario defines a particular application of recommendations. It can be for example "homepage", "cart" or "emailing".
    
    
    You can set various settings to the [scenario](https://docs.recombee.com/scenarios.html) in the [Admin UI](https://admin.recombee.com). You can also see performance of each scenario in the Admin UI separately, so you can check how well each application performs.
    
    
    The AI which optimizes models in order to get the best results may optimize different scenarios separately, or even use different models in each of the scenarios.
    
    
    :param cascade_create: If item of given *itemId* or user of given *targetUserId* doesn't exist in the database, it creates the missing entity/entities and returns some (non-personalized) recommendations. This allows for example rotations in the following recommendations for the user of given *targetUserId*, as the user will be already known to the system.
    
    :param return_properties: With `returnProperties=true`, property values of the recommended items are returned along with their IDs in a JSON dictionary. The acquired property values can be used for easy displaying of the recommended items to the user. 
    
    
    Example response:
    
    ```
    
    E{lb}
    
    "recommId": "0c6189e7-dc1a-429a-b613-192696309361",
    
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
    
    
    :param included_properties: Allows to specify, which properties should be returned when `returnProperties=true` is set. The properties are given as a comma-separated list. 
    
    
    Example response for `includedProperties=description,price`:
    
    ```
    
    E{lb}
    
    "recommId": "6842c725-a79f-4537-a02c-f34d668a3f80",
    
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
    
    
    :param filter: Boolean-returning [ReQL](https://docs.recombee.com/reql.html) expression which allows you to filter recommended items based on the values of their attributes.
    
    
    Filters can be also assigned to a [scenario](https://docs.recombee.com/scenarios.html) in the [Admin UI](https://admin.recombee.com).
    
    
    :param booster: Number-returning [ReQL](https://docs.recombee.com/reql.html) expression which allows you to boost recommendation rate of some items based on the values of their attributes.
    
    
    Boosters can be also assigned to a [scenario](https://docs.recombee.com/scenarios.html) in the [Admin UI](https://admin.recombee.com).
    
    
    :param logic: Logic specifies particular behavior of the recommendation models. You can pick tailored logic for your domain and use case.
    
    See [this section](https://docs.recombee.com/recommendation_logics.html) for list of available logics and other details.
    
    
    The difference between `logic` and `scenario` is that `logic` specifies mainly behavior, while `scenario` specifies the place where recommendations are shown to the users.
    
    
    Logic can be also set to a [scenario](https://docs.recombee.com/scenarios.html) in the [Admin UI](https://admin.recombee.com).
    
    
    :param user_impact: **Expert option** If *targetUserId* parameter is present, the recommendations are biased towards the given user. Using *userImpact*, you may control this bias. For an extreme case of `userImpact=0.0`, the interactions made by the user are not taken into account at all (with the exception of history-based blacklisting), for `userImpact=1.0`, you'll get user-based recommendation. The default value is `0`.
    
    
    :param diversity: **Expert option** Real number from [0.0, 1.0] which determines how much mutually dissimilar should the recommended items be. The default value is 0.0, i.e., no diversification. Value 1.0 means maximal diversification.
    
    
    :param min_relevance: **Expert option** If the *targetUserId* is provided:  Specifies the threshold of how much relevant must the recommended items be to the user. Possible values one of: "low", "medium", "high". The default value is "low", meaning that the system attempts to recommend number of items equal to *count* at any cost. If there are not enough data (such as interactions or item properties), this may even lead to bestseller-based recommendations to be appended to reach the full *count*. This behavior may be suppressed by using "medium" or "high" values. In such case, the system only recommends items of at least the requested relevance, and may return less than *count* items when there is not enough data to fulfill it.
    
    
    :param rotation_rate: **Expert option** If the *targetUserId* is provided: If your users browse the system in real-time, it may easily happen that you wish to offer them recommendations multiple times. Here comes the question: how much should the recommendations change? Should they remain the same, or should they rotate? Recombee API allows you to control this per-request in backward fashion. You may penalize an item for being recommended in the near past. For the specific user, `rotationRate=1` means maximal rotation, `rotationRate=0` means absolutely no rotation. You may also use, for example `rotationRate=0.2` for only slight rotation of recommended items.
    
    
    :param rotation_time: **Expert option** If the *targetUserId* is provided: Taking *rotationRate* into account, specifies how long time it takes to an item to recover from the penalization. For example, `rotationTime=7200.0` means that items recommended less than 2 hours ago are penalized.
    
    
    :param expert_settings: Dictionary of custom options.
    
    
    :param return_ab_group: If there is a custom AB-testing running, return name of group to which the request belongs.
    
    

    """

    def __init__(self, item_id: str, target_user_id: str, count: int, scenario: str = DEFAULT, cascade_create: bool = DEFAULT, return_properties: bool = DEFAULT, included_properties: list = DEFAULT, filter: str = DEFAULT, booster: str = DEFAULT, logic: Union[str, dict] = DEFAULT, user_impact: float = DEFAULT, diversity: float = DEFAULT, min_relevance: str = DEFAULT, rotation_rate: float = DEFAULT, rotation_time: float = DEFAULT, expert_settings: dict = DEFAULT, return_ab_group: bool = DEFAULT):
        super().__init__(path="/recomms/items/%s/items/" % (item_id), method='post', timeout=3000, ensure_https=False)
        self.item_id = item_id
        self.target_user_id = target_user_id
        self.count = count
        self.scenario = scenario
        self.cascade_create = cascade_create
        self.return_properties = return_properties
        self.included_properties = included_properties
        self.filter = filter
        self.booster = booster
        self.logic = logic
        self.user_impact = user_impact
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
        p['targetUserId'] = self.target_user_id
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
        if self.user_impact is not DEFAULT:
            p['userImpact'] = self.user_impact
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
