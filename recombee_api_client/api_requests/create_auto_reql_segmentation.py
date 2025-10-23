from recombee_api_client.api_requests.request import Request
from recombee_api_client.utils.serialize_to_json import serialize_to_json
from typing import Union, List
from datetime import datetime
import uuid

DEFAULT = uuid.uuid4()


class CreateAutoReqlSegmentation(Request):
    """
    Segment the items using a [ReQL](https://docs.recombee.com/reql) expression.

    For each item, the expression should return a set that contains IDs of segments to which the item belongs to.

    Required parameters:

    :param segmentation_id: ID of the newly created Segmentation

    :param source_type: What type of data should be segmented. Currently only `items` are supported.


    :param expression: ReQL expression that returns for each item a set with IDs of segments to which the item belongs



    Optional parameters:

    :param title: Human-readable name that is shown in the Recombee Admin UI.


    :param description: Description that is shown in the Recombee Admin UI.


    """

    def __init__(
        self,
        segmentation_id: str,
        source_type: str,
        expression: str,
        title: str = DEFAULT,
        description: str = DEFAULT,
    ):
        super().__init__(
            path="/segmentations/auto-reql/%s" % (segmentation_id),
            method="put",
            timeout=10000,
            ensure_https=False,
        )
        self.segmentation_id = segmentation_id
        self.source_type = source_type
        self.expression = expression
        self.title = title
        self.description = description

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p["sourceType"] = serialize_to_json(self.source_type)
        p["expression"] = serialize_to_json(self.expression)
        if self.title is not DEFAULT:
            p["title"] = serialize_to_json(self.title)
        if self.description is not DEFAULT:
            p["description"] = serialize_to_json(self.description)

        return p

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()

        return params
