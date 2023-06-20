import pytest

from kikinzage.client import AsyncClient
from kikinzage.client import DefaultClient
from kikinzage.models import ObjectlijstPersoon


def test_burgerservicenummer(kik: DefaultClient) -> None:
    response = kik.objectlijstpersoon_burgerservicenummer("123456788")

    assert isinstance(response, ObjectlijstPersoon)


@pytest.mark.asyncio
async def test_burgerservicenummer_async(akik: AsyncClient) -> None:
    response = await akik.objectlijstpersoon_burgerservicenummer("123456788")

    assert isinstance(response, ObjectlijstPersoon)


def test_objectlijstpersoon_kadastraalpersoonidentificatie(kik: DefaultClient) -> None:
    response = kik.objectlijstpersoon_kadastraalpersoonidentificatie("11304723")

    assert isinstance(response, ObjectlijstPersoon)


@pytest.mark.asyncio
async def test_objectlijstpersoon_kadastraalpersoonidentificatie_async(
    akik: AsyncClient,
) -> None:
    response = await akik.objectlijstpersoon_kadastraalpersoonidentificatie("11304723")

    assert isinstance(response, ObjectlijstPersoon)
