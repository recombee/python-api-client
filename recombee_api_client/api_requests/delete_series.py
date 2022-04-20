from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class DeleteSeries(Request):
    """
    Deletes the series of given `seriesId` from the database.
    
    Deleting a series will only delete assignment of items to it, not the items themselves!
    
    Required parameters:
    
    :param series_id: ID of the series to be deleted.
    

    """

    def __init__(self, series_id: str):
        super().__init__(path="/series/%s" % (series_id), method='delete', timeout=1000, ensure_https=False)
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
