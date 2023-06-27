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


@pytest.mark.xfail
@pytest.mark.live
def test_brondocument_live(kik: DefaultClient) -> None:
    response = kik.brondocument("2", "2", "50001", "38")

    assert isinstance(response, Brondocument)


@pytest.mark.asyncio
@pytest.mark.xfail
@pytest.mark.live
async def test_brondocument_async_live(akik: AsyncClient) -> None:
    response = await akik.brondocument("2", "2", "50001", "38")

    assert isinstance(response, Brondocument)
