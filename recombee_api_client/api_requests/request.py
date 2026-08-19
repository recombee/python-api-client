class Request(object):
    """
    Base class for all the requests
    """

    def __init__(self, path: str, method: str, timeout: int, ensure_https: bool):
        self.path = path
        self.method = method
        self.timeout = timeout
        self.ensure_https = ensure_https
        self.additional_query_parameters = {}
        self.additional_body_parameters = {}

    def get_body_parameters(self) -> dict:
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        raise NotImplementedError()

    def get_query_parameters(self) -> dict:
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        raise NotImplementedError()

    def set_additional_query_parameters(self, params: dict) -> "Request":
        """
        Set custom query parameters to be sent with the request.

        :param params: Dictionary of additional query parameters (name: value).
            These are merged with the parameters defined by the request and take
            precedence on name collision.

        Returns the request itself so the call can be chained.
        """
        self.additional_query_parameters = params
        return self

    def set_additional_body_parameters(self, params: dict) -> "Request":
        """
        Set custom body parameters to be sent with the request.

        :param params: Dictionary of additional body parameters (name: value).
            These are merged with the parameters defined by the request and take
            precedence on name collision.

        Returns the request itself so the call can be chained.
        """
        self.additional_body_parameters = params
        return self
