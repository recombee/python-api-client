from recombee_api_client.api_requests.request import Request
from recombee_api_client.utils.serialize_to_json import serialize_to_json
from typing import Union, List
from datetime import datetime
import uuid

DEFAULT = uuid.uuid4()


class SetViewPortion(Request):
    """
    Sets viewed portion of an item (for example a video or article) by a user (at a session).
    If you send a new request with the same (`userId`, `itemId`, `sessionId`), the portion gets updated.

    Required parameters:

    :param user_id: User who viewed a portion of the item

    :param item_id: Viewed item

    :param portion: Viewed portion of the item (number between 0.0 (viewed nothing) and 1.0 (viewed full item) ). It should be the actual viewed part of the item, no matter the seeking. For example, if the user seeked immediately to half of the item and then viewed 10% of the item, the `portion` should still be `0.1`.


    Optional parameters:

    :param session_id: ID of the session in which the user viewed the item. Default is `null` (`None`, `nil`, `NULL` etc., depending on the language).

    :param timestamp: UTC timestamp of the view portion as ISO8601-1 pattern or UTC epoch time. The default value is the current time.

    :param cascade_create: Sets whether the given user/item should be created if not present in the database.

    :param recomm_id: If this view portion is based on a recommendation request, `recommId` is the id of the clicked recommendation.

    :param additional_data: A dictionary of additional data for the interaction.

    :param auto_presented: Indicates whether the item was automatically presented to the user (e.g., in a swiping feed) or explicitly requested by the user (e.g., by clicking on a link). Defaults to `false`.

    :param time_spent: The duration (in seconds) that the user viewed the item. In update requests, this value may only increase and is required only if it has changed.

    """

    def __init__(
        self,
        user_id: str,
        item_id: str,
        portion: float,
        session_id: str = DEFAULT,
        timestamp: Union[str, int, datetime] = DEFAULT,
        cascade_create: bool = DEFAULT,
        recomm_id: str = DEFAULT,
        additional_data: dict = DEFAULT,
        auto_presented: bool = DEFAULT,
        time_spent: float = DEFAULT,
    ):
        super().__init__(
            path="/viewportions/", method="post", timeout=3000, ensure_https=False
        )
        self.user_id = user_id
        self.item_id = item_id
        self.portion = portion
        self.session_id = session_id
        self.timestamp = timestamp
        self.cascade_create = cascade_create
        self.recomm_id = recomm_id
        self.additional_data = additional_data
        self.auto_presented = auto_presented
        self.time_spent = time_spent

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p["userId"] = serialize_to_json(self.user_id)
        p["itemId"] = serialize_to_json(self.item_id)
        p["portion"] = serialize_to_json(self.portion)
        if self.session_id is not DEFAULT:
            p["sessionId"] = serialize_to_json(self.session_id)
        if self.timestamp is not DEFAULT:
            p["timestamp"] = serialize_to_json(self.timestamp)
        if self.cascade_create is not DEFAULT:
            p["cascadeCreate"] = serialize_to_json(self.cascade_create)
        if self.recomm_id is not DEFAULT:
            p["recommId"] = serialize_to_json(self.recomm_id)
        if self.additional_data is not DEFAULT:
            p["additionalData"] = serialize_to_json(self.additional_data)
        if self.auto_presented is not DEFAULT:
            p["autoPresented"] = serialize_to_json(self.auto_presented)
        if self.time_spent is not DEFAULT:
            p["timeSpent"] = serialize_to_json(self.time_spent)

        return p

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()

        return params
