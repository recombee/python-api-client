from recombee_api_client.api_requests.request import Request
import uuid

DEFAULT = uuid.uuid4()

class ListItems(Request):
    """
    Gets a list of IDs of items currently present in the catalog.
    """

    def __init__(self, filter=DEFAULT, count=DEFAULT, offset=DEFAULT, return_properties=DEFAULT, included_properties=DEFAULT):
        """
        
        Optional parameters:
        @param filter: Boolean-returning [ReQL](https://docs.recombee.com/reql.html) expression, which allows you to filter items to be listed. Only the items for which the expression is *true* will be returned.
        
        @param count: The number of items to be listed.
        
        @param offset: Specifies the number of items to skip (ordered by `itemId`).
        
        @param return_properties: With `returnProperties=true`, property values of the listed items are returned along with their IDs in a JSON dictionary. 
        
        
        Example response:
        
        ```
        
        [
        
        E{lb}
        
        "itemId": "tv-178",
        
        "description": "4K TV with 3D feature",
        
        "categories":   ["Electronics", "Televisions"],
        
        "price": 342,
        
        "url": "myshop.com/tv-178"
        E{rb},
        
        E{lb}
        
        "itemId": "mixer-42",
        
        "description": "Stainless Steel Mixer",
        
        "categories":   ["Home & Kitchen"],
        
        "price": 39,
        
        "url": "myshop.com/mixer-42"
        E{rb}
        
        ]
        
        ```
        
        
        @param included_properties: Allows to specify, which properties should be returned when `returnProperties=true` is set. The properties are given as a comma-separated list. 
        
        
        Example response for `includedProperties=description,price`:
        
        ```
        
        [
        
        E{lb}
        
        "itemId": "tv-178",
        
        "description": "4K TV with 3D feature",
        
        "price": 342
        E{rb},
        
        E{lb}
        
        "itemId": "mixer-42",
        
        "description": "Stainless Steel Mixer",
        
        "price": 39
        E{rb}
        
        ]
        
        ```
        
        
        """
        self.filter = filter
        self.count = count
        self.offset = offset
        self.return_properties = return_properties
        self.included_properties = included_properties
        self.timeout = 600000
        self.ensure_https = False
        self.method = 'get'
        self.path = "/items/list/" % ()

    def get_body_parameters(self):
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        return p

    def get_query_parameters(self):
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        if self.filter is not DEFAULT:
            params['filter'] = self.filter
        if self.count is not DEFAULT:
            params['count'] = self.count
        if self.offset is not DEFAULT:
            params['offset'] = self.offset
        if self.return_properties is not DEFAULT:
            params['returnProperties'] = self.return_properties
        if self.included_properties is not DEFAULT:
            params['includedProperties'] = self.included_properties
        return params
