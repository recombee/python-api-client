from recombee_api_client.inputs.logic import Logic
from recombee_api_client.api_requests.request import Request
from recombee_api_client.utils.serialize_to_json import serialize_to_json
from typing import Union, List
from datetime import datetime
import uuid

DEFAULT = uuid.uuid4()


class RecommendUsersToItem(Request):
    """
    Recommends users that are likely to be interested in the given item.

    It is also possible to use POST HTTP method (for example in the case of a very long ReQL filter) - query parameters then become body parameters.

    The returned users are sorted by predicted interest in the item (the first user being the most interested).

    Required parameters:

    :param item_id: ID of the item for which the recommendations are to be generated.

    :param count: Number of users to be recommended (N for the top-N recommendation).


    Optional parameters:

    :param scenario: Scenario defines a particular application of recommendations. It can be, for example, "homepage", "cart", or "emailing".


    You can set various settings to the [scenario](https://docs.recombee.com/scenarios) in the [Admin UI](https://admin.recombee.com). You can also see the performance of each scenario in the Admin UI separately, so you can check how well each application performs.


    The AI that optimizes models to get the best results may optimize different scenarios separately or even use different models in each of the scenarios.


    :param cascade_create: If an item of the given *itemId* doesn't exist in the database, it creates the missing item.

    :param return_properties: With `returnProperties=true`, property values of the recommended users are returned along with their IDs in a JSON dictionary. The acquired property values can be used to easily display the recommended users.


    Example response:

    ```json

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

    ```json

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


    :param filter: Boolean-returning [ReQL](https://docs.recombee.com/reql) expression, which allows you to filter recommended users based on the values of their attributes.


    Filters can also be assigned to a [scenario](https://docs.recombee.com/scenarios) in the [Admin UI](https://admin.recombee.com).


    :param booster: Number-returning [ReQL](https://docs.recombee.com/reql) expression, which allows you to boost the recommendation rate of some users based on the values of their attributes.


    Boosters can also be assigned to a [scenario](https://docs.recombee.com/scenarios) in the [Admin UI](https://admin.recombee.com).


    :param logic: Logic specifies the particular behavior of the recommendation models. You can pick tailored logic for your domain and use case.

    See [this section](https://docs.recombee.com/recommendation_logics) for a list of available logics and other details.


    The difference between `logic` and `scenario` is that `logic` specifies mainly behavior, while `scenario` specifies the place where recommendations are shown to the users.


    Logic can also be set to a [scenario](https://docs.recombee.com/scenarios) in the [Admin UI](https://admin.recombee.com).


    :param reql_expressions: A dictionary of [ReQL](https://docs.recombee.com/reql) expressions that will be executed for each recommended user.

    This can be used to compute additional properties of the recommended users that are not stored in the database.


    The keys are the names of the expressions, and the values are the actual ReQL expressions.


    Example request:

    ```json

    E{lb}

    "reqlExpressions": E{lb}

    "isInUsersCity": "context_user[\"city\"] in 'cities'",

    "distanceToUser": "earth_distance('location', context_user[\"location\"])",

    "isFromSameCompany": "'company' == context_item[\"company\"]"
    E{rb}
    E{rb}

    ```


    Example response:

    ```json

    E{lb}

    "recommId": "ce52ada4-e4d9-4885-943c-407db2dee837",

    "recomms":

    [

    E{lb}

    "id": "restaurant-178",

    "reqlEvaluations": E{lb}

    "isInUsersCity": true,

    "distanceToUser": 5200.2,

    "isFromSameCompany": false
    E{rb}
    E{rb},

    E{lb}

    "id": "bar-42",

    "reqlEvaluations": E{lb}

    "isInUsersCity": false,

    "distanceToUser": 2516.0,

    "isFromSameCompany": true
    E{rb}
    E{rb}

    ],

    "numberNextRecommsCalls": 0
    E{rb}

    ```


    :param diversity: **Expert option:** Real number from [0.0, 1.0], which determines how mutually dissimilar the recommended users should be. The default value is 0.0, i.e., no diversification. Value 1.0 means maximal diversification.


    :param expert_settings: Dictionary of custom options.


    :param return_ab_group: If there is a custom AB-testing running, return the name of the group to which the request belongs.


    """

    def __init__(
        self,
        item_id: str,
        count: int,
        scenario: str = DEFAULT,
        cascade_create: bool = DEFAULT,
        return_properties: bool = DEFAULT,
        included_properties: list = DEFAULT,
        filter: str = DEFAULT,
        booster: str = DEFAULT,
        logic: Logic = DEFAULT,
        reql_expressions: dict = DEFAULT,
        diversity: float = DEFAULT,
        expert_settings: dict = DEFAULT,
        return_ab_group: bool = DEFAULT,
    ):
        super().__init__(
            path="/recomms/items/%s/users/" % (item_id),
            method="post",
            timeout=50000,
            ensure_https=False,
        )
        self.item_id = item_id
        self.count = count
        self.scenario = scenario
        self.cascade_create = cascade_create
        self.return_properties = return_properties
        self.included_properties = included_properties
        self.filter = filter
        self.booster = booster
        self.logic = logic
        self.reql_expressions = reql_expressions
        self.diversity = diversity
        self.expert_settings = expert_settings
        self.return_ab_group = return_ab_group

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p["count"] = serialize_to_json(self.count)
        if self.scenario is not DEFAULT:
            p["scenario"] = serialize_to_json(self.scenario)
        if self.cascade_create is not DEFAULT:
            p["cascadeCreate"] = serialize_to_json(self.cascade_create)
        if self.return_properties is not DEFAULT:
            p["returnProperties"] = serialize_to_json(self.return_properties)
        if self.included_properties is not DEFAULT:
            p["includedProperties"] = serialize_to_json(self.included_properties)
        if self.filter is not DEFAULT:
            p["filter"] = serialize_to_json(self.filter)
        if self.booster is not DEFAULT:
            p["booster"] = serialize_to_json(self.booster)
        if self.logic is not DEFAULT:
            p["logic"] = serialize_to_json(self.logic)
        if self.reql_expressions is not DEFAULT:
            p["reqlExpressions"] = serialize_to_json(self.reql_expressions)
        if self.diversity is not DEFAULT:
            p["diversity"] = serialize_to_json(self.diversity)
        if self.expert_settings is not DEFAULT:
            p["expertSettings"] = serialize_to_json(self.expert_settings)
        if self.return_ab_group is not DEFAULT:
            p["returnAbGroup"] = serialize_to_json(self.return_ab_group)

        return p

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()

        return params
