from typing import Any
from typing import Literal
from typing import Optional
from typing import Type
from typing import Union

import httpx
from httpx import USE_CLIENT_DEFAULT
from httpx._client import UseClientDefault

from .. import models
from ..models import Formaat
from ..models import ResponseType
from .base import KikinzageBaseClient


FormaatDefault: Literal["FormaatFormaatDefault"] = "FormaatFormaatDefault"
Klantreferentie: Literal["Klantreferentie"] = "Klantreferentie"


class AsyncClient(KikinzageBaseClient):
    """Client for async requests"""

    client: httpx.AsyncClient

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
        super().__init__(
            username=username,
            password=password,
            base_url=base_url,
            formaat=formaat,
            klantreferentie=klantreferentie,
            gebruikeridentificatie=gebruikeridentificatie,
            hyperlinkopproduct=hyperlinkopproduct,
            inkoopnummer=inkoopnummer,
            referentienummer=referentienummer,
        )

        httpx_kwargs.setdefault("base_url", base_url)
        httpx_kwargs.setdefault("auth", (self.username, self.password))

        self.client = self.create_client(**httpx_kwargs)

    def create_client(self, **httpx_kwargs: Any) -> httpx.AsyncClient:
        return httpx.AsyncClient(**httpx_kwargs)

    async def eigendomsinformatie_kadastraalobjectidentificatie_get(
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

        return await self.send(request, models.Eigendomsinformatie)

    async def send(
        self,
        request: httpx.Request,
        model: Type[ResponseType],
        status_code_success: int = 200,
    ) -> ResponseType:
        response = await self.client.send(request)

        return self.process_response(response, model, status_code_success)
