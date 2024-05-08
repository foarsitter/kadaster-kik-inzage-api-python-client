from datetime import datetime
from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from .adres import AdresType
from .adres import FieldAdresLocatie
from .eigendomsinformatie import AppartementsrechtSplitsing
from .eigendomsinformatie import Beperkingsgebied
from .eigendomsinformatie import Erfpachtcanon
from .eigendomsinformatie import GezamenlijkAandeel
from .eigendomsinformatie import Herverkavelingsgebied
from .eigendomsinformatie import Mandeligheid
from .eigendomsinformatie import PubliekrechtelijkeBeperking
from .eigendomsinformatie import Tenaamstelling
from .eigendomsinformatie import VerkavelObject
from .eigendomsinformatie import ZakelijkRecht
from .enum import OnroerendeZaakTypeEnum
from .misc import NEN3610ID
from .misc import Bedrag
from .misc import Waardelijst
from .persoon import PersoonType
from .stukken import FieldType
from .zekerheid import FieldZekerheidsstelling


class Aantekening(BaseModel):
    identificatie: Optional[NEN3610ID] = None
    aard: Optional[Waardelijst] = None
    betreft_gedeelte_van_perceel: Optional[bool] = Field(
        None, alias="betreftGedeelteVanPerceel"
    )
    einddatum: Optional[datetime] = None
    einddatum_recht: Optional[datetime] = Field(None, alias="einddatumRecht")
    omschrijving: Optional[str] = None
    aantekening_kadastraal_object: Optional[NEN3610ID] = Field(
        None, alias="aantekeningKadastraalObject"
    )
    aantekening_recht: Optional[List[NEN3610ID]] = Field(
        None, alias="aantekeningRecht", min_length=0
    )
    is_vermeld_in: Optional[List[NEN3610ID]] = Field(
        None, alias="isVermeldIn", min_length=0
    )
    is_gebaseerd_op: Optional[NEN3610ID] = Field(None, alias="isGebaseerdOp")
    betrokken_persoon: Optional[List[NEN3610ID]] = Field(
        None, alias="betrokkenPersoon", min_length=0
    )


class LocatieKadastraalObject(BaseModel):
    koppelingswijze: Optional[Waardelijst] = None
    betreft: Optional[NEN3610ID] = None
    heeft: Optional[NEN3610ID] = None


class OnroerendeZaakFiliatie(BaseModel):
    betreft_oz: Optional[NEN3610ID] = Field(None, alias="betreftOZ")


class VoorwaartseOnroerendeZaakFiliatie(BaseModel):
    betreft_oz: Optional[NEN3610ID] = Field(None, alias="betreftOZ")


class FieldKadastraalObject(BaseModel):
    identificatie: Optional[NEN3610ID] = None


class AanvullendeGegevens(BaseModel):
    bij_identificatie: Optional[NEN3610ID] = Field(None, alias="bijIdentificatie")
    soort: Optional[str] = None
    gegevens: Optional[str] = None


class GevraagdGebied(BaseModel):
    betreft_onroerende_zaken: Optional[List[NEN3610ID]] = Field(
        None, alias="betreftOnroerendeZaken"
    )
    huisletter: Optional[str] = Field(None, pattern="^[a-zA-Z]$")
    huisnummer: Optional[int] = Field(None, ge=1, le=99999)
    huisnummertoevoeging: Optional[str] = Field(None, pattern="^([a-z,A-Z,0-9]){1,4}$")
    identificatie: Optional[NEN3610ID] = None
    postcode: Optional[str] = Field(None, pattern="^[1-9][0-9][0-9][0-9][A-Z][A-Z]$")
    straatnaam: Optional[str] = Field(None, max_length=80)
    plaatsnaam: Optional[str] = Field(None, max_length=80)


class TypeKadastraleAanduiding(BaseModel):
    appartementsrecht_volgnummer: Optional[int] = Field(
        None, alias="appartementsrechtVolgnummer"
    )
    kadastrale_gemeente: Optional[Waardelijst] = Field(None, alias="kadastraleGemeente")
    perceelnummer: Optional[int] = None
    sectie: Optional[str] = None


class TypeKoopsom(BaseModel):
    bedrag: Optional[Bedrag] = None
    indicatie_meer_objecten: Optional[bool] = Field(None, alias="indicatieMeerObjecten")
    koopjaar: Optional[int] = None


class TypeLandinrichtingsrente(BaseModel):
    bedrag: Optional[Bedrag] = None
    eindjaar: Optional[int] = None


