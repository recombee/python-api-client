from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class RecommendUsersToItem(Request):
    """
    Recommends users that are likely to be interested in the given item.
    
    It is also possible to use POST HTTP method (for example in the case of a very long ReQL filter) - query parameters then become body parameters.
    
    The returned users are sorted by predicted interest in the item (the first user being the most interested).
    
    Required parameters:
    
    :param item_id: ID of the item for which the recommendations are to be generated.
    
    :param count: Number of items to be recommended (N for the top-N recommendation).
    
    
    Optional parameters:
    
    :param scenario: Scenario defines a particular application of recommendations. It can be, for example, "homepage", "cart", or "emailing".
    
    
    You can set various settings to the [scenario](https://docs.recombee.com/scenarios.html) in the [Admin UI](https://admin.recombee.com). You can also see the performance of each scenario in the Admin UI separately, so you can check how well each application performs.
    
    
    The AI that optimizes models to get the best results may optimize different scenarios separately or even use different models in each of the scenarios.
    
    
    :param cascade_create: If an item of the given *itemId* doesn't exist in the database, it creates the missing item.
    
    :param return_properties: With `returnProperties=true`, property values of the recommended users are returned along with their IDs in a JSON dictionary. The acquired property values can be used to easily display the recommended users. 
    
    
    Example response:
    
    ```
    
    E{lb}
    
    "recommId": "039b71dc-b9cc-4645-a84f-62b841eecfce",
    
    "recomms":
    
    [
    
    E{lb}
    
    "id": "user-17",
    
    "values": E{lb}
    
    "country": "US",
    
    "sex": "F"
    E{rb}
    E{rb},
    
    E{lb}
    
    "id": "user-2",
    
    "values": E{lb}
    
    "country": "CAN",
    
    "sex": "M"
    E{rb}
    E{rb}
    
    ],
    
    "numberNextRecommsCalls": 0
    E{rb}
    
    ```
    
    
    :param included_properties: Allows specifying which properties should be returned when `returnProperties=true` is set. The properties are given as a comma-separated list.
    
    
    Example response for `includedProperties=country`:
    
    ```
    
    E{lb}
    
    "recommId": "b2b355dd-972a-4728-9c6b-2dc229db0678",
    
    "recomms":
    
    [
    
    E{lb}
    
    "id": "user-17",
    
    "values": E{lb}
    
    "country": "US"
    E{rb}
    E{rb},
    
    E{lb}
    
    "id": "user-2",
    
    "values": E{lb}
    
    "country": "CAN"
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
    
    
    :param expert_settings: Dictionary of custom options.
    
    
    :param return_ab_group: If there is a custom AB-testing running, return the name of the group to which the request belongs.
    
    

    """

    def __init__(self, item_id: str, count: int, scenario: str = DEFAULT, cascade_create: bool = DEFAULT, return_properties: bool = DEFAULT, included_properties: list = DEFAULT, filter: str = DEFAULT, booster: str = DEFAULT, logic: Union[str, dict] = DEFAULT, diversity: float = DEFAULT, expert_settings: dict = DEFAULT, return_ab_group: bool = DEFAULT):
        super().__init__(path="/recomms/items/%s/users/" % (item_id), method='post', timeout=50000, ensure_https=False)
        self.item_id = item_id
        self.count = count
        self.scenario = scenario
        self.cascade_create = cascade_create
        self.return_properties = return_properties
        self.included_properties = included_properties
        self.filter = filter
        self.booster = booster
        self.logic = logic
        self.diversity = diversity
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
