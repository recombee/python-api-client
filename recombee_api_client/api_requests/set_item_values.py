from recombee_api_client.api_requests.request import Request
from datetime import datetime

class SetItemValues(Request):
    """
    Set/update (some) property values of a given item. The properties (columns) must be previously created by [Add item property](https://docs.recombee.com/api.html#add-item-property).

    """

    def __init__(self,item_id, values):
        """
        Required parameters:
        @param item_id: ID of the item which will be modified.
        
        
        @param values: The values for the individual properties.
        
        
        Example of body:
        
        ```
        
        E{lb}
        
        "product_description": "4K TV with 3D feature",
        
        "categories":   ["Electronics", "Televisions"],
        
        "price_usd": 342,
        
        "!cascadeCreate": true
        E{rb}
        
        ```
        
        
        Special parameter `!cascadeCreate` may be used. It indicates that the item of the given itemId should be created if it does not exist in the database, as if the corresponding PUT method was used. Note the exclamation mark (!) at the beginning of the parameter's name to distinguish it from item property names.
        
        
        """
        self.item_id = item_id
        self.values = values
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'post'
        self.path = "/{databaseId}/items/%s" % (self.item_id)

    def get_body_parameters(self):
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        return {key: (val.utcnow().isoformat() if isinstance(val, datetime) else val) for (key, val) in self.values.items() }

    def get_query_parameters(self):
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
