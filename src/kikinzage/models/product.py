from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from kikinzage.models.collectie import ATCollectie
from kikinzage.models.collectie import EDICollectie
from kikinzage.models.collectie import EGICollectie
from kikinzage.models.collectie import HPICollectie
from kikinzage.models.collectie import OICollectie
from kikinzage.models.collectie import OLPCollectie
from kikinzage.models.collectie import PTCollectie
from kikinzage.models.misc import NEN3610ID


class Product(BaseModel):
    actualiteitstijdstip_hypothecair: Optional[datetime] = Field(
        None, alias="actualiteitstijdstipHypothecair"
    )
    actualiteitstijdstip_kadastraal: Optional[datetime] = Field(
        None, alias="actualiteitstijdstipKadastraal"
    )
    klantreferentie: Optional[str] = Field(None, title="klantreferentie")
    productieordernummer: Optional[str] = Field(None, title="productieordernummer")
    signaleringstijdstip_beslagen: Optional[datetime] = Field(
        None, alias="signaleringstijdstipBeslagen"
    )
    signaleringstijdstip_hypothecair: Optional[datetime] = Field(
        None, alias="signaleringstijdstipHypothecair"
    )
    signaleringstijdstip_kadastraal: Optional[datetime] = Field(
        None, alias="signaleringstijdstipKadastraal"
    )
    tijdstip_samenstelling_bericht: Optional[datetime] = Field(
        None, alias="tijdstipSamenstellingBericht"
    )
    betreft: Optional[NEN3610ID] = None


class EigendomsinformatieProduct(Product):
    met: Optional[EDICollectie] = None


class DatuminformatieProduct(BaseModel):
    actualiteitstijdstip_hypothecair: Optional[datetime] = Field(
        None, alias="actualiteitstijdstipHypothecair"
    )
    actualiteitstijdstip_kadastraal: Optional[datetime] = Field(
        None, alias="actualiteitstijdstipKadastraal"
    )
    klantreferentie: Optional[str] = Field(None, title="klantreferentie")
    productieordernummer: Optional[str] = Field(None, title="productieordernummer")
    signaleringstijdstip_beslagen: Optional[datetime] = Field(
        None, alias="signaleringstijdstipBeslagen"
    )
    signaleringstijdstip_hypothecair: Optional[datetime] = Field(
        None, alias="signaleringstijdstipHypothecair"
    )
    signaleringstijdstip_kadastraal: Optional[datetime] = Field(
        None, alias="signaleringstijdstipKadastraal"
    )
    tijdstip_samenstelling_bericht: Optional[datetime] = Field(
        None, alias="tijdstipSamenstellingBericht"
    )


class MeldingProduct(BaseModel):
    nummer: Optional[str] = None
    tekst: Optional[str] = None


class NegatieveMededelingProduct(BaseModel):
    actualiteitstijdstip_hypothecair: Optional[datetime] = Field(
        None, alias="actualiteitstijdstipHypothecair"
    )
    actualiteitstijdstip_kadastraal: Optional[datetime] = Field(
        None, alias="actualiteitstijdstipKadastraal"
    )
    klantreferentie: Optional[str] = Field(None, title="klantreferentie")
    melding_negatieve_mededeling: Optional[str] = Field(
        None, alias="meldingNegatieveMededeling"
    )
    productieordernummer: Optional[str] = Field(None, title="productieordernummer")
    signaleringstijdstip_beslagen: Optional[datetime] = Field(
        None, alias="signaleringstijdstipBeslagen"
    )
    signaleringstijdstip_hypothecair: Optional[datetime] = Field(
        None, alias="signaleringstijdstipHypothecair"
    )
    signaleringstijdstip_kadastraal: Optional[datetime] = Field(
        None, alias="signaleringstijdstipKadastraal"
    )
    tijdstip_samenstelling_bericht: Optional[datetime] = Field(
        None, alias="tijdstipSamenstellingBericht"
    )


class HypotheekinformatieProduct(Product):
    met: Optional[HPICollectie] = None


class ObjectlijstPersoonProduct(Product):
    met: Optional[OLPCollectie] = None


class OvergegaanInProduct(Product):
    met: Optional[OICollectie] = None


class AdresTreffersProduct(Product):
    met: Optional[ATCollectie] = None


class EigenaarsinformatieProduct(Product):
    met: Optional[EGICollectie] = None


class PostcodeTreffersProduct(Product):
    met: Optional[PTCollectie] = None
