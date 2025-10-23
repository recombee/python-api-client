class Input(object):

    def to_dict(self) -> dict:
        """
        Serializes the input into a dict for sending to the Recombee API.
        """
        raise NotImplementedError()
