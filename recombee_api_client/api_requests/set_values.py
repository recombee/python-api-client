from recombee_api_client.api_requests.request import Request
from datetime import datetime


class SetValues(Request):
    """
    Set/update (some) property values of an entity.
    
    Required parameters:

    :param values: The values for the individual properties.
    
    Example:
    
    ```
    
    E{lb}
    
    "product_description": "4K TV with 3D feature",
    
    "categories":   ["Electronics", "Televisions"],
    
    "price_usd": 342,
    
    "!cascadeCreate": True
    E{rb}
    ```

    Optional parameters:
    
    :param cascade_create: Sets whether the given enity should be created if not present in the database.

    """

    def __init__(self, path: str, values: dict, cascade_create: bool = None):
        super().__init__(path=path, method='post', timeout=1000, ensure_https=False)
        self.values = values
        self.cascade_create = cascade_create

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        values = {key: (val.timestamp() if isinstance(val, datetime) else val) for (key, val) in self.values.items()}
        values = {key: (list(val) if isinstance(val, set) else val) for (key, val) in values.items()}

        if self.cascade_create is not None:
            values['!cascadeCreate'] = self.cascade_create
        return values

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        return dict()
