from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class AddDetailView(Request):
    """
    Adds a detail view of the given item made by the given user.
    
    Required parameters:
    
    :param user_id: User who viewed the item
    
    :param item_id: Viewed item
    
    
    Optional parameters:
    
    :param timestamp: UTC timestamp of the view as ISO8601-1 pattern or UTC epoch time. The default value is the current time.
    
    :param duration: Duration of the view
    
    :param cascade_create: Sets whether the given user/item should be created if not present in the database.
    
    :param recomm_id: If this detail view is based on a recommendation request, `recommId` is the id of the clicked recommendation.
    
    :param additional_data: A dictionary of additional data for the interaction.
    

    """

    def __init__(self, user_id: str, item_id: str, timestamp: Union[str, int] = DEFAULT, duration: int = DEFAULT, cascade_create: bool = DEFAULT, recomm_id: str = DEFAULT, additional_data: dict = DEFAULT):
        super().__init__(path="/detailviews/", method='post', timeout=1000, ensure_https=False)
        self.user_id = user_id
        self.item_id = item_id
        self.timestamp = timestamp
        self.duration = duration
        self.cascade_create = cascade_create
        self.recomm_id = recomm_id
        self.additional_data = additional_data

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p['userId'] = self.user_id
        p['itemId'] = self.item_id
        if self.timestamp is not DEFAULT:
            p['timestamp'] = self.timestamp
        if self.duration is not DEFAULT:
            p['duration'] = self.duration
        if self.cascade_create is not DEFAULT:
            p['cascadeCreate'] = self.cascade_create
        if self.recomm_id is not DEFAULT:
            p['recommId'] = self.recomm_id
        if self.additional_data is not DEFAULT:
            p['additionalData'] = self.additional_data
        return p

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
