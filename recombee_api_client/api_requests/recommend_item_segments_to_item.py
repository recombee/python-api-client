from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class RecommendItemSegmentsToItem(Request):
    """
    Recommends Segments from a [Segmentation](https://docs.recombee.com/segmentations.html) that are the most relevant to a particular item.
    
    Based on the used Segmentation, this endpoint can be used for example for:
    
      - Recommending the related categories
      - Recommending the related genres
      - Recommending the related brands
      - Recommending the related artists
    
    You need to set the used Segmentation the Admin UI in the [Scenario settings](https://docs.recombee.com/scenarios) prior to using this endpoint.
    
    The returned segments are sorted by relevance (first segment being the most relevant).
    
    It is also possible to use POST HTTP method (for example in case of very long ReQL filter) - query parameters then become body parameters.
    
    Required parameters:
    
    :param item_id: ID of the item for which the recommendations are to be generated.
    
    :param target_user_id: ID of the user who will see the recommendations.
    
    
    Specifying the *targetUserId* is beneficial because:
    
    
    * It makes the recommendations personalized
    
    * Allows the calculation of Actions and Conversions
    
    in the graphical user interface,
    
    as Recombee can pair the user who got recommendations
    
    and who afterward viewed/purchased an item.
    
    
    If you insist on not specifying the user, pass `null`
    
    (`None`, `nil`, `NULL` etc., depending on the language) to *targetUserId*.
    
    Do not create some special dummy user for getting recommendations,
    
    as it could mislead the recommendation models,
    
    and result in wrong recommendations.
    
    
    For anonymous/unregistered users, it is possible to use, for example, their session ID.
    
    
    :param count: Number of item segments to be recommended (N for the top-N recommendation).
    
    
    
    Optional parameters:
    
    :param scenario: Scenario defines a particular application of recommendations. It can be, for example, "homepage", "cart", or "emailing".
    
    
    You can set various settings to the [scenario](https://docs.recombee.com/scenarios.html) in the [Admin UI](https://admin.recombee.com). You can also see the performance of each scenario in the Admin UI separately, so you can check how well each application performs.
    
    
    The AI that optimizes models to get the best results may optimize different scenarios separately or even use different models in each of the scenarios.
    
    
    :param cascade_create: If the user does not exist in the database, returns a list of non-personalized recommendations and creates the user in the database. This allows, for example, rotations in the following recommendations for that user, as the user will be already known to the system.
    
    
    :param filter: Boolean-returning [ReQL](https://docs.recombee.com/reql.html) expression which allows you to filter recommended segments based on the `segmentationId`.
    
    
    :param booster: Number-returning [ReQL](https://docs.recombee.com/reql.html) expression which allows you to boost recommendation rate of some segments based on the `segmentationId`.
    
    
    :param logic: Logic specifies the particular behavior of the recommendation models. You can pick tailored logic for your domain and use case.
    
    See [this section](https://docs.recombee.com/recommendation_logics.html) for a list of available logics and other details.
    
    
    The difference between `logic` and `scenario` is that `logic` specifies mainly behavior, while `scenario` specifies the place where recommendations are shown to the users.
    
    
    Logic can also be set to a [scenario](https://docs.recombee.com/scenarios.html) in the [Admin UI](https://admin.recombee.com).
    
    
    :param expert_settings: Dictionary of custom options.
    
    
    :param return_ab_group: If there is a custom AB-testing running, return the name of the group to which the request belongs.
    
    

    """

    def __init__(self, item_id: str, target_user_id: str, count: int, scenario: str = DEFAULT, cascade_create: bool = DEFAULT, filter: str = DEFAULT, booster: str = DEFAULT, logic: Union[str, dict] = DEFAULT, expert_settings: dict = DEFAULT, return_ab_group: bool = DEFAULT):
        super().__init__(path="/recomms/items/%s/item-segments/" % (item_id), method='post', timeout=3000, ensure_https=False)
        self.item_id = item_id
        self.target_user_id = target_user_id
        self.count = count
        self.scenario = scenario
        self.cascade_create = cascade_create
        self.filter = filter
        self.booster = booster
        self.logic = logic
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

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
