"""Error Messages."""


class BaseErrorMessage:
    """Base error message."""
    status_code: int
    message_code: int
    message: str

    def __init__(self, *args):
        self.message = self.message.format(*args)
