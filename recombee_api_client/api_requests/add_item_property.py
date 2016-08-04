from recombee_api_client.api_requests.request import Request

class AddItemProperty(Request):
    """
    Adding an item property is somehow equivalent to adding a column to the table of items. The items may be characterized by various properties of different types.

    """

    def __init__(self,property_name, type):
        """
        Required parameters:
        @param property_name: Name of the item property to be created. Currently, the following names are reserved:`id`, `itemid`, case insensitively. Also, the length of the property name must not exceed 63 characters.
        
        
        @param type: Value type of the item property to be created. One of: `int`, `double`, `string`, `boolean`, `timestamp`, `set`
        
        
        """
        self.property_name = property_name
        self.type = type
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'put'
        self.path = "/{databaseId}/items/properties/%s" % (self.property_name)

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
        params['type'] = self.type
        return params
