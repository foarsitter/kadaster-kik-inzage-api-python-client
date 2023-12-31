from typing import Optional

import pytest

from kikinzage.client import AsyncClient
from kikinzage.client.default import DefaultClient
from kikinzage.models import Eigendomsinformatie
from kikinzage.models import Formaat
from kikinzage.models import SeverityCode


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
    response = kik.eigendomsinformatie_postcode(
        postcode=postcode,
        huisnummer=huisnummer,
        huisletter=huisletter,
        huisnummertoevoeging=huisnummertoevoeging,
        formaat=Formaat.JSON,
        klantreferentie="onbekend",
    )
    assert response.proces
    assert response.proces.severity_code == SeverityCode.INFO

    assert response.product_gegevens
    assert response.product_gegevens.klantreferentie == "onbekend"
    assert response.geleverd_product
    assert response.geleverd_product.pdf is None


def test_postcode_pdf(kik: DefaultClient) -> None:
    response = kik.eigendomsinformatie_postcode(
        postcode="4884ME",
        huisnummer=16,
        formaat=Formaat.PDF,
        klantreferentie="onbekend",
        huisnummertoevoeging="K298",
    )
    assert response.proces
    assert response.proces.severity_code == SeverityCode.INFO

    assert response.product_gegevens
    assert response.product_gegevens.klantreferentie == "onbekend"

    assert response.geleverd_product
    assert response.geleverd_product.pdf is not None


@pytest.mark.asyncio
async def test_postcode_pdf_async(akik: AsyncClient) -> None:
    response = await akik.eigendomsinformatie_postcode(
        postcode="4884ME",
        huisnummer=16,
        formaat=Formaat.JSON,
        klantreferentie="onbekend",
        huisnummertoevoeging="K298",
    )
    assert isinstance(response, Eigendomsinformatie)


def test_kadastraalobjectidentificatie(kik: DefaultClient) -> None:
    response = kik.eigendomsinformatie_kadastraalobjectidentificatie(
        kadastraalobjectidentificatie="11010156070000",
        formaat=Formaat.JSON,
        klantreferentie="onbekend",
    )

    assert response.product_gegevens
    assert response.proces
    assert response.proces.meldingen is not None
    assert len(response.proces.meldingen) > 0
    assert response.proces.meldingen[0].severity_code == SeverityCode.INFO
    assert (
        response.proces.meldingen[0].omschrijving
        == "Gevraagde product is succesvol geleverd."
    )


@pytest.mark.asyncio
async def test_kadastraalobjectidentificatie_async(akik: AsyncClient) -> None:
    response = await akik.eigendomsinformatie_kadastraalobjectidentificatie(
        kadastraalobjectidentificatie="11010156070000",
        formaat=Formaat.JSON,
        klantreferentie="onbekend",
    )

    assert isinstance(response, Eigendomsinformatie)


def test_kadastraleaanduiding(kik: DefaultClient) -> None:
    response = kik.eigendomsinformatie_kadastraleaanduiding(
        kadastralegemeente="Zundert",
        sectie="T",
        perceelnummer=1560,
        formaat=Formaat.JSON,
        klantreferentie="onbekend",
    )

    assert response.product_gegevens
    assert response.proces
    assert response.proces.meldingen is not None
    assert len(response.proces.meldingen) > 0
    assert response.proces.meldingen[0].severity_code == SeverityCode.INFO
    assert (
        response.proces.meldingen[0].omschrijving
        == "Gevraagde product is succesvol geleverd."
    )
    assert response.geleverd_product
    assert response.geleverd_product.product
    assert response.geleverd_product.product.met
    assert response.geleverd_product.product.met.onroerende_zaken
    assert len(response.geleverd_product.product.met.onroerende_zaken) > 0

    zaak = response.geleverd_product.product.met.onroerende_zaken[0]

    assert zaak
    assert zaak.kadastrale_aanduiding
    assert zaak.kadastrale_aanduiding.kadastrale_gemeente
    assert zaak.kadastrale_aanduiding.kadastrale_gemeente.waarde

    assert zaak.kadastrale_aanduiding.kadastrale_gemeente.waarde == "Zundert"


@pytest.mark.asyncio
async def test_kadastraleaanduiding_async(akik: AsyncClient) -> None:
    response = await akik.eigendomsinformatie_kadastraleaanduiding(
        kadastralegemeente="Zundert",
        sectie="T",
        perceelnummer=1560,
        formaat=Formaat.JSON,
        klantreferentie="onbekend",
    )

    assert isinstance(response, Eigendomsinformatie)


def test_adres(kik: DefaultClient) -> None:
    response = kik.eigendomsinformatie_adres(
        plaatsnaam="Wernhout",
        straatnaam="Kleine Heistraat",
        huisnummer=16,
        formaat=Formaat.JSON,
        klantreferentie="onbekend",
    )

    assert response.product_gegevens
    assert response.proces
    assert response.proces.meldingen is not None
    assert len(response.proces.meldingen) > 0
    assert response.proces.meldingen[0].severity_code == SeverityCode.INFO
    assert (
        response.proces.meldingen[0].omschrijving
        == "Gevraagde product is succesvol geleverd."
    )


@pytest.mark.asyncio
async def test_adres_async(akik: AsyncClient) -> None:
    response = await akik.eigendomsinformatie_adres(
        plaatsnaam="Wernhout",
        straatnaam="Kleine Heistraat",
        huisnummer=16,
        formaat=Formaat.JSON,
        klantreferentie="onbekend",
    )

    assert isinstance(response, Eigendomsinformatie)
