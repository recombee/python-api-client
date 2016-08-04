from recombee_api_client.api_requests.request import Request

class DeleteItemProperty(Request):
    """
    Deleting an item property is roughly equivalent to removing a column from the table of items.

    """

    def __init__(self,property_name):
        """
        Required parameters:
        @param property_name: Name of the property to be deleted.
        
        """
        self.property_name = property_name
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'delete'
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
