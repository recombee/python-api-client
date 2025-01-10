from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class AddItemProperty(Request):
    """
    Adding an item property is somewhat equivalent to adding a column to the table of items. The items may be characterized by various properties of different types.
    
    Required parameters:
    
    :param property_name: Name of the item property to be created. Currently, the following names are reserved: `id`, `itemid`, case-insensitively. Also, the length of the property name must not exceed 63 characters.
    
    
    :param type: Value type of the item property to be created. One of: `int`, `double`, `string`, `boolean`, `timestamp`, `set`, `image` or `imageList`.
    
    
    * `int`- Signed integer number.
    
    
    * `double` - Floating point number. It uses 64-bit base-2 format (IEEE 754 standard).
    
    
    * `string` - UTF-8 string.
    
    
    * `boolean` - *true* / *false*
    
    
    * `timestamp` - Value representing date and time.
    
    
    * `set` - Set of strings.
    
    
    * `image` - URL of an image (`jpeg`, `png` or `gif`).
    
    
    * `imageList` - List of URLs that refer to images. 
    
    

    """

    def __init__(self, property_name: str, type: str):
        super().__init__(path="/items/properties/%s" % (property_name), method='put', timeout=100000, ensure_https=False)
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
