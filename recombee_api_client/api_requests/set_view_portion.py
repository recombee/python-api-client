from recombee_api_client.api_requests.request import Request
import uuid

DEFAULT = uuid.uuid4()

class SetViewPortion(Request):
    """
    Sets viewed portion of an item (for example a video or article) by a user (at a session).
    If you send new request with the same (`userId`, `itemId`, `sessionId`), the portion gets updated.

    """

    def __init__(self, user_id, item_id, portion, session_id=DEFAULT, timestamp=DEFAULT, cascade_create=DEFAULT, recomm_id=DEFAULT, additional_data=DEFAULT):
        """
        Required parameters:
        @param user_id: User who viewed a portion of the item
        
        @param item_id: Viewed item
        
        @param portion: Viewed portion of the item (number between 0.0 (viewed nothing) and 1.0 (viewed full item) ). It should be the really viewed part of the item, no matter seeking, so for example if the user seeked immediately to half of the item and then viewed 10% of the item, the `portion` should still be `0.1`.
        
        
        Optional parameters:
        @param session_id: ID of session in which the user viewed the item. Default is `null` (`None`, `nil`, `NULL` etc. depending on language).
        
        @param timestamp: UTC timestamp of the rating as ISO8601-1 pattern or UTC epoch time. The default value is the current time.
        
        @param cascade_create: Sets whether the given user/item should be created if not present in the database.
        
        @param recomm_id: If this view portion is based on a recommendation request, `recommId` is the id of the clicked recommendation.
        
        @param additional_data: A dictionary of additional data for the interaction.
        
        """
        self.user_id = user_id
        self.item_id = item_id
        self.portion = portion
        self.session_id = session_id
        self.timestamp = timestamp
        self.cascade_create = cascade_create
        self.recomm_id = recomm_id
        self.additional_data = additional_data
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'post'
        self.path = "/viewportions/" % ()

    def get_body_parameters(self):
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p['userId'] = self.user_id
        p['itemId'] = self.item_id
        p['portion'] = self.portion
        if self.session_id is not DEFAULT:
            p['sessionId'] = self.session_id
        if self.timestamp is not DEFAULT:
            p['timestamp'] = self.timestamp
        if self.cascade_create is not DEFAULT:
            p['cascadeCreate'] = self.cascade_create
        if self.recomm_id is not DEFAULT:
            p['recommId'] = self.recomm_id
        if self.additional_data is not DEFAULT:
            p['additionalData'] = self.additional_data
        return p

    def get_query_parameters(self):
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
