from recombee_api_client.inputs.input import Input
from recombee_api_client.utils.serialize_to_json import serialize_to_json

from typing import Union, List
from datetime import datetime
import uuid

DEFAULT = uuid.uuid4()


class PropertyMetadata(Input):
    """
    Initializes PropertyMetadata input
    Required parameters:

    :param name: Name of the [metadata](https://docs.recombee.com/api/property_roles_metadata#metadata) assigned to the property.


    Optional parameters:

    :param settings: Optional configuration for this metadata entry.

    """

    def __init__(self, name: str, settings: dict = DEFAULT):
        self.name = name
        self.settings = settings

    def to_dict(self) -> dict:
        """
        Serializes the input into a dict for sending to the Recombee API.
        """
        res = dict()
        res["name"] = serialize_to_json(self.name)
        if self.settings is not DEFAULT:
            res["settings"] = serialize_to_json(self.settings)

        return res
