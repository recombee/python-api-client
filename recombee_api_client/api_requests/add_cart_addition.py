from recombee_api_client.api_requests.request import Request
import uuid

DEFAULT = uuid.uuid4()

class AddCartAddition(Request):
    """
    Adds a cart addition of a given item made by a given user.

    """

    def __init__(self, user_id, item_id, timestamp=DEFAULT, cascade_create=DEFAULT, amount=DEFAULT, price=DEFAULT, recomm_id=DEFAULT, additional_data=DEFAULT):
        """
        Required parameters:
        @param user_id: User who added the item to the cart
        
        @param item_id: Item added to the cart
        
        
        Optional parameters:
        @param timestamp: UTC timestamp of the cart addition as ISO8601-1 pattern or UTC epoch time. The default value is the current time.
        
        @param cascade_create: Sets whether the given user/item should be created if not present in the database.
        
        @param amount: Amount (number) added to cart. The default is 1. For example if `user-x` adds two `item-y` during a single order (session...), the `amount` should equal to 2.
        
        @param price: Price of the added item. If `amount` is greater than 1, sum of prices of all the items should be given.
        
        @param recomm_id: If this cart addition is based on a recommendation request, `recommId` is the id of the clicked recommendation.
        
        @param additional_data: A dictionary of additional data for the interaction.
        
        """
        self.user_id = user_id
        self.item_id = item_id
        self.timestamp = timestamp
        self.cascade_create = cascade_create
        self.amount = amount
        self.price = price
        self.recomm_id = recomm_id
        self.additional_data = additional_data
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'post'
        self.path = "/cartadditions/" % ()

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
