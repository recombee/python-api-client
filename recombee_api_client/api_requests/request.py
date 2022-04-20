class Request(object):
    """
    Base class for all the requests
    """
    def __init__(self, path: str, method: str, timeout: int, ensure_https: bool):
        self.path = path
        self.method = method
        self.timeout = timeout
        self.ensure_https = ensure_https

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
