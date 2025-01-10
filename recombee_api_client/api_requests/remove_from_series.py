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
    

    """

    def __init__(self, series_id: str, item_type: str, item_id: str):
        super().__init__(path="/series/%s/items/" % (series_id), method='delete', timeout=3000, ensure_https=False)
        self.series_id = series_id
        self.item_type = item_type
        self.item_id = item_id

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p['itemType'] = self.item_type
        p['itemId'] = self.item_id
        return p

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
