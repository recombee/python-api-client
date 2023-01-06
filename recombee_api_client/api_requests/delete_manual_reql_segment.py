from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class DeleteManualReqlSegment(Request):
    """
    Delete a Segment from a Manual ReQL Segmentation.
    
    Required parameters:
    
    :param segmentation_id: ID of the Segmentation from which the Segment should be deleted
    
    :param segment_id: ID of the Segment that should be deleted
    

    """

    def __init__(self, segmentation_id: str, segment_id: str):
        super().__init__(path="/segmentations/manual-reql/%s/segments/%s" % (segmentation_id,segment_id), method='delete', timeout=10000, ensure_https=False)
        self.segmentation_id = segmentation_id
        self.segment_id = segment_id

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
