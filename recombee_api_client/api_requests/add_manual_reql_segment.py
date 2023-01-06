from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class AddManualReqlSegment(Request):
    """
    Adds a new Segment into a Manual ReQL Segmentation.
    
    The new Segment is defined by a [ReQL](https://docs.recombee.com/reql.html) filter that returns `true` for an item in case that this item belongs to the segment.
    
    Required parameters:
    
    :param segmentation_id: ID of the Segmentation to which the new Segment should be added
    
    :param segment_id: ID of the newly created Segment
    
    :param filter: ReQL filter that returns `true` for items that belong to this Segment. Otherwise returns `false`.
    
    
    
    Optional parameters:
    
    :param title: Human-readable name of the Segment that is shown in the Recombee Admin UI.
    
    

    """

    def __init__(self, segmentation_id: str, segment_id: str, filter: str, title: str = DEFAULT):
        super().__init__(path="/segmentations/manual-reql/%s/segments/%s" % (segmentation_id,segment_id), method='put', timeout=10000, ensure_https=False)
        self.segmentation_id = segmentation_id
        self.segment_id = segment_id
        self.filter = filter
        self.title = title

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p['filter'] = self.filter
        if self.title is not DEFAULT:
            p['title'] = self.title
        return p

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
