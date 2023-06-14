from typing import Any
from typing import Dict
from typing import Optional


class KIKError(Exception):
    """Base exception for all KIKinzage errors"""


class KIKRequestError(KIKError):
    def __init__(
        self, message: str, status_code: int, json: Optional[Dict[str, Any]] = None
    ):
        super().__init__(message)
        self.json = json
        self.status_code = status_code


class KIKValidationError(KIKRequestError):
    pass


class KIKAuthenticationError(KIKRequestError):
    pass


class KIKNotFoundError(KIKRequestError):
    pass


class KIKServerError(KIKRequestError):
    pass
