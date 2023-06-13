import httpx
import pytest
from respx import MockRouter

from kikinzage.client import errors
from kikinzage.client.default import DefaultClient
from kikinzage.client.errors import KIKAuthenticationError
from kikinzage.models import SeverityCode


def test_401() -> None:
    kik = DefaultClient(username="", password="")  # nosec

    with pytest.raises(KIKAuthenticationError):
        kik.eigendomsinformatie_kadastraalobjectidentificatie_get(
            kadastraalobjectidentificatie="",
            formaat="json",
            klantreferentie="onbekend",
        )


def test_postcode(kik: DefaultClient) -> None:
    response = kik.eigendomsinformatie_postcode_get(
        postcode="4884ME",
        huisnummer="16",
        formaat="json",
        klantreferentie="onbekend",
        huisnummertoevoeging="K298",
    )
    assert response.proces
    assert response.proces.severity_code == SeverityCode.INFO
    assert response.product_gegevens
    assert response.product_gegevens.klantreferentie == "onbekend"


def test_kadastraalobjectidentificatie(kik: DefaultClient) -> None:
    response = kik.eigendomsinformatie_kadastraalobjectidentificatie_get(
        kadastraalobjectidentificatie="11010156070000",
        formaat="json",
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


def test_kadastraleaanduiding(kik: DefaultClient) -> None:
    response = kik.eigendomsinformatie_kadastraleaanduiding_get(
        kadastralegemeente="Zundert",
        sectie="T",
        perceelnummer=1560,
        formaat="json",
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


def test_invalid_json(kik: DefaultClient, respx_mock: MockRouter) -> None:
    respx_mock.get() % httpx.Response(200, content="this is not valid")
    with pytest.raises(errors.KIKError):
        kik.eigendomsinformatie_kadastraalobjectidentificatie_get(
            kadastraalobjectidentificatie="11010156070000",
            formaat="json",
            klantreferentie="onbekend",
        )


def test_adres(kik: DefaultClient):
    response = kik.eigendomsinformatie_adres_get(
        plaatsnaam="Wernhout",
        straatnaam="Kleine Heistraat",
        huisnummer=16,
        formaat="json",
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
