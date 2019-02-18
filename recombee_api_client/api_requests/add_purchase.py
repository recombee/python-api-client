from recombee_api_client.api_requests.request import Request
import uuid

DEFAULT = uuid.uuid4()

class AddPurchase(Request):
    """
    Adds a purchase of a given item made by a given user.

    """

    def __init__(self, user_id, item_id, timestamp=DEFAULT, cascade_create=DEFAULT, amount=DEFAULT, price=DEFAULT, profit=DEFAULT, recomm_id=DEFAULT, additional_data=DEFAULT):
        """
        Required parameters:
        @param user_id: User who purchased the item
        
        @param item_id: Purchased item
        
        
        Optional parameters:
        @param timestamp: UTC timestamp of the purchase as ISO8601-1 pattern or UTC epoch time. The default value is the current time.
        
        @param cascade_create: Sets whether the given user/item should be created if not present in the database.
        
        @param amount: Amount (number) of purchased items. The default is 1. For example if `user-x` purchases two `item-y` during a single order (session...), the `amount` should equal to 2.
        
        @param price: Price paid by the user for the item. If `amount` is greater than 1, sum of prices of all the items should be given.
        
        @param profit: Your profit from the purchased item. The profit is natural in e-commerce domain (for example if `user-x` purchases `item-y` for $100 and the gross margin is 30 %, then the profit is $30), but is applicable also in other domains (for example at a news company it may be income from displayed advertisement on article page). If `amount` is greater than 1, sum of profit of all the items should be given.
        
        @param recomm_id: If this purchase is based on a recommendation request, `recommId` is the id of the clicked recommendation.
        
        @param additional_data: A dictionary of additional data for the interaction.
        
        """
        self.user_id = user_id
        self.item_id = item_id
        self.timestamp = timestamp
        self.cascade_create = cascade_create
        self.amount = amount
        self.price = price
        self.profit = profit
        self.recomm_id = recomm_id
        self.additional_data = additional_data
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'post'
        self.path = "/purchases/" % ()

    def get_body_parameters(self):
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p['userId'] = self.user_id
        p['itemId'] = self.item_id
        if self.timestamp is not DEFAULT:
            p['timestamp'] = self.timestamp
        if self.cascade_create is not DEFAULT:
            p['cascadeCreate'] = self.cascade_create
        if self.amount is not DEFAULT:
            p['amount'] = self.amount
        if self.price is not DEFAULT:
            p['price'] = self.price
        if self.profit is not DEFAULT:
            p['profit'] = self.profit
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
