import pytest

from kikinzage.client import AsyncClient
from kikinzage.client import DefaultClient
from kikinzage.models import Eigenaarsinformatie


def test_burgerservicenummer(kik: DefaultClient) -> None:
    response = kik.eigenaarsinformatie_burgerservicenummer("123456788")

    assert isinstance(response, Eigenaarsinformatie)


@pytest.mark.asyncio
async def test_burgerservicenummer_async(akik: AsyncClient) -> None:
    response = await akik.eigenaarsinformatie_burgerservicenummer("123456788")

    assert isinstance(response, Eigenaarsinformatie)


def test_eigenaarsinformatie_kadastraalpersoonidentificatie(kik: DefaultClient) -> None:
    response = kik.eigenaarsinformatie_kadastraalpersoonidentificatie("11304723")

    assert isinstance(response, Eigenaarsinformatie)


@pytest.mark.asyncio
async def test_eigenaarsinformatie_kadastraalpersoonidentificatie_async(
    akik: AsyncClient,
) -> None:
    response = await akik.eigenaarsinformatie_kadastraalpersoonidentificatie("11304723")

    assert isinstance(response, Eigenaarsinformatie)
