from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class GetSegmentation(Request):
    """
    Get existing Segmentation.
    
    Required parameters:
    
    :param segmentation_id: ID of the Segmentation that should be returned
    

    """

    def __init__(self, segmentation_id: str):
        super().__init__(path="/segmentations/list/%s" % (segmentation_id), method='get', timeout=10000, ensure_https=False)
        self.segmentation_id = segmentation_id

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
