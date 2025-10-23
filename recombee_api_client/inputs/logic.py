from recombee_api_client.inputs.input import Input
from recombee_api_client.utils.serialize_to_json import serialize_to_json

from typing import Union, List
from datetime import datetime
import uuid

DEFAULT = uuid.uuid4()


class Logic(Input):
    """
    Initializes Logic input

    Optional parameters:

    :param name: Name of the logic that should be used

    :param settings: Parameters passed to the logic

    """

    def __init__(self, name: str = DEFAULT, settings: dict = DEFAULT):
        self.name = name
        self.settings = settings

    def to_dict(self) -> dict:
        """
        Serializes the input into a dict for sending to the Recombee API.
        """
        res = dict()
        if self.name is not DEFAULT:
            res["name"] = serialize_to_json(self.name)
        if self.settings is not DEFAULT:
            res["settings"] = serialize_to_json(self.settings)

        return res