class FieldOnroerendeZaak(FieldKadastraalObject):
    type: Optional[OnroerendeZaakTypeEnum] = None
    aard_cultuur_bebouwd: Optional[Waardelijst] = Field(
        None, alias="aardCultuurBebouwd"
    )
    aard_cultuur_onbebouwd: Optional[Waardelijst] = Field(
        None, alias="aardCultuurOnbebouwd"
    )
    heeft_meer_adressen: Optional[bool] = Field(None, alias="heeftMeerAdressen")
    kadastrale_aanduiding: Optional[TypeKadastraleAanduiding] = Field(
        None, alias="kadastraleAanduiding"
    )
    koopsom: Optional[TypeKoopsom] = None
    landinrichtingsrente: Optional[List[TypeLandinrichtingsrente]] = Field(
        None, min_length=0
    )
    toelichting_bewaarder: Optional[str] = Field(None, alias="toelichtingBewaarder")
    ontstaan_uit_oz: Optional[List[OnroerendeZaakFiliatie]] = Field(
        None, alias="ontstaanUitOZ", min_length=0
    )
    is_vermeld_in: Optional[List[NEN3610ID]] = Field(
        None, alias="isVermeldIn", min_length=0
    )
    overgegaan_in: Optional[List[VoorwaartseOnroerendeZaakFiliatie]] = Field(
        None, alias="overgegaanIn"
    )


class OLPCollectie(BaseModel):
    aanvullende_gegevens: Optional[List[AanvullendeGegevens]] = Field(
        None, alias="aanvullendeGegevens"
    )
    adres_locaties: Optional[List[FieldAdresLocatie]] = Field(
        None, alias="adresLocaties"
    )
    locatie_kadastraal_objecten: Optional[List[LocatieKadastraalObject]] = Field(
        None, alias="locatieKadastraalObjecten"
    )
    onroerende_zaken: Optional[List[FieldOnroerendeZaak]] = Field(
        None, alias="onroerendeZaken"
    )
    personen: Optional[List[PersoonType]] = None


class OICollectie(BaseModel):
    adres_locaties: Optional[List[FieldAdresLocatie]] = Field(
        None, alias="adresLocaties"
    )
    locatie_kadastraal_objecten: Optional[List[LocatieKadastraalObject]] = Field(
        None, alias="locatieKadastraalObjecten"
    )
    onroerende_zaken: Optional[List[FieldOnroerendeZaak]] = Field(
        None, alias="onroerendeZaken"
    )


class PTCollectie(BaseModel):
    adres_locaties: Optional[List[FieldAdresLocatie]] = Field(
        None, alias="adresLocaties"
    )
    gevraagd_gebied: Optional[GevraagdGebied] = Field(None, alias="gevraagdGebied")
    locatie_kadastraal_objecten: Optional[List[LocatieKadastraalObject]] = Field(
        None, alias="locatieKadastraalObjecten"
    )
    onroerende_zaken: Optional[List[FieldOnroerendeZaak]] = Field(
        None, alias="onroerendeZaken"
    )


class AttenderingKadastraalObject(BaseModel):
    van: Optional[NEN3610ID] = None
    ten_behoeve_van: Optional[List[NEN3610ID]] = Field(
        None, alias="tenBehoeveVan", title="tenBehoeveVan"
    )


class SignaleringKadastraalObject(BaseModel):
    ten_behoeve_van: Optional[List[NEN3610ID]] = Field(None, alias="tenBehoeveVan")
    van: Optional[NEN3610ID] = None


class OverigBetrokkenKadastraalObject(BaseModel):
    betreft: Optional[NEN3610ID] = None
    heeft: Optional[NEN3610ID] = None


class Stukdeel(BaseModel):
    identificatie: Optional[NEN3610ID] = None
    aard: Optional[Waardelijst] = None
    datum_kenbaarheid_pb: Optional[datetime] = Field(None, alias="datumKenbaarheidPB")
    omschrijving_gekozen_woonplaats: Optional[str] = Field(
        None, alias="omschrijvingGekozenWoonplaats"
    )
    is_aanvulling_op: Optional[List[NEN3610ID]] = Field(
        None, alias="isAanvullingOp", min_length=0
    )
    bedrag_vorderingsbeslag: Optional[Bedrag] = Field(
        None, alias="bedragVorderingsbeslag"
    )
    bedrag_zekerheidsstelling_hypotheek: Optional[Bedrag] = Field(
        None, alias="bedragZekerheidsstellingHypotheek"
    )


class Verblijfsobject(BaseModel):
    identificatie: Optional[str] = None
    hoofdadres: Optional[NEN3610ID] = None


