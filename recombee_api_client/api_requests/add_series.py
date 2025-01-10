from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class AddSeries(Request):
    """
    Creates a new series in the database.
    Required parameters:
    
    :param series_id: ID of the series to be created.
    
    
    Optional parameters:
    
    :param cascade_create: If set to `true`, the item will be created with the same ID as the series. Default is `true`.
    

    """

    def __init__(self, series_id: str, cascade_create: bool = DEFAULT):
        super().__init__(path="/series/%s" % (series_id), method='put', timeout=3000, ensure_https=False)
        self.series_id = series_id
        self.cascade_create = cascade_create

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        if self.cascade_create is not DEFAULT:
            p['cascadeCreate'] = self.cascade_create
        return p

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
