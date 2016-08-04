from recombee_api_client.api_requests.request import Request

class RemoveFromSeries(Request):
    """
    Removes an existing series item from the series.
    """

    def __init__(self,series_id, item_type, item_id, time):
        """
        Required parameters:
        @param series_id: ID of the series from which a series item is to be removed.
        
        @param item_type: Type of the item to be removed.
        
        @param item_id: ID of the item iff `itemType` is `item`. ID of the series iff `itemType` is `series`.
        
        @param time: Time index of the item to be removed.
        
        """
        self.series_id = series_id
        self.item_type = item_type
        self.item_id = item_id
        self.time = time
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'delete'
        self.path = "/{databaseId}/series/%s/items/" % (self.series_id)

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
        params['itemType'] = self.item_type
        params['itemId'] = self.item_id
        params['time'] = self.time
        return params
