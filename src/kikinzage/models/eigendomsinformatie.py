from datetime import datetime
from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from .enum import AppartementsrechtSplitsingTypeEnum
from .enum import ObjectReferentieType
from .misc import NEN3610ID
from .misc import Bedrag
from .misc import TypeBreuk
from .misc import Waardelijst


class OnroerendeZaakBeperking(BaseModel):
    in_onderzoek: Optional[bool] = Field(None, alias="inOnderzoek")
    beperkt: Optional[NEN3610ID] = None


class VerkavelObject(BaseModel):
    betreft: Optional[NEN3610ID] = None
    ligt_in: Optional[NEN3610ID] = Field(None, alias="ligtIn")


class ZakelijkRecht(BaseModel):
    identificatie: Optional[NEN3610ID] = None
    aard: Optional[Waardelijst] = None
    toelichting_bewaarder: Optional[str] = Field(None, alias="toelichtingBewaarder")
    is_gebaseerd_op: Optional[List[NEN3610ID]] = Field(
        None, alias="isGebaseerdOp", min_length=0
    )
    is_vermeld_in: Optional[List[NEN3610ID]] = Field(
        None, alias="isVermeldIn", min_length=0
    )
    rust_op: Optional[NEN3610ID] = Field(None, alias="rustOp")
    is_belast_met: Optional[List[NEN3610ID]] = Field(
        None, alias="isBelastMet", min_length=0
    )
    is_ontstaan_uit: Optional[NEN3610ID] = Field(None, alias="isOntstaanUit")
    is_bestemd_tot: Optional[NEN3610ID] = Field(None, alias="isBestemdTot")
    is_betrokken_bij: Optional[NEN3610ID] = Field(None, alias="isBetrokkenBij")
    is_beperkt_tot: Optional[List[NEN3610ID]] = Field(
        None, alias="isBeperktTot", min_length=0
    )


class AppartementsrechtSplitsing(BaseModel):
    identificatie: Optional[NEN3610ID] = None
    type: Optional[AppartementsrechtSplitsingTypeEnum] = None
    is_vermeld_in: Optional[List[NEN3610ID]] = Field(
        None, alias="isVermeldIn", min_length=0
    )
    heeft_vereniging_van_eigenaren: Optional[NEN3610ID] = Field(
        None, alias="heeftVerenigingVanEigenaren"
    )
    is_gebaseerd_op: Optional[NEN3610ID] = Field(None, alias="isGebaseerdOp")


class GezamenlijkAandeel(BaseModel):
    identificatie: Optional[NEN3610ID] = None
    aandeel: Optional[TypeBreuk] = None


class Herverkavelingsgebied(BaseModel):
    identificatie: Optional[NEN3610ID] = None
    status_herverkavelingsproject: Optional[Waardelijst] = Field(
        None, alias="statusHerverkavelingsproject"
    )


class JaarlijksBedrag(BaseModel):
    bedrag: Optional[Bedrag] = None
    betreft_meer_onroerende_zaken: Optional[bool] = Field(
        None, alias="betreftMeerOnroerendeZaken"
    )


class Mandeligheid(BaseModel):
    identificatie: Optional[NEN3610ID] = None
    is_vermeld_in: Optional[List[NEN3610ID]] = Field(
        None, alias="isVermeldIn", min_length=0
    )
    is_gebaseerd_op: Optional[List[NEN3610ID]] = Field(None, alias="isGebaseerdOp")
    heeft_hoofdzaak: Optional[List[NEN3610ID]] = Field(None, alias="heeftHoofdzaak")


class ObjectReferentie(BaseModel):
    type: Optional[ObjectReferentieType] = None
    domein: Optional[str] = None
    identificatie_referentie: Optional[str] = Field(
        None, alias="identificatieReferentie"
    )


class PubliekrechtelijkeBeperking(BaseModel):
    identificatie: Optional[NEN3610ID] = None
    datum_beeindiging: Optional[datetime] = Field(None, alias="datumBeeindiging")
    datum_in_werking: Optional[datetime] = Field(None, alias="datumInWerking")
    grondslag: Optional[Waardelijst] = None
    is_gebaseerd_op: Optional[NEN3610ID] = Field(None, alias="isGebaseerdOp")
    is_vermeld_in: Optional[List[NEN3610ID]] = Field(None, alias="isVermeldIn")
    leidt_tot: Optional[List[OnroerendeZaakBeperking]] = Field(None, alias="leidtTot")
    bevoegd_gezag: Optional[NEN3610ID] = Field(None, alias="bevoegdGezag")
    heeft: Optional[NEN3610ID] = None


class Tenaamstelling(BaseModel):
    identificatie: Optional[NEN3610ID] = None
    aandeel: Optional[TypeBreuk] = None
    burgerlijke_staat_ten_tijde_van_verkrijging: Optional[Waardelijst] = Field(
        None, alias="burgerlijkeStaatTenTijdeVanVerkrijging"
    )
    omschrijving: Optional[str] = Field(None, max_length=50, min_length=1)
    verkregen_namens_samenwerkingsverband: Optional[Waardelijst] = Field(
        None, alias="verkregenNamensSamenwerkingsverband"
    )
    betrokken_partner: Optional[NEN3610ID] = Field(None, alias="betrokkenPartner")
    geldt_voor: Optional[NEN3610ID] = Field(None, alias="geldtVoor")
    is_vermeld_in: Optional[List[NEN3610ID]] = Field(
        None, alias="isVermeldIn", min_length=0
    )
    betrokken_samenwerkingsverband: Optional[NEN3610ID] = Field(
        None, alias="betrokkenSamenwerkingsverband"
    )
    betrokken_gorzen_en_aanwassen: Optional[NEN3610ID] = Field(
        None, alias="betrokkenGorzenEnAanwassen"
    )
    is_gebaseerd_op: Optional[List[NEN3610ID]] = Field(None, alias="isGebaseerdOp")
    van: Optional[NEN3610ID] = None
    ten_name_van: Optional[NEN3610ID] = Field(None, alias="tenNameVan")


class Beperkingsgebied(BaseModel):
    identificatie: Optional[NEN3610ID] = None
    ontleend_aan: Optional[List[ObjectReferentie]] = Field(None, alias="ontleendAan")


class Erfpachtcanon(BaseModel):
    einddatum_afkoop: Optional[datetime] = Field(None, alias="einddatumAfkoop")
    identificatie: Optional[NEN3610ID] = None
    indicatie_oude_onroerende_zaak_betrokken: Optional[bool] = Field(
        None, alias="indicatieOudeOnroerendeZaakBetrokken"
    )
    jaarlijks_bedrag: Optional[JaarlijksBedrag] = Field(None, alias="jaarlijksBedrag")
    soort: Optional[Waardelijst] = None
    betreft: Optional[NEN3610ID] = None
    is_gebaseerd_op: Optional[NEN3610ID] = Field(None, alias="isGebaseerdOp")
    is_vermeld_in: Optional[List[NEN3610ID]] = Field(
        None, alias="isVermeldIn", min_length=0
    )
