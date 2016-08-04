from recombee_api_client.api_requests.request import Request

class GetItemPropertyInfo(Request):
    """
    Gets information about specified item property.

    """

    def __init__(self,property_name):
        """
        Required parameters:
        @param property_name: Name of the property about which the information is to be retrieved.
        
        """
        self.property_name = property_name
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'get'
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
        return params
