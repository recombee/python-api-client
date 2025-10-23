from recombee_api_client.inputs.logic import Logic
from recombee_api_client.inputs.composite_recommendation_stage_parameters import (
    CompositeRecommendationStageParameters,
)
from recombee_api_client.api_requests.request import Request
from recombee_api_client.utils.serialize_to_json import serialize_to_json
from typing import Union, List
from datetime import datetime
import uuid

DEFAULT = uuid.uuid4()


class CompositeRecommendation(Request):
    """
    Composite Recommendation returns both a *source entity* (e.g., an Item or [Item Segment](https://docs.recombee.com/segmentations.html)) and a list of related recommendations in a single response.

    It is ideal for use cases such as personalized homepage sections (*Articles from <category>*), *Because You Watched <movie>*, or *Artists Related to Your Favorite Artist <artist>*.

    See detailed **examples and configuration guidance** in the [Composite Scenarios documentation](https://docs.recombee.com/scenarios#composite-recommendations).

    **Structure**

    The endpoint operates in two stages:
    1. Recommends the *source* (e.g., an Item Segment or item) to the user.
    2. Recommends *results* (items or Item Segments) related to that *source*.

    For example, *Articles from <category>* can be decomposed into:
      - [Recommend Item Segments To User](https://docs.recombee.com/api#recommend-item-segments-to-user) to find the category.
      - [Recommend Items To Item Segment](https://docs.recombee.com/api#recommend-items-to-item-segment) to recommend articles from that category.

    Since the first step uses [Recommend Item Segments To User](https://docs.recombee.com/api#recommend-items-to-user), you must include the `userId` parameter in the *Composite Recommendation* request.

    Each *Composite Recommendation* counts as a single recommendation API request for billing.

    **Stage-specific Parameters**

    Additional parameters can be supplied via [sourceSettings](https://docs.recombee.com/api#composite-recommendation-param-sourceSettings) and [resultSettings](https://docs.recombee.com/api#composite-recommendation-param-resultSettings).
    In the example above:
      - `sourceSettings` may include any parameter valid for [Recommend Item Segments To User](https://docs.recombee.com/api#recommend-items-to-user) (e.g., `filter`, `booster`).
      - `resultSettings` may include any parameter valid for [Recommend Items To Item Segment](https://docs.recombee.com/api#recommend-items-to-item-segment).

    See [this example](https://docs.recombee.com/api#composite-recommendation-example-setting-parameters-for-individual-stages) for more details.

    Required parameters:

    :param scenario: Scenario defines a particular application of recommendations. It can be, for example, "homepage", "cart", or "emailing".


    You can set various settings to the [scenario](https://docs.recombee.com/scenarios) in the [Admin UI](https://admin.recombee.com). You can also see the performance of each scenario in the Admin UI separately, so you can check how well each application performs.


    The AI that optimizes models to get the best results may optimize different scenarios separately or even use different models in each of the scenarios.


    :param count: Number of items to be recommended (N for the top-N recommendation).



    Optional parameters:

    :param item_id: ID of the item for which the recommendations are to be generated.


    :param user_id: ID of the user for which the recommendations are to be generated.


    :param logic: Logic specifies the particular behavior of the recommendation models. You can pick tailored logic for your domain and use case.

    See [this section](https://docs.recombee.com/recommendation_logics) for a list of available logics and other details.


    The difference between `logic` and `scenario` is that `logic` specifies mainly behavior, while `scenario` specifies the place where recommendations are shown to the users.


    Logic can also be set to a [scenario](https://docs.recombee.com/scenarios) in the [Admin UI](https://admin.recombee.com).


    :param segment_id: ID of the segment from `contextSegmentationId` for which the recommendations are to be generated.


    :param cascade_create: If the entity for the source recommendation does not exist in the database, returns a list of non-personalized recommendations and creates the user in the database. This allows, for example, rotations in the following recommendations for that entity, as the entity will be already known to the system.


    :param source_settings: Parameters applied for recommending the *Source* stage. The accepted parameters correspond with the recommendation sub-endpoint used to recommend the *Source*.


    :param result_settings: Parameters applied for recommending the *Result* stage. The accepted parameters correspond with the recommendation sub-endpoint used to recommend the *Result*.


    :param expert_settings: Dictionary of custom options.


    """

    def __init__(
        self,
        scenario: str,
        count: int,
        item_id: str = DEFAULT,
        user_id: str = DEFAULT,
        logic: Logic = DEFAULT,
        segment_id: str = DEFAULT,
        cascade_create: bool = DEFAULT,
        source_settings: CompositeRecommendationStageParameters = DEFAULT,
        result_settings: CompositeRecommendationStageParameters = DEFAULT,
        expert_settings: dict = DEFAULT,
    ):
        super().__init__(
            path="/recomms/composite/", method="post", timeout=3000, ensure_https=False
        )
        self.scenario = scenario
        self.count = count
        self.item_id = item_id
        self.user_id = user_id
        self.logic = logic
        self.segment_id = segment_id
        self.cascade_create = cascade_create
        self.source_settings = source_settings
        self.result_settings = result_settings
        self.expert_settings = expert_settings

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p["scenario"] = serialize_to_json(self.scenario)
        p["count"] = serialize_to_json(self.count)
        if self.item_id is not DEFAULT:
            p["itemId"] = serialize_to_json(self.item_id)
        if self.user_id is not DEFAULT:
            p["userId"] = serialize_to_json(self.user_id)
        if self.logic is not DEFAULT:
            p["logic"] = serialize_to_json(self.logic)
        if self.segment_id is not DEFAULT:
            p["segmentId"] = serialize_to_json(self.segment_id)
        if self.cascade_create is not DEFAULT:
            p["cascadeCreate"] = serialize_to_json(self.cascade_create)
        if self.source_settings is not DEFAULT:
            p["sourceSettings"] = serialize_to_json(self.source_settings)
        if self.result_settings is not DEFAULT:
            p["resultSettings"] = serialize_to_json(self.result_settings)
        if self.expert_settings is not DEFAULT:
            p["expertSettings"] = serialize_to_json(self.expert_settings)

        return p

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()

        return params
