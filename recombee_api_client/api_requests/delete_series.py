from recombee_api_client.api_requests.request import Request

class DeleteSeries(Request):
    """
    Deletes the series of given `seriesId` from the database.
    
    Deleting a series will only delete assignment of items to it, not the items themselves!

    """

    def __init__(self,series_id):
        """
        Required parameters:
        @param series_id: ID of the series to be deleted.
        
        """
        self.series_id = series_id
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'delete'
        self.path = "/{databaseId}/series/%s" % (self.series_id)

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
