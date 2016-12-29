from recombee_api_client.api_requests.set_values import SetValues

class SetItemValues(SetValues):
    """
    Set/update (some) property values of a given item. The properties (columns) must be previously created by [Add item property](https://docs.recombee.com/api.html#add-item-property).

    """

    def __init__(self,item_id, values, cascade_create=None):
        """
        Required parameters:
        @param item_id: ID of the item which will be modified.
        
        
        @param values: The values for the individual properties.
        
        
        Example:
        
        ```
        
        E{lb}
        
        "product_description": "4K TV with 3D feature",
        
        "categories":   ["Electronics", "Televisions"],
        
        "price_usd": 342,
        
        E{rb}
        
        ```        

        Optional parameters:
        
        @param cascade_create: Sets whether the given item should be created if not present in the database.
        """
        super(SetItemValues, self).__init__(values, cascade_create=cascade_create)

        self.item_id = item_id
        self.path = "/{databaseId}/items/%s" % (self.item_id)