from json import JSONDecodeError
from typing import Dict
from typing import Type

import httpx

from ..models import ResponseType
from . import errors


class BaseClient:
    """Class with method shared between async and default client"""

    ERROR_RESPONSE_MAPPING: Dict[int, Type[errors.KIKError]] = {
        422: errors.KIKValidationError,
        401: errors.KIKAuthenticationError,
        403: errors.KIKAuthenticationError,
        404: errors.KIKNotFoundError,
        400: errors.KIKValidationError,
        500: errors.KIKServerError,
    }

    def __init__(
        self,
        username: str,
        password: str,
        base_url: str = "https://api.signhost.com/api/",
    ):
        self.username = username
        self.password = password
        self.base_url = base_url

    def process_response(
        self,
        response: httpx.Response,
        model: Type[ResponseType],
        status_code_success: int = 200,
    ) -> ResponseType:
        try:
            if response.status_code == status_code_success:
                response_json = response.json()
                return model(**response_json)
            else:
                raise self.create_error(response)
        except JSONDecodeError as e:
            raise errors.KIKServerError(
                "Invalid json from server", status_code=400
            ) from e

    def create_error(self, response: httpx.Response) -> errors.KIKError:
        try:
            response_json = response.json()
        except JSONDecodeError:
            response_json = {"message": response.text}

        response_json["status_code"] = response.status_code

        exception_type = self.map_exception(response)
        return exception_type(
            status_code=response.status_code,
            json=response_json,
            message="Error from server",
        )

    def map_exception(self, response: httpx.Response) -> Type[errors.KIKError]:
        exception_type = self.ERROR_RESPONSE_MAPPING.get(
            response.status_code, errors.KIKError
        )
        return exception_type
