from typing import Any
from typing import Dict
from typing import Optional


class KIKError(Exception):
    def __init__(
        self, message: str, status_code: int, json: Optional[Dict[str, Any]] = None
    ):
        super().__init__(message)
        self.json = json
        self.status_code = status_code


class KIKValidationError(KIKError):
    pass


class KIKAuthenticationError(KIKError):
    pass


class KIKNotFoundError(KIKError):
    pass


class KIKServerError(KIKError):
    pass
