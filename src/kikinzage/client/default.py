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

    def hypotheekinformatie_kadastraalobjectidentificatie(
        self,
        kadastraalobjectidentificatie: str,
        *,
        formaat: Union[Formaat, UseClientDefault] = USE_CLIENT_DEFAULT,
        klantreferentie: Union[str, UseClientDefault] = USE_CLIENT_DEFAULT,
        gebruikeridentificatie: Optional[str] = None,
        hyperlinkopproduct: Optional[bool] = None,
        inkoopnummer: Optional[str] = None,
        referentienummer: Optional[str] = None,
    ) -> models.Hypotheekinformatie:
        request = self.request_hypotheekinformatie_kadastraalobjectidentificatie(
            kadastraalobjectidentificatie=kadastraalobjectidentificatie,
            formaat=formaat,
            klantreferentie=klantreferentie,
            gebruikeridentificatie=gebruikeridentificatie,
            hyperlinkopproduct=hyperlinkopproduct,
            inkoopnummer=inkoopnummer,
            referentienummer=referentienummer,
        )

        return self.send(request, models.Hypotheekinformatie)

    def hypotheekinformatie_kadastraleaanduiding(
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
    ) -> models.Hypotheekinformatie:
        request = self.request_hypotheekinformatie_kadastraleaanduiding(
            kadastralegemeente=kadastralegemeente,
            sectie=sectie,
            perceelnummer=perceelnummer,
            appartementsrecht_volgnummer=appartementsrecht_volgnummer,
            formaat=formaat,
            klantreferentie=klantreferentie,
            gebruikeridentificatie=gebruikeridentificatie,
            hyperlinkopproduct=hyperlinkopproduct,
            inkoopnummer=inkoopnummer,
            referentienummer=referentienummer,
        )

        return self.send(request, models.Hypotheekinformatie)

    def hypotheekinformatie_postcode(
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
    ) -> models.Hypotheekinformatie:
        request = self.request_hypotheekinformatie_postcode(
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

        return self.send(request, models.Hypotheekinformatie)

    def eigenaarsinformatie_burgerservicenummer(
        self,
        burgerservicenummer: str,
        *,
        formaat: Union[Formaat, UseClientDefault] = USE_CLIENT_DEFAULT,
        klantreferentie: Union[str, UseClientDefault] = USE_CLIENT_DEFAULT,
        gebruikeridentificatie: Optional[str] = None,
        hyperlinkopproduct: Optional[bool] = None,
        inkoopnummer: Optional[str] = None,
        referentienummer: Optional[str] = None,
    ) -> models.Eigenaarsinformatie:
        request = self.request_eigenaarsinformatie_burgerservicenummer(
            burgerservicenummer=burgerservicenummer,
            formaat=formaat,
            klantreferentie=klantreferentie,
            gebruikeridentificatie=gebruikeridentificatie,
            hyperlinkopproduct=hyperlinkopproduct,
            inkoopnummer=inkoopnummer,
            referentienummer=referentienummer,
        )

        return self.send(request, models.Eigenaarsinformatie)

    def eigenaarsinformatie_kadastraalpersoonidentificatie(
        self,
        kadastraalpersoonidentificatie: str,
        *,
        formaat: Union[Formaat, UseClientDefault] = USE_CLIENT_DEFAULT,
        klantreferentie: Union[str, UseClientDefault] = USE_CLIENT_DEFAULT,
        gebruikeridentificatie: Optional[str] = None,
        hyperlinkopproduct: Optional[bool] = None,
        inkoopnummer: Optional[str] = None,
        referentienummer: Optional[str] = None,
    ) -> models.Eigenaarsinformatie:
        request = self.request_eigenaarsinformatie_kadastraalpersoonidentificatie(
            kadastraalpersoonidentificatie=kadastraalpersoonidentificatie,
            formaat=formaat,
            klantreferentie=klantreferentie,
            gebruikeridentificatie=gebruikeridentificatie,
            hyperlinkopproduct=hyperlinkopproduct,
            inkoopnummer=inkoopnummer,
            referentienummer=referentienummer,
        )

        return self.send(request, models.Eigenaarsinformatie)

    def objectlijstpersoon_burgerservicenummer(
        self,
        burgerservicenummer: str,
        *,
        formaat: Union[Formaat, UseClientDefault] = USE_CLIENT_DEFAULT,
        klantreferentie: Union[str, UseClientDefault] = USE_CLIENT_DEFAULT,
        gebruikeridentificatie: Optional[str] = None,
        hyperlinkopproduct: Optional[bool] = None,
        inkoopnummer: Optional[str] = None,
        referentienummer: Optional[str] = None,
    ) -> models.ObjectlijstPersoon:
        request = self.request_objectlijstpersoon_burgerservicenummer(
            burgerservicenummer=burgerservicenummer,
            formaat=formaat,
            klantreferentie=klantreferentie,
            gebruikeridentificatie=gebruikeridentificatie,
            hyperlinkopproduct=hyperlinkopproduct,
            inkoopnummer=inkoopnummer,
            referentienummer=referentienummer,
        )

        return self.send(request, models.ObjectlijstPersoon)

    def objectlijstpersoon_kadastraalpersoonidentificatie(
        self,
        kadastraalpersoonidentificatie: str,
        *,
        formaat: Union[Formaat, UseClientDefault] = USE_CLIENT_DEFAULT,
        klantreferentie: Union[str, UseClientDefault] = USE_CLIENT_DEFAULT,
        gebruikeridentificatie: Optional[str] = None,
        hyperlinkopproduct: Optional[bool] = None,
        inkoopnummer: Optional[str] = None,
        referentienummer: Optional[str] = None,
    ) -> models.ObjectlijstPersoon:
        request = self.request_objectlijstpersoon_kadastraalpersoonidentificatie(
            kadastraalpersoonidentificatie=kadastraalpersoonidentificatie,
            formaat=formaat,
            klantreferentie=klantreferentie,
            gebruikeridentificatie=gebruikeridentificatie,
            hyperlinkopproduct=hyperlinkopproduct,
            inkoopnummer=inkoopnummer,
            referentienummer=referentienummer,
        )

        return self.send(request, models.ObjectlijstPersoon)

    def brondocument(
        self,
        soort_register: str,
        register_code: str,
        deel: str,
        nummer: str,
        *,
        klantreferentie: Union[str, UseClientDefault] = USE_CLIENT_DEFAULT,
        gebruikeridentificatie: Optional[str] = None,
        hyperlinkopproduct: Optional[bool] = None,
        inkoopnummer: Optional[str] = None,
        referentienummer: Optional[str] = None,
    ) -> models.Brondocument:
        request = self.request_brondocument(
            soort_register=soort_register,
            register_code=register_code,
            deel=deel,
            nummer=nummer,
            klantreferentie=klantreferentie,
            gebruikeridentificatie=gebruikeridentificatie,
            hyperlinkopproduct=hyperlinkopproduct,
            inkoopnummer=inkoopnummer,
            referentienummer=referentienummer,
        )

        return self.send(request, models.Brondocument)

    def kadastralekaart_kadastraalobjectidentificatie(
        self,
        kadastraalobjectidentificatie: str,
        formaat: Union[Formaat, UseClientDefault] = USE_CLIENT_DEFAULT,
        klantreferentie: Union[str, UseClientDefault] = USE_CLIENT_DEFAULT,
        gebruikeridentificatie: Optional[str] = None,
        hyperlinkopproduct: Optional[bool] = None,
        inkoopnummer: Optional[str] = None,
        referentienummer: Optional[str] = None,
    ) -> models.KadastraleKaart:
        request = self.request_kadastralekaart_kadastraalobjectidentificatie(
            kadastraalobjectidentificatie=kadastraalobjectidentificatie,
            formaat=formaat,
            klantreferentie=klantreferentie,
            gebruikeridentificatie=gebruikeridentificatie,
            hyperlinkopproduct=hyperlinkopproduct,
            inkoopnummer=inkoopnummer,
            referentienummer=referentienummer,
        )

        return self.send(request, models.KadastraleKaart)

    def kadastralekaart_kadastraleaanduiding(
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
    ) -> models.KadastraleKaart:
        request = self.request_kadastralekaart_kadastraleaanduiding(
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

        return self.send(request, models.KadastraleKaart)

    def kadastralekaart_postcode(
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
    ) -> models.KadastraleKaart:
        request = self.request_kadastralekaart_postcode(
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

        return self.send(request, models.KadastraleKaart)

    def datuminformatie(
        self,
        klantreferentie: Union[str, UseClientDefault] = USE_CLIENT_DEFAULT,
        *,
        gebruikeridentificatie: Optional[str] = None,
        inkoopnummer: Optional[str] = None,
        referentienummer: Optional[str] = None,
    ) -> models.Datuminformatie:
        request = self.request_datuminformatie(
            klantreferentie=klantreferentie,
            gebruikeridentificatie=gebruikeridentificatie,
            inkoopnummer=inkoopnummer,
            referentienummer=referentienummer,
        )

        return self.send(request, models.Datuminformatie)
