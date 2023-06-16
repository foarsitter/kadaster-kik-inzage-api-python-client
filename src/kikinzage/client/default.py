from typing import Any
from typing import Optional
from typing import Type
from typing import Union

import httpx
from httpx._client import USE_CLIENT_DEFAULT
from httpx._client import UseClientDefault

from .. import models
from ..models import ResponseType
from ..models.enum import Formaat
from .base import KikinzageBaseClient


class DefaultClient(KikinzageBaseClient):
    """Synchronous client"""

    client: httpx.Client

    def create_client(self, **httpx_kwargs: Any) -> httpx.Client:
        return httpx.Client(**httpx_kwargs)

    def send(
        self,
        request: httpx.Request,
        model: Type[ResponseType],
        status_code_success: int = 200,
    ) -> ResponseType:
        response = self.client.send(request)

        return self.process_response(response, model, status_code_success)

    def eigendomsinformatie_kadastraalobjectidentificatie(
        self,
        kadastraalobjectidentificatie: str,
        formaat: Union[Formaat, UseClientDefault] = USE_CLIENT_DEFAULT,
        klantreferentie: Union[str, UseClientDefault] = USE_CLIENT_DEFAULT,
        gebruikeridentificatie: Optional[str] = None,
        hyperlinkopproduct: Optional[bool] = None,
        inkoopnummer: Optional[str] = None,
        referentienummer: Optional[str] = None,
    ) -> models.Eigendomsinformatie:
        """GET /eigendomsinformatie/kadastraalobjectidentificatie/{kadastraalobjectidentificatie}"""

        request = self.request_eigendomsinformatie_kadastraalobjectidentificatie(
            kadastraalobjectidentificatie=kadastraalobjectidentificatie,
            formaat=formaat,
            klantreferentie=klantreferentie,
            gebruikeridentificatie=gebruikeridentificatie,
            hyperlinkopproduct=hyperlinkopproduct,
            inkoopnummer=inkoopnummer,
            referentienummer=referentienummer,
        )

        return self.send(request, models.Eigendomsinformatie)

    def eigendomsinformatie_kadastraleaanduiding(
        self,
        kadastralegemeente: str,
        sectie: str,
        perceelnummer: int,
        appartementsrecht_volgnummer: Optional[int] = None,
        formaat: Union[Formaat, UseClientDefault] = USE_CLIENT_DEFAULT,
        klantreferentie: Union[str, UseClientDefault] = USE_CLIENT_DEFAULT,
        gebruikeridentificatie: Optional[str] = None,
        hyperlinkopproduct: Optional[bool] = None,
        inkoopnummer: Optional[str] = None,
        referentienummer: Optional[str] = None,
    ) -> models.Eigendomsinformatie:
        request = self.request_eigendomsinformatie_kadastraleaanduiding(
            kadastralegemeente=kadastralegemeente,
            sectie=sectie,
            perceelnummer=perceelnummer,
            formaat=formaat,
            klantreferentie=klantreferentie,
            appartementsrecht_volgnummer=appartementsrecht_volgnummer,
            gebruikeridentificatie=gebruikeridentificatie,
            hyperlinkopproduct=hyperlinkopproduct,
            inkoopnummer=inkoopnummer,
            referentienummer=referentienummer,
        )

        return self.send(request, models.Eigendomsinformatie)

    def eigendomsinformatie_postcode(
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
    ) -> models.Eigendomsinformatie:
        request = self.request_eigendomsinformatie_postcode(
            postcode=postcode,
            huisnummer=huisnummer,
            huisletter=huisletter,
            huisnummertoevoeging=huisnummertoevoeging,
            formaat=formaat,
            klantreferentie=klantreferentie,
            gebruikeridentificatie=gebruikeridentificatie,
            hyperlinkopproduct=hyperlinkopproduct,
            inkoopnummer=inkoopnummer,
            referentienummer=referentienummer,
        )

        return self.send(request, models.Eigendomsinformatie)

    def eigendomsinformatie_adres(
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
    ) -> models.Eigendomsinformatie:
        request = self.request_eigendomsinformatie_adres(
            plaatsnaam=plaatsnaam,
            straatnaam=straatnaam,
            huisnummer=huisnummer,
            huisletter=huisletter,
            formaat=formaat,
            klantreferentie=klantreferentie,
            gebruikeridentificatie=gebruikeridentificatie,
            hyperlinkopproduct=hyperlinkopproduct,
            inkoopnummer=inkoopnummer,
            referentienummer=referentienummer,
        )

        return self.send(request, models.Eigendomsinformatie)
