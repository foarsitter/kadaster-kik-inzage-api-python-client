from typing import Any
from typing import Dict
from typing import Optional

import httpx

from .. import models
from .base import BaseClient
from .utils import kwargs_as_params


class DefaultClient(BaseClient):
    """Synchronous client"""

    client: httpx.Client

    def __init__(
        self,
        username: str,
        password: str,
        base_url: str = "https://service10.kadaster.nl/kik-inzage-eto/v6/",
        **httpx_kwargs: Any,
    ):
        super().__init__(username, password, base_url)
        self.client = self.create_client(base_url, **httpx_kwargs)

    def create_client(self, base_url: str, **httpx_kwargs: Any) -> httpx.Client:
        httpx_kwargs.setdefault("base_url", base_url)
        httpx_kwargs.setdefault("auth", (self.username, self.password))
        return httpx.Client(**httpx_kwargs)

    def eigendomsinformatie_kadastraalobjectidentificatie_get(
        self,
        kadastraalobjectidentificatie: str,
        formaat: str,
        klantreferentie: str,
        gebruikeridentificatie: Optional[str] = None,
        hyperlinkopproduct: Optional[bool] = None,
        inkoopnummer: Optional[str] = None,
        referentienummer: Optional[str] = None,
    ) -> models.Eigendomsinformatie:
        """GET /eigendomsinformatie/kadastraalobjectidentificatie/{kadastraalobjectidentificatie}"""

        params: Dict[str, Any] = {
            "formaat": formaat,
            "klantreferentie": klantreferentie,
        }

        params.update(
            kwargs_as_params(
                gebruikeridentificatie=gebruikeridentificatie,
                hyperlinkopproduct=hyperlinkopproduct,
                inkoopnummer=inkoopnummer,
                referentienummer=referentienummer,
            )
        )

        response = self.client.get(
            f"eigendomsinformatie/kadastraalobjectidentificatie/{kadastraalobjectidentificatie}",
            params=params,
        )

        return self.process_response(response, models.Eigendomsinformatie)

    def eigendomsinformatie_kadastraleaanduiding_get(
        self,
        kadastralegemeente: str,
        sectie: str,
        perceelnummer: int,
        formaat: str,
        klantreferentie: str,
        appartementsrecht_volgnummer: Optional[int] = None,
        gebruikeridentificatie: Optional[str] = None,
        hyperlinkopproduct: Optional[bool] = None,
        inkoopnummer: Optional[str] = None,
        referentienummer: Optional[str] = None,
    ) -> models.Eigendomsinformatie:
        params: Dict[str, Any] = {
            "kadastralegemeente": kadastralegemeente,
            "sectie": sectie,
            "perceelnummer": perceelnummer,
            "formaat": formaat,
            "klantreferentie": klantreferentie,
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

        response = self.client.get(
            f"/eigendomsinformatie/kadastraleaanduiding/{kadastralegemeente}/{sectie}/{perceelnummer}",
            params=params,
        )

        return self.process_response(response, models.Eigendomsinformatie)

    def eigendomsinformatie_postcode_get(
        self,
        postcode: str,
        huisnummer: str,
        formaat: str,
        klantreferentie: str,
        huisletter: Optional[str] = None,
        huisnummertoevoeging: Optional[str] = None,
        gebruikeridentificatie: Optional[str] = None,
        hyperlinkopproduct: Optional[bool] = None,
        inkoopnummer: Optional[str] = None,
        referentienummer: Optional[str] = None,
    ) -> models.Eigendomsinformatie:
        params = {
            "formaat": formaat,
            "klantreferentie": klantreferentie,
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

        response = self.client.get(
            f"eigendomsinformatie/postcode/{postcode}/{huisnummer}",
            params=params,
        )

        return self.process_response(response, models.Eigendomsinformatie)

    def eigendomsinformatie_adres_get(
        self,
        plaatsnaam: str,
        straatnaam: str,
        huisnummer: int,
        formaat: str,
        klantreferentie: str,
        huisletter: str = None,
        gebruikeridentificatie: Optional[str] = None,
        hyperlinkopproduct: Optional[bool] = None,
        inkoopnummer: Optional[str] = None,
        referentienummer: Optional[str] = None,
    ) -> models.Eigendomsinformatie:
        params = {
            "formaat": formaat,
            "klantreferentie": klantreferentie,
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
        response = self.client.get(
            f"/eigendomsinformatie/adres/{plaatsnaam}/{straatnaam}/{huisnummer}",
            params=params,
        )

        return self.process_response(response, models.Eigendomsinformatie)
