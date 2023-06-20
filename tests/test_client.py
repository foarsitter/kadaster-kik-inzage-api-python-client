import httpx
import pytest
from httpx import USE_CLIENT_DEFAULT
from respx import MockRouter

from kikinzage.client import DefaultClient
from kikinzage.client import KikinzageBaseClient
from kikinzage.client import errors
from kikinzage.client.errors import KIKAuthenticationError
from kikinzage.client.errors import KIKError
from kikinzage.models import Formaat


def test_get_klantreferentie() -> None:
    kik = DefaultClient(password="password", username="username")  # nosec

    with pytest.raises(KIKError):
        kik._get_klantreferentie(USE_CLIENT_DEFAULT)

    kik.klantreferentie = "klantreferentie"

    assert kik._get_klantreferentie(USE_CLIENT_DEFAULT) == "klantreferentie"


def test_abstract_client_factory() -> None:
    with pytest.raises(NotImplementedError):
        KikinzageBaseClient("", "")


def test_401() -> None:
    kik = DefaultClient(username="", password="")  # nosec

    with pytest.raises(KIKAuthenticationError):
        kik.eigendomsinformatie_kadastraalobjectidentificatie(
            kadastraalobjectidentificatie="",
            formaat=Formaat.JSON,
            klantreferentie="onbekend",
        )


def test_invalid_json(kik: DefaultClient, respx_mock: MockRouter) -> None:
    respx_mock.get() % httpx.Response(200, content="this is not valid")
    with pytest.raises(errors.KIKRequestError):
        kik.eigendomsinformatie_kadastraalobjectidentificatie(
            kadastraalobjectidentificatie="11010156070000",
            formaat=Formaat.JSON,
            klantreferentie="onbekend",
        )
