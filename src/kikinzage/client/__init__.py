from typing import Any
from typing import Dict

from .asyncio import AsyncClient  # noqa
from .base import KikinzageBaseClient  # noqa
from .default import DefaultClient  # noqa


__all__ = ["KikinzageBaseClient", "DefaultClient", "AsyncClient"]

RequestFixtures = Dict[str, Dict[str, Dict[str, Any]]]
