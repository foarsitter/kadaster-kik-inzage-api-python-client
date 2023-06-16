from typing import TypeVar

import pydantic

from .adres import *  # noqa
from .collectie import *  # noqa
from .eigendomsinformatie import *  # noqa
from .enum import *  # noqa
from .generated import *  # noqa
from .misc import *  # noqa
from .persoon import *  # noqa
from .stukken import *  # noqa
from .zekerheid import *  # noqa


ResponseType = TypeVar("ResponseType", bound=pydantic.BaseModel)
