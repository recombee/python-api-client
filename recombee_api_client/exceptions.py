class APIException(Exception):
    """
    Base class for exceptions that occur because of errors in requests reported by API or because of a timeout 
    """
    pass

class ResponseException(APIException):
    """
    Exception which is thrown when response status code is not 200 or 201
    """
    def __init__(self, request, status_code, description):

        super(ResponseException, self).__init__("status: %s, description: %s" % (status_code, description))

        self.request = request
        self.status_code = status_code
        self.description = description

class ApiTimeoutException(APIException):
    """
    Exception which is thrown when a request is not processed within the timeout
    """
    def __init__(self, request):

        super(ApiTimeoutException, self).__init__("ApiTimeout: client did not get response within %s ms" % request.timeout)

        self.request = request