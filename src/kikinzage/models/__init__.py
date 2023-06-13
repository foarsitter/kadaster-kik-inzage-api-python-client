from typing import TypeVar

import pydantic

from .generated import *  # noqa


ResponseType = TypeVar("ResponseType", bound=pydantic.BaseModel)
