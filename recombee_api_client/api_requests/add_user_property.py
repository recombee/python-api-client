from recombee_api_client.inputs.property_metadata import PropertyMetadata
from recombee_api_client.inputs.property_role import PropertyRole
from recombee_api_client.api_requests.request import Request
from recombee_api_client.utils.serialize_to_json import serialize_to_json
from typing import Union, List
from datetime import datetime
import uuid

DEFAULT = uuid.uuid4()


class AddUserProperty(Request):
    """
    Adding a user property is somewhat equivalent to adding a column to the table of users. The users may be characterized by various properties of different types.

    Required parameters:

    :param property_name: Name of the user property to be created. Currently, the following names are reserved: `id`, `userid`, case-insensitively. Also, the length of the property name must not exceed 63 characters.


    :param type: Value type of the user property to be created. One of: `int`, `double`, `string`, `boolean`, `timestamp`, `set`.


    * `int` - Signed integer number.


    * `double` - Floating point number. It uses 64-bit base-2 format (IEEE 754 standard).


    * `string` - UTF-8 string.


    * `boolean` - *true* / *false*


    * `timestamp` - Value representing date and time. ISO8601-1 pattern (string) or UTC epoch time (number).


    * `set` - Set of strings.



    Optional parameters:

    :param role: [Role](https://docs.recombee.com/api/property_roles_metadata#roles) to assign to the property.


    :param metadata: List of [metadata](https://docs.recombee.com/api/property_roles_metadata#metadata) entries to assign to the property.

    """

    def __init__(
        self,
        property_name: str,
        type: str,
        role: PropertyRole = DEFAULT,
        metadata: List[PropertyMetadata] = DEFAULT,
    ):
        super().__init__(
            path="/users/properties/%s" % (property_name),
            method="put",
            timeout=100000,
            ensure_https=False,
        )
        self.property_name = property_name
        self.type = type
        self.role = role
        self.metadata = metadata

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p["type"] = serialize_to_json(self.type)
        if self.role is not DEFAULT:
            p["role"] = serialize_to_json(self.role)
        if self.metadata is not DEFAULT:
            p["metadata"] = serialize_to_json(self.metadata)

        return p

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()

        return params
