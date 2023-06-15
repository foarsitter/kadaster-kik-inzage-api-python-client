import pytest
from httpx import USE_CLIENT_DEFAULT

from kikinzage.client import DefaultClient
from kikinzage.client import KikinzageBaseClient
from kikinzage.client.errors import KIKError


def test_get_klantreferentie() -> None:
    kik = DefaultClient(password="password", username="username")  # nosec

    with pytest.raises(KIKError):
        kik._get_klantreferentie(USE_CLIENT_DEFAULT)

    kik.klantreferentie = "klantreferentie"

    assert kik._get_klantreferentie(USE_CLIENT_DEFAULT) == "klantreferentie"


def test_abstract_client_factory() -> None:
    with pytest.raises(NotImplementedError):
        KikinzageBaseClient("", "")
