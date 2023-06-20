import os
from typing import AsyncIterator

import pytest
import pytest_asyncio

from kikinzage.client import AsyncClient
from kikinzage.client.default import DefaultClient


@pytest.fixture
def kik() -> DefaultClient:
    password = os.getenv("KIK_PASSWORD")
    username = os.getenv("KIK_USERNAME")

    if not password or not username:  # pragma: no cover
        raise Exception(
            "KIK_PASSWORD and KIK_USERNAME environment variables must be set"
        )

    return DefaultClient(
        username=username,
        password=password,
        klantreferentie="test",
    )


@pytest_asyncio.fixture(scope="function")
async def akik() -> AsyncIterator[AsyncClient]:
    password = os.getenv("KIK_PASSWORD")
    username = os.getenv("KIK_USERNAME")

    if not password or not username:  # pragma: no cover
        raise Exception(
            "KIK_PASSWORD and KIK_USERNAME environment variables must be set"
        )

    c = AsyncClient(
        username=username,
        password=password,
        klantreferentie="test",
    )

    async with c as kik:
        yield kik
