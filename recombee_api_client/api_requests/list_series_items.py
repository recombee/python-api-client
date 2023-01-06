from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class ListSeriesItems(Request):
    """
    Lists all the items present in the given series, sorted according to their time index values.
    Required parameters:
    
    :param series_id: ID of the series whose items are to be listed.
    

    """

    def __init__(self, series_id: str):
        super().__init__(path="/series/%s/items/" % (series_id), method='get', timeout=100000, ensure_https=False)
        self.series_id = series_id

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
        return params
