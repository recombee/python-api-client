from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class UpdatePropertyBasedSegmentation(Request):
    """
    Updates a Property Based Segmentation
    
    Required parameters:
    
    :param segmentation_id: ID of the updated Segmentation
    
    
    Optional parameters:
    
    :param property_name: Name of the property on which the Segmentation should be based
    
    
    :param title: Human-readable name that is shown in the Recombee Admin UI.
    
    
    :param description: Description that is shown in the Recombee Admin UI.
    
    

    """

    def __init__(self, segmentation_id: str, property_name: str = DEFAULT, title: str = DEFAULT, description: str = DEFAULT):
        super().__init__(path="/segmentations/property-based/%s" % (segmentation_id), method='post', timeout=10000, ensure_https=False)
        self.segmentation_id = segmentation_id
        self.property_name = property_name
        self.title = title
        self.description = description

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        if self.property_name is not DEFAULT:
            p['propertyName'] = self.property_name
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
