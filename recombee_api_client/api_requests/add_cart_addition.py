from recombee_api_client.api_requests.request import Request
from recombee_api_client.utils.serialize_to_json import serialize_to_json
from typing import Union, List
from datetime import datetime
import uuid

DEFAULT = uuid.uuid4()


class AddCartAddition(Request):
    """
    Adds a cart addition of the given item made by the given user.

    Required parameters:

    :param user_id: User who added the item to the cart

    :param item_id: Item added to the cart


    Optional parameters:

    :param timestamp: UTC timestamp of the cart addition as ISO8601-1 pattern or UTC epoch time. The default value is the current time.

    :param cascade_create: Sets whether the given user/item should be created if not present in the database.

    :param amount: Amount (number) added to cart. The default is 1. For example, if `user-x` adds two `item-y` during a single order (session...), the `amount` should equal 2.

    :param price: Price of the added item. If `amount` is greater than 1, the sum of prices of all the items should be given.

    :param recomm_id: If this cart addition is based on a recommendation request, `recommId` is the id of the clicked recommendation.

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
        recomm_id: str = DEFAULT,
        additional_data: dict = DEFAULT,
    ):
        super().__init__(
            path="/cartadditions/", method="post", timeout=3000, ensure_https=False
        )
        self.user_id = user_id
        self.item_id = item_id
        self.timestamp = timestamp
        self.cascade_create = cascade_create
        self.amount = amount
        self.price = price
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
