from recombee_api_client.api_requests.request import Request
from datetime import datetime

class SetValues(Request):
    """
    Set/update (some) property values of an entity.

    """

    def __init__(self, values, cascade_create=None):
        """
        Required parameters:
        
        @param values: The values for the individual properties.
        
        Example:
        
        ```
        
        E{lb}
        
        "product_description": "4K TV with 3D feature",
        
        "categories":   ["Electronics", "Televisions"],
        
        "price_usd": 342,
        
        "!cascadeCreate": True
        E{rb}

        Optional parameters:
        
        @param cascade_create: Sets whether the given enity should be created if not present in the database.
        ```        
        
        """
        self.values = values
        self.cascade_create = cascade_create
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'post'

    def get_body_parameters(self):
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        values = {key: (val.utcnow().isoformat() if isinstance(val, datetime) else val) for (key, val) in self.values.items() }
        if self.cascade_create is not None:
            values['!cascadeCreate'] = self.cascade_create
        return values

    def get_query_parameters(self):
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        return dict()