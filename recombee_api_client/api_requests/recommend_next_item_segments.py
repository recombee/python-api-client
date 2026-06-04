from recombee_api_client.api_requests.request import Request
from recombee_api_client.utils.serialize_to_json import serialize_to_json
from typing import Union, List
from datetime import datetime
import uuid

DEFAULT = uuid.uuid4()


class RecommendNextItemSegments(Request):
    """
    Returns [Item Segments](https://docs.recombee.com/segmentations) to be shown as the next recommendations when a user scrolls (e.g., within a carousel or feed of Item Segments such as brands, artists, topics, or categories).

    The request requires the `recommId` of a base recommendation request and the number of Segments to return (`count`).

    The base request can be one of:
      - [Recommend Item Segments to Item](https://docs.recombee.com/api#recommend-item-segments-to-item)
      - [Recommend Item Segments to User](https://docs.recombee.com/api#recommend-item-segments-to-user)
      - [Recommend Item Segments to Item Segment](https://docs.recombee.com/api#recommend-item-segments-to-item-segment)
      - [Search Item Segments](https://docs.recombee.com/api#search-item-segments)

    All other parameters are inherited from the base request associated with the provided `recommId`.

    This endpoint can be called multiple times for a single `recommId`. Each call returns different Item Segments that have not been recommended in previous calls.
    The number of calls made so far is returned in the `numberNextRecommsCalls` field.

    Requests can be made up to 30 minutes after the base request or the most recent Recommend Next Item Segments call.

    For billing purposes, each call to this endpoint is counted as a separate recommendation request.

    Required parameters:

    :param recomm_id: ID of the base recommendation request for which next recommendations should be returned

    :param count: Number of item segments to be recommended


    """

    def __init__(self, recomm_id: str, count: int):
        super().__init__(
            path="/recomms/next/item-segments/%s" % (recomm_id),
            method="post",
            timeout=3000,
            ensure_https=False,
        )
        self.recomm_id = recomm_id
        self.count = count

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p["count"] = serialize_to_json(self.count)

        return p

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()

        return params
