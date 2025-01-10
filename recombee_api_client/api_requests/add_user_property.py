from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class AddUserProperty(Request):
    """
    Adding a user property is somewhat equivalent to adding a column to the table of users. The users may be characterized by various properties of different types.
    
    Required parameters:
    
    :param property_name: Name of the user property to be created. Currently, the following names are reserved: `id`, `userid`, case-insensitively. Also, the length of the property name must not exceed 63 characters.
    
    
    :param type: Value type of the user property to be created. One of: `int`, `double`, `string`, `boolean`, `timestamp`, `set`.
    
    
    * `int` - Signed integer number.
    
    
    * `double` - Floating point number. It uses 64-bit base-2 format (IEEE 754 standard).
    
    
    * `string` - UTF-8 string.
    
    
    * `boolean` - *true* / *false*
    
    
    * `timestamp` - Value representing date and time.
    
    
    * `set` - Set of strings.
    
    

    """

    def __init__(self, property_name: str, type: str):
        super().__init__(path="/users/properties/%s" % (property_name), method='put', timeout=100000, ensure_https=False)
        self.property_name = property_name
        self.type = type

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
        params['type'] = self.type
        return params
