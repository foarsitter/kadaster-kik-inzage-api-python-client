import json
import os
from pathlib import Path
from typing import Any
from typing import AsyncIterator
from typing import Iterator

import pytest
import pytest_asyncio
import respx
from httpx import Response

from kikinzage.client import AsyncClient
from kikinzage.client.default import DefaultClient


MOCKED_RESPONSES_PATH = Path(__file__).parent / "responses.json"
MOCK_USE = os.getenv("MOCK_USE", True)
MOCK_SAFE = os.getenv("MOCK_USE", False)


def write_response(response: Response) -> None:  # pragma: no cover
    url = response.request.url
    response.read()
    json_response = response.json()

    content = json.load(MOCKED_RESPONSES_PATH.open())
    content[str(url)] = json_response

    json.dump(content, MOCKED_RESPONSES_PATH.open("w"))


def mock_responses() -> None:
    content = json.load(MOCKED_RESPONSES_PATH.open())

    for url, response in content.items():
        route = respx.get(url)
        route.return_value = Response(
            status_code=200,
            content=json.dumps(response).encode(),
        )


mock_responses()


@pytest.fixture
def kik() -> Iterator[DefaultClient]:
    password = os.getenv("KIK_PASSWORD")
    username = os.getenv("KIK_USERNAME")

    if not password or not username:  # pragma: no cover
        raise Exception(
            "KIK_PASSWORD and KIK_USERNAME environment variables must be set"
        )

    httpx_kwargs: Any = dict(
        username=username,
        password=password,
        klantreferentie="test",
    )

    if MOCK_USE is False and MOCK_SAFE is True:  # pragma: no cover
        httpx_kwargs["event_hooks"] = {"response": [write_response]}

    if MOCK_USE:
        with respx.mock:
            yield DefaultClient(**httpx_kwargs)
    else:
        yield DefaultClient(**httpx_kwargs)  # pragma: no cover


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
        # event_hooks={"response": [write_response]},
    )

    if MOCK_SAFE:  # pragma: no cover
        raise Exception("Cannot use event_hooks in async context")

    if MOCK_USE:
        with respx.mock:
            async with c as kik:
                yield kik
    else:
        async with c as kik:
            yield kik
