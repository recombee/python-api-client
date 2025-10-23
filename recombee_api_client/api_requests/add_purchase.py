from recombee_api_client.api_requests.request import Request
from recombee_api_client.utils.serialize_to_json import serialize_to_json
from typing import Union, List
from datetime import datetime
import uuid

DEFAULT = uuid.uuid4()


class AddPurchase(Request):
    """
    Adds a purchase of the given item made by the given user.

    Required parameters:

    :param user_id: User who purchased the item

    :param item_id: Purchased item


    Optional parameters:

    :param timestamp: UTC timestamp of the purchase as ISO8601-1 pattern or UTC epoch time. The default value is the current time.

    :param cascade_create: Sets whether the given user/item should be created if not present in the database.

    :param amount: Amount (number) of purchased items. The default is 1. For example, if `user-x` purchases two `item-y` during a single order (session...), the `amount` should equal 2.

    :param price: Price paid by the user for the item. If `amount` is greater than 1, the sum of prices of all the items should be given.

    :param profit: Your profit from the purchased item. The profit is natural in the e-commerce domain (for example, if `user-x` purchases `item-y` for $100 and the gross margin is 30 %, then the profit is $30) but is also applicable in other domains (for example, at a news company it may be income from a displayed advertisement on article page). If `amount` is greater than 1, the sum of profit of all the items should be given.

    :param recomm_id: If this purchase is based on a recommendation request, `recommId` is the id of the clicked recommendation.

    :param additional_data: A dictionary of additional data for the interaction.

    """

    def __init__(
        self,
        user_id: str,
        item_id: str,
        timestamp: Union[str, int, datetime] = DEFAULT,
        cascade_create: bool = DEFAULT,
        amount: float = DEFAULT,
        price: float = DEFAULT,
        profit: float = DEFAULT,
        recomm_id: str = DEFAULT,
        additional_data: dict = DEFAULT,
    ):
        super().__init__(
            path="/purchases/", method="post", timeout=3000, ensure_https=False
        )
        self.user_id = user_id
        self.item_id = item_id
        self.timestamp = timestamp
        self.cascade_create = cascade_create
        self.amount = amount
        self.price = price
        self.profit = profit
        self.recomm_id = recomm_id
        self.additional_data = additional_data

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p["userId"] = serialize_to_json(self.user_id)
        p["itemId"] = serialize_to_json(self.item_id)
        if self.timestamp is not DEFAULT:
            p["timestamp"] = serialize_to_json(self.timestamp)
        if self.cascade_create is not DEFAULT:
            p["cascadeCreate"] = serialize_to_json(self.cascade_create)
        if self.amount is not DEFAULT:
            p["amount"] = serialize_to_json(self.amount)
        if self.price is not DEFAULT:
            p["price"] = serialize_to_json(self.price)
        if self.profit is not DEFAULT:
            p["profit"] = serialize_to_json(self.profit)
        if self.recomm_id is not DEFAULT:
            p["recommId"] = serialize_to_json(self.recomm_id)
        if self.additional_data is not DEFAULT:
            p["additionalData"] = serialize_to_json(self.additional_data)

        return p

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()

        return params
