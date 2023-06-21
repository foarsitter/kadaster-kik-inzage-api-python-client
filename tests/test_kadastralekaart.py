from typing import Optional

import pytest

from kikinzage.client import AsyncClient
from kikinzage.client.default import DefaultClient
from kikinzage.models import Formaat
from kikinzage.models import KadastraleKaart


@pytest.mark.parametrize(
    "postcode,huisnummer,huisletter,huisnummertoevoeging",
    [
        ("4884ME", 16, None, "K298"),
        ("1016AK", 402, "B", None),
        ("1012AR", 41, "C", None),
        ("6301VK", 21, None, None),
    ],
)
def test_postcode(
    kik: DefaultClient,
    postcode: str,
    huisnummer: int,
    huisletter: Optional[str],
    huisnummertoevoeging: Optional[str],
) -> None:
    response = kik.kadastralekaart_postcode(
        postcode=postcode,
        huisnummer=huisnummer,
        huisletter=huisletter,
        huisnummertoevoeging=huisnummertoevoeging,
        formaat=Formaat.JSON,
        klantreferentie="onbekend",
    )

    assert isinstance(response, KadastraleKaart)


def test_postcode_pdf(kik: DefaultClient) -> None:
    response = kik.kadastralekaart_postcode(
        postcode="4884ME",
        huisnummer=16,
        formaat=Formaat.PDF,
        klantreferentie="onbekend",
        huisnummertoevoeging="K298",
    )

    assert isinstance(response, KadastraleKaart)


@pytest.mark.asyncio
async def test_postcode_pdf_async(akik: AsyncClient) -> None:
    response = await akik.kadastralekaart_postcode(
        postcode="4884ME",
        huisnummer=16,
        formaat=Formaat.JSON,
        klantreferentie="onbekend",
        huisnummertoevoeging="K298",
    )
    assert isinstance(response, KadastraleKaart)


def test_kadastraalobjectidentificatie(kik: DefaultClient) -> None:
    response = kik.kadastralekaart_kadastraalobjectidentificatie(
        kadastraalobjectidentificatie="11010156070000",
        formaat=Formaat.JSON,
        klantreferentie="onbekend",
    )

    assert isinstance(response, KadastraleKaart)


@pytest.mark.asyncio
async def test_kadastraalobjectidentificatie_async(akik: AsyncClient) -> None:
    response = await akik.kadastralekaart_kadastraalobjectidentificatie(
        kadastraalobjectidentificatie="11010156070000",
        formaat=Formaat.JSON,
        klantreferentie="onbekend",
    )

    assert isinstance(response, KadastraleKaart)


def test_kadastraleaanduiding(kik: DefaultClient) -> None:
    response = kik.kadastralekaart_kadastraleaanduiding(
        kadastralegemeente="Zundert",
        sectie="T",
        perceelnummer=1560,
        formaat=Formaat.JSON,
        klantreferentie="onbekend",
    )

    assert isinstance(response, KadastraleKaart)


@pytest.mark.asyncio
async def test_kadastraleaanduiding_async(akik: AsyncClient) -> None:
    response = await akik.kadastralekaart_kadastraleaanduiding(
        kadastralegemeente="Zundert",
        sectie="T",
        perceelnummer=1560,
        formaat=Formaat.JSON,
        klantreferentie="onbekend",
    )

    assert isinstance(response, KadastraleKaart)
