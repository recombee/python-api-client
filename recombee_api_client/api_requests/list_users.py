from recombee_api_client.api_requests.request import Request
from typing import Union, List
import uuid

DEFAULT = uuid.uuid4()

class ListUsers(Request):
    """
    Gets a list of IDs of users currently present in the catalog.
    
    Optional parameters:
    
    :param filter: Boolean-returning [ReQL](https://docs.recombee.com/reql.html) expression, which allows you to filter users to be listed. Only the users for which the expression is *true* will be returned.
    
    :param count: The number of users to be listed.
    
    :param offset: Specifies the number of users to skip (ordered by `userId`).
    
    :param return_properties: With `returnProperties=true`, property values of the listed users are returned along with their IDs in a JSON dictionary. 
    
    
    Example response:
    
    ```json
    
    [
    
    E{lb}
    
    "userId": "user-81",
    
    "country": "US",
    
    "sex": "M"
    E{rb},
    
    E{lb}
    
    "userId": "user-314",
    
    "country": "CAN",
    
    "sex": "F"
    E{rb}
    
    ]
    
    ```
    
    
    :param included_properties: Allows specifying which properties should be returned when `returnProperties=true` is set. The properties are given as a comma-separated list.
    
    
    Example response for `includedProperties=country`:
    
    ```json
    
    [
    
    E{lb}
    
    "userId": "user-81",
    
    "country": "US"
    E{rb},
    
    E{lb}
    
    "userId": "user-314",
    
    "country": "CAN"
    E{rb}
    
    ]
    
    ```
    
    

    """

    def __init__(self, filter: str = DEFAULT, count: int = DEFAULT, offset: int = DEFAULT, return_properties: bool = DEFAULT, included_properties: list = DEFAULT):
        super().__init__(path="/users/list/", method='get', timeout=100000, ensure_https=False)
        self.filter = filter
        self.count = count
        self.offset = offset
        self.return_properties = return_properties
        self.included_properties = included_properties

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        return p

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        if self.filter is not DEFAULT:
            params['filter'] = self.filter
        if self.count is not DEFAULT:
            params['count'] = self.count
        if self.offset is not DEFAULT:
            params['offset'] = self.offset
        if self.return_properties is not DEFAULT:
            params['returnProperties'] = self.return_properties
        if self.included_properties is not DEFAULT:
            params['includedProperties'] = self.included_properties
        return params
