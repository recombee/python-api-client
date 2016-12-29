from recombee_api_client.api_requests.set_values import SetValues

class SetUserValues(SetValues):
    """
    Set/update (some) property values of a given user. The properties (columns) must be previously created by [Add user property](https://docs.recombee.com/api.html#add-user-property).

    """

    def __init__(self,user_id, values, cascade_create=None):
        """
        Required parameters:
        @param user_id: ID of the user which will be modified.
        
        
        @param values: The values for the individual properties.
        
        Example:
        
        ```
        
        E{lb}
        
            "country": "US",
            "sex": "F",
        E{rb}
        
        ```

        Optional parameters:
        
        @param cascade_create: Sets whether the given user should be created if not present in the database.
        """
        super(SetUserValues, self).__init__(values, cascade_create=cascade_create)

        self.user_id = user_id
        self.path = "/{databaseId}/users/%s" % (self.user_id)