import pytest

from kikinzage.client import AsyncClient
from kikinzage.client import DefaultClient
from kikinzage.models import Datuminformatie


def test_datuminformatie(kik: DefaultClient) -> None:
    response = kik.datuminformatie("test")

    assert isinstance(response, Datuminformatie)


@pytest.mark.asyncio
async def test_datuminformatie_async(akik: AsyncClient) -> None:
    response = await akik.datuminformatie("test")

    assert isinstance(response, Datuminformatie)