class Collectie(BaseModel):
    aantekeningen: Optional[List[Aantekening]] = None
    locatie_kadastraal_objecten: Optional[List[LocatieKadastraalObject]] = Field(
        None, alias="locatieKadastraalObjecten"
    )
    onroerende_zaken: Optional[List[FieldOnroerendeZaak]] = Field(
        None, alias="onroerendeZaken"
    )
    personen: Optional[List[PersoonType]] = None
    adres_locaties: Optional[List[AdresType]] = Field(None, alias="adresLocaties")
    attendering_kadastraal_objecten: Optional[List[AttenderingKadastraalObject]] = (
        Field(None, alias="attenderingKadastraalObjecten")
    )
    signalering_kadastraal_objecten: Optional[List[SignaleringKadastraalObject]] = (
        Field(None, alias="signaleringKadastraalObjecten")
    )
    stukdelen: Optional[List[Stukdeel]] = None
    stukken: Optional[List[FieldType]] = None
    verblijfsobjecten: Optional[List[Verblijfsobject]] = None
    aanvullende_gegevens: Optional[List[AanvullendeGegevens]] = Field(
        None, alias="aanvullendeGegevens"
    )


class EDICollectie(Collectie):
    erfpachtcanons: Optional[List[Erfpachtcanon]] = None
    gezamenlijk_aandelen: Optional[List[GezamenlijkAandeel]] = Field(
        None, alias="gezamenlijkAandelen"
    )
    mandeligheden: Optional[List[Mandeligheid]] = None
    tenaamstellingen: Optional[List[Tenaamstelling]] = None
    appartementsrecht_splitsingen: Optional[List[AppartementsrechtSplitsing]] = Field(
        None, alias="appartementsrechtSplitsingen"
    )
    publiekrechtelijke_beperkingen: Optional[List[PubliekrechtelijkeBeperking]] = Field(
        None, alias="publiekrechtelijkeBeperkingen"
    )
    beperkingsgebieden: Optional[List[Beperkingsgebied]] = None
    zakelijk_rechten: Optional[List[ZakelijkRecht]] = Field(
        None, alias="zakelijkRechten"
    )
    verkavel_objecten: Optional[List[VerkavelObject]] = Field(
        None, alias="verkavelObjecten"
    )
    herverkavelingsgebieden: Optional[List[Herverkavelingsgebied]] = None


class HPICollectie(Collectie):
    zekerheidsstellingen: Optional[List[FieldZekerheidsstelling]] = None
    overig_betrokken_kadastraal_objecten: Optional[
        List[OverigBetrokkenKadastraalObject]
    ] = Field(None, alias="overigBetrokkenKadastraalObjecten")


class ATCollectie(BaseModel):
    adres_locaties: Optional[List[FieldAdresLocatie]] = Field(
        None, alias="adresLocaties"
    )
    gevraagd_gebied: Optional[GevraagdGebied] = Field(None, alias="gevraagdGebied")
    locatie_kadastraal_objecten: Optional[List[LocatieKadastraalObject]] = Field(
        None, alias="locatieKadastraalObjecten"
    )
    onroerende_zaken: Optional[List[FieldOnroerendeZaak]] = Field(
        None, alias="onroerendeZaken"
    )


class SignaleringPersoon(BaseModel):
    ten_behoeve_van: Optional[List[NEN3610ID]] = Field(None, alias="tenBehoeveVan")
    van: Optional[NEN3610ID] = None


class AttenderingPersoon(BaseModel):
    van: Optional[NEN3610ID] = None
    ten_behoeve_van: Optional[List[NEN3610ID]] = Field(
        None, alias="tenBehoeveVan", title="tenBehoeveVan"
    )


class EGICollectie(Collectie):
    erfpachtcanons: Optional[List[Erfpachtcanon]] = None
    gezamenlijk_aandelen: Optional[List[GezamenlijkAandeel]] = Field(
        None, alias="gezamenlijkAandelen"
    )
    mandeligheden: Optional[List[Mandeligheid]] = None
    tenaamstellingen: Optional[List[Tenaamstelling]] = None
    appartementsrecht_splitsingen: Optional[List[AppartementsrechtSplitsing]] = Field(
        None, alias="appartementsrechtSplitsingen"
    )
    publiekrechtelijke_beperkingen: Optional[List[PubliekrechtelijkeBeperking]] = Field(
        None, alias="publiekrechtelijkeBeperkingen"
    )
    beperkingsgebieden: Optional[List[Beperkingsgebied]] = None
    zakelijk_rechten: Optional[List[ZakelijkRecht]] = Field(
        None, alias="zakelijkRechten"
    )
    attendering_personen: Optional[List[AttenderingPersoon]] = Field(
        None, alias="attenderingPersonen"
    )
    signalering_personen: Optional[List[SignaleringPersoon]] = Field(
        None, alias="signaleringPersonen"
    )
    verkavel_objecten: Optional[List[VerkavelObject]] = Field(
        None, alias="verkavelObjecten"
    )
    herverkavelingsgebieden: Optional[List[Herverkavelingsgebied]] = None
