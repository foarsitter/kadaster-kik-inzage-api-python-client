from abc import ABC
from json import JSONDecodeError
from typing import Any
from typing import Dict
from typing import Optional
from typing import Type
from typing import Union

import httpx
from httpx import USE_CLIENT_DEFAULT
from httpx import Request
from httpx._client import BaseClient
from httpx._client import UseClientDefault

from ..models import ResponseType
from ..models.enum import Formaat
from . import errors
from .utils import kwargs_as_params


class KikinzageBaseClient(ABC):
    """Class with method shared between async and default client"""

    ERROR_RESPONSE_MAPPING: Dict[int, Type[errors.KIKRequestError]] = {
        422: errors.KIKValidationError,
        401: errors.KIKAuthenticationError,
        403: errors.KIKAuthenticationError,
        404: errors.KIKNotFoundError,
        400: errors.KIKValidationError,
        500: errors.KIKServerError,
    }

    client: BaseClient

    def __init__(
        self,
        username: str,
        password: str,
        base_url: str = "https://service10.kadaster.nl/kik-inzage-eto/v6/",
        formaat: Formaat = Formaat.JSON,
        klantreferentie: Optional[str] = None,
        gebruikeridentificatie: Optional[str] = None,
        hyperlinkopproduct: Optional[bool] = None,
        inkoopnummer: Optional[str] = None,
        referentienummer: Optional[str] = None,
        **httpx_kwargs: Any,
    ) -> None:
        self.klantreferentie = klantreferentie
        self.username = username
        self.password = password
        self.base_url = base_url
        self.formaat = formaat
        self.gebruikeridentificatie = gebruikeridentificatie
        self.hyperlinkopproduct = hyperlinkopproduct
        self.inkoopnummer = inkoopnummer
        self.referentienummer = referentienummer

        httpx_kwargs.setdefault("base_url", base_url)
        httpx_kwargs.setdefault("auth", (self.username, self.password))

        self.client = self.create_client(**httpx_kwargs)

    def create_client(self, **httpx_kwargs: Any) -> BaseClient:
        raise NotImplementedError

    def process_response(
        self,
        response: httpx.Response,
        model: Type[ResponseType],
        status_code_success: int = 200,
    ) -> ResponseType:
        try:
            if response.status_code == status_code_success:
                response_json = response.json()
                return model(**response_json)
            else:
                raise self.create_error(response)
        except JSONDecodeError as e:
            raise errors.KIKServerError(
                "Invalid json from server", status_code=400
            ) from e

    def create_error(self, response: httpx.Response) -> errors.KIKRequestError:
        try:
            response_json = response.json()
        except JSONDecodeError:
            response_json = {"message": response.text}

        response_json["status_code"] = response.status_code

        exception_type = self.map_exception(response)
        return exception_type(
            status_code=response.status_code,
            json=response_json,
            message="Error from server",
        )

    def map_exception(self, response: httpx.Response) -> Type[errors.KIKRequestError]:
        exception_type = self.ERROR_RESPONSE_MAPPING.get(
            response.status_code, errors.KIKRequestError
        )
        return exception_type

    def _get_klantreferentie(
        self, klantreferentie: Union[str, UseClientDefault]
    ) -> str:
        if isinstance(klantreferentie, str):
            return klantreferentie
        elif self.klantreferentie is not None:
            return self.klantreferentie

        raise errors.KIKError(
            "`klantreferentie` is required, pass it as parameter or set `self.klantreferentie`"
        )

    def _get_formaat(self, formaat: Union[Formaat, UseClientDefault]) -> str:
        return formaat.value if isinstance(formaat, Formaat) else self.formaat.value

    def request_eigendomsinformatie_kadastraleaanduiding(
        self,
        kadastralegemeente: str,
        sectie: str,
        perceelnummer: int,
        appartementsrecht_volgnummer: Optional[int] = None,
        *,
        formaat: Union[Formaat, UseClientDefault] = USE_CLIENT_DEFAULT,
        klantreferentie: Union[str, UseClientDefault] = USE_CLIENT_DEFAULT,
        gebruikeridentificatie: Optional[str] = None,
        hyperlinkopproduct: Optional[bool] = None,
        inkoopnummer: Optional[str] = None,
        referentienummer: Optional[str] = None,
    ) -> Request:
        params: Dict[str, Any] = {
            "formaat": self._get_formaat(formaat),
            "klantreferentie": self._get_klantreferentie(klantreferentie),
        }

        params.update(
            kwargs_as_params(
                appartementsrechtVolgnummer=appartementsrecht_volgnummer,
                gebruikeridentificatie=gebruikeridentificatie,
                hyperlinkopproduct=hyperlinkopproduct,
                inkoopnummer=inkoopnummer,
                referentienummer=referentienummer,
            )
        )

        request = self.client.build_request(
            method="GET",
            url=f"/eigendomsinformatie/kadastraleaanduiding/{kadastralegemeente}/{sectie}/{perceelnummer}",
            params=params,
        )

        return request

    def request_eigendomsinformatie_kadastraalobjectidentificatie(
        self,
        kadastraalobjectidentificatie: str,
        *,
        formaat: Union[Formaat, UseClientDefault] = USE_CLIENT_DEFAULT,
        klantreferentie: Union[str, UseClientDefault] = USE_CLIENT_DEFAULT,
        gebruikeridentificatie: Optional[str] = None,
        hyperlinkopproduct: Optional[bool] = None,
        inkoopnummer: Optional[str] = None,
        referentienummer: Optional[str] = None,
    ) -> Request:
        """GET /eigendomsinformatie/kadastraalobjectidentificatie/{kadastraalobjectidentificatie}"""

        params: Dict[str, Any] = {
            "formaat": self._get_formaat(formaat),
            "klantreferentie": self._get_klantreferentie(klantreferentie),
        }

        params.update(
            kwargs_as_params(
                gebruikeridentificatie=gebruikeridentificatie
                or self.gebruikeridentificatie,
                hyperlinkopproduct=hyperlinkopproduct or self.hyperlinkopproduct,
                inkoopnummer=inkoopnummer or self.inkoopnummer,
                referentienummer=referentienummer or self.referentienummer,
            )
        )

        request = self.client.build_request(
            method="GET",
            url=f"eigendomsinformatie/kadastraalobjectidentificatie/{kadastraalobjectidentificatie}",
            params=params,
        )

        return request

    def request_eigendomsinformatie_postcode(
        self,
        postcode: str,
        huisnummer: int,
        huisletter: Optional[str] = None,
        huisnummertoevoeging: Optional[str] = None,
        *,
        formaat: Union[Formaat, UseClientDefault] = USE_CLIENT_DEFAULT,
        klantreferentie: Union[str, UseClientDefault] = USE_CLIENT_DEFAULT,
        gebruikeridentificatie: Optional[str] = None,
        hyperlinkopproduct: Optional[bool] = None,
        inkoopnummer: Optional[str] = None,
        referentienummer: Optional[str] = None,
    ) -> Request:
        """GET /eigendomsinformatie/postcode/{postcode}/{huisnummer}"""
        params: Dict[str, Any] = {
            "formaat": self._get_formaat(formaat),
            "klantreferentie": self._get_klantreferentie(klantreferentie),
        }

        params.update(
            kwargs_as_params(
                huisletter=huisletter,
                huisnummertoevoeging=huisnummertoevoeging,
                gebruikeridentificatie=gebruikeridentificatie,
                hyperlinkopproduct=hyperlinkopproduct,
                inkoopnummer=inkoopnummer,
                referentienummer=referentienummer,
            )
        )

        response = self.client.build_request(
            method="GET",
            url=f"eigendomsinformatie/postcode/{postcode}/{huisnummer}",
            params=params,
        )
        return response

    def request_eigendomsinformatie_adres(
        self,
        plaatsnaam: str,
        straatnaam: str,
        huisnummer: int,
        huisletter: Optional[str] = None,
        *,
        formaat: Union[Formaat, UseClientDefault] = USE_CLIENT_DEFAULT,
        klantreferentie: Union[str, UseClientDefault] = USE_CLIENT_DEFAULT,
        gebruikeridentificatie: Optional[str] = None,
        hyperlinkopproduct: Optional[bool] = None,
        inkoopnummer: Optional[str] = None,
        referentienummer: Optional[str] = None,
    ) -> Request:
        params: Dict[str, Any] = {
            "formaat": self._get_formaat(formaat),
            "klantreferentie": self._get_klantreferentie(klantreferentie),
        }
        params.update(
            kwargs_as_params(
                huisletter=huisletter,
                gebruikeridentificatie=gebruikeridentificatie,
                hyperlinkopproduct=hyperlinkopproduct,
                inkoopnummer=inkoopnummer,
                referentienummer=referentienummer,
            )
        )

        request = self.client.build_request(
            method="GET",
            url=f"eigendomsinformatie/adres/{plaatsnaam}/{straatnaam}/{huisnummer}",
            params=params,
        )

        return request
