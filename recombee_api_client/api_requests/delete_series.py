from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class DeleteSeries(Request):
    """
    Deletes the series of the given `seriesId` from the database.
    
    Deleting a series will only delete assignment of items to it, not the items themselves!
    
    Required parameters:
    
    :param series_id: ID of the series to be deleted.
    
    
    Optional parameters:
    
    :param cascade_delete: If set to `true`, item with the same ID as seriesId will be also deleted. Default is `false`.
    

    """

    def __init__(self, series_id: str, cascade_delete: bool = DEFAULT):
        super().__init__(path="/series/%s" % (series_id), method='delete', timeout=3000, ensure_https=False)
        self.series_id = series_id
        self.cascade_delete = cascade_delete

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        if self.cascade_delete is not DEFAULT:
            p['cascadeDelete'] = self.cascade_delete
        return p

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
