from recombee_api_client.api_requests.request import Request
from recombee_api_client.utils.serialize_to_json import serialize_to_json
from typing import Union, List
from datetime import datetime
import uuid

DEFAULT = uuid.uuid4()


class AddDetailView(Request):
    """
    Adds a detail view of the given item made by the given user.

    Required parameters:

    :param user_id: User who viewed the item

    :param item_id: Viewed item


    Optional parameters:

    :param timestamp: UTC timestamp of the view as ISO8601-1 pattern or UTC epoch time. The default value is the current time.

    :param duration: Duration of the view

    :param cascade_create: Sets whether the given user/item should be created if not present in the database.

    :param recomm_id: If this detail view is based on a recommendation request, `recommId` is the id of the clicked recommendation.

    :param additional_data: A dictionary of additional data for the interaction.

    :param auto_presented: Indicates whether the item was automatically presented to the user (e.g., in a swiping feed) or explicitly requested by the user (e.g., by clicking on a link). Defaults to `false`.

    """

    def __init__(
        self,
        user_id: str,
        item_id: str,
        timestamp: Union[str, int, datetime] = DEFAULT,
        duration: int = DEFAULT,
        cascade_create: bool = DEFAULT,
        recomm_id: str = DEFAULT,
        additional_data: dict = DEFAULT,
        auto_presented: bool = DEFAULT,
    ):
        super().__init__(
            path="/detailviews/", method="post", timeout=3000, ensure_https=False
        )
        self.user_id = user_id
        self.item_id = item_id
        self.timestamp = timestamp
        self.duration = duration
        self.cascade_create = cascade_create
        self.recomm_id = recomm_id
        self.additional_data = additional_data
        self.auto_presented = auto_presented

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p["userId"] = serialize_to_json(self.user_id)
        p["itemId"] = serialize_to_json(self.item_id)
        if self.timestamp is not DEFAULT:
            p["timestamp"] = serialize_to_json(self.timestamp)
        if self.duration is not DEFAULT:
            p["duration"] = serialize_to_json(self.duration)
        if self.cascade_create is not DEFAULT:
            p["cascadeCreate"] = serialize_to_json(self.cascade_create)
        if self.recomm_id is not DEFAULT:
            p["recommId"] = serialize_to_json(self.recomm_id)
        if self.additional_data is not DEFAULT:
            p["additionalData"] = serialize_to_json(self.additional_data)
        if self.auto_presented is not DEFAULT:
            p["autoPresented"] = serialize_to_json(self.auto_presented)

        return p

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()

        return params
