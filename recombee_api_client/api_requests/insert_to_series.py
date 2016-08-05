from recombee_api_client.api_requests.request import Request

class InsertToSeries(Request):
    """
    Inserts an existing item/series into series of given seriesId at position determined by time.

    """

    def __init__(self,series_id, item_type, item_id, time, cascade_create=None):
        """
        Required parameters:
        @param series_id: ID of the series to be inserted into.
        
        @param item_type: `item` iff the regular item from the catalog is to be inserted, `series` iff series is inserted as the item.
        
        @param item_id: ID of the item iff `itemType` is `item`. ID of the series iff `itemType` is `series`.
        
        @param time: Time index used for sorting items in the series. According to time, items are sorted within series in ascending order. In the example of TV show episodes, the episode number is a natural choice to be passed as time.
        
        
        Optional parameters:
        @param cascade_create: Indicates that any non-existing entity specified within the request should be created (as is corresponding PUT requests were invoked). This concerns both the `seriesId` and the `itemId`. If `cascadeCreate` is set true, the behavior also depends on the `itemType`. Either item or series may be created if not present in the database.
        
        """
        self.series_id = series_id
        self.item_type = item_type
        self.item_id = item_id
        self.time = time
        self.cascade_create = cascade_create
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'post'
        self.path = "/{databaseId}/series/%s/items/" % (self.series_id)

    def get_body_parameters(self):
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p['itemType'] = self.item_type
        p['itemId'] = self.item_id
        p['time'] = self.time
        if self.cascade_create is not None:
            p['cascadeCreate'] = self.cascade_create
        return p

    def get_query_parameters(self):
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
