from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class GetUserPropertyInfo(Request):
    """
    Gets information about specified user property.
    
    Required parameters:
    
    :param property_name: Name of the property about which the information is to be retrieved.
    

    """

    def __init__(self, property_name: str):
        super().__init__(path="/users/properties/%s" % (property_name), method='get', timeout=100000, ensure_https=False)
        self.property_name = property_name

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
