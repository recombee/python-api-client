from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class AddRating(Request):
    """
    Adds a rating of the given item made by the given user.
    
    Required parameters:
    
    :param user_id: User who submitted the rating
    
    :param item_id: Rated item
    
    :param rating: Rating rescaled to interval [-1.0,1.0], where -1.0 means the worst rating possible, 0.0 means neutral, and 1.0 means absolutely positive rating. For example, in the case of 5-star evaluations, rating = (numStars-3)/2 formula may be used for the conversion.
    
    
    Optional parameters:
    
    :param timestamp: UTC timestamp of the rating as ISO8601-1 pattern or UTC epoch time. The default value is the current time.
    
    :param cascade_create: Sets whether the given user/item should be created if not present in the database.
    
    :param recomm_id: If this rating is based on a recommendation request, `recommId` is the id of the clicked recommendation.
    
    :param additional_data: A dictionary of additional data for the interaction.
    

    """

    def __init__(self, user_id: str, item_id: str, rating: float, timestamp: Union[str, int] = DEFAULT, cascade_create: bool = DEFAULT, recomm_id: str = DEFAULT, additional_data: dict = DEFAULT):
        super().__init__(path="/ratings/", method='post', timeout=1000, ensure_https=False)
        self.user_id = user_id
        self.item_id = item_id
        self.rating = rating
        self.timestamp = timestamp
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
        p['rating'] = self.rating
        if self.timestamp is not DEFAULT:
            p['timestamp'] = self.timestamp
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
