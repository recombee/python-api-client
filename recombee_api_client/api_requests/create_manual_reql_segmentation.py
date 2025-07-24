from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class CreateManualReqlSegmentation(Request):
    """
    Segment the items using multiple [ReQL](https://docs.recombee.com/reql) filters.
    
    Use the Add Manual ReQL Items Segment endpoint to create the individual segments.
    
    Required parameters:
    
    :param segmentation_id: ID of the newly created Segmentation
    
    :param source_type: What type of data should be segmented. Currently only `items` are supported.
    
    
    
    Optional parameters:
    
    :param title: Human-readable name that is shown in the Recombee Admin UI.
    
    
    :param description: Description that is shown in the Recombee Admin UI.
    
    

    """

    def __init__(self, segmentation_id: str, source_type: str, title: str = DEFAULT, description: str = DEFAULT):
        super().__init__(path="/segmentations/manual-reql/%s" % (segmentation_id), method='put', timeout=10000, ensure_https=False)
        self.segmentation_id = segmentation_id
        self.source_type = source_type
        self.title = title
        self.description = description

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p['sourceType'] = self.source_type
        if self.title is not DEFAULT:
            p['title'] = self.title
        if self.description is not DEFAULT:
            p['description'] = self.description
        return p

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
