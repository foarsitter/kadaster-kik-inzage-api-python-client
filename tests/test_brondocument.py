import pytest

from kikinzage.client import AsyncClient
from kikinzage.client import DefaultClient
from kikinzage.models import Brondocument


def test_brondocument(kik: DefaultClient) -> None:
    response = kik.brondocument("2", "2", "50001", "38")

    assert isinstance(response, Brondocument)


@pytest.mark.asyncio
async def test_brondocument_async(akik: AsyncClient) -> None:
    response = await akik.brondocument("2", "2", "50001", "38")

    assert isinstance(response, Brondocument)
