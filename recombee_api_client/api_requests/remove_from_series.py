from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class RemoveFromSeries(Request):
    """
    Removes an existing series item from the series.
    Required parameters:
    
    :param series_id: ID of the series from which a series item is to be removed.
    
    :param item_type: Type of the item to be removed.
    
    :param item_id: ID of the item iff `itemType` is `item`. ID of the series iff `itemType` is `series`.
    
    :param time: Time index of the item to be removed.
    

    """

    def __init__(self, series_id: str, item_type: str, item_id: str, time: float):
        super().__init__(path="/series/%s/items/" % (series_id), method='delete', timeout=1000, ensure_https=False)
        self.series_id = series_id
        self.item_type = item_type
        self.item_id = item_id
        self.time = time

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        return p

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        params['itemType'] = self.item_type
        params['itemId'] = self.item_id
        params['time'] = self.time
        return params
