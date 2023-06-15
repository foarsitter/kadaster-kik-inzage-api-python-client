from types import TracebackType
from typing import Any
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


class AsyncClient(KikinzageBaseClient):
    """Client for async requests"""

    client: httpx.AsyncClient

    async def __aenter__(self) -> "AsyncClient":
        await self.client.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        traceback: Optional[TracebackType] = None,
    ) -> None:
        await self.client.__aexit__(exc_type, exc_value, traceback)

    def create_client(self, **httpx_kwargs: Any) -> httpx.AsyncClient:
        return httpx.AsyncClient(**httpx_kwargs)

    async def send(
        self,
        request: httpx.Request,
        model: Type[ResponseType],
        status_code_success: int = 200,
    ) -> ResponseType:
        response = await self.client.send(request)

        return self.process_response(response, model, status_code_success)

    async def eigendomsinformatie_kadastraalobjectidentificatie(
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
