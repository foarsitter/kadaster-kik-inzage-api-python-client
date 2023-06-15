# generated by datamodel-codegen:
#   filename:  https://developer.kadaster.nl/schemas/kik-inzage/6.0.x/openapi.yaml
#   timestamp: 2023-06-13T15:07:50+00:00

from datetime import datetime
from typing import List
from typing import Optional

from pydantic import AnyUrl
from pydantic import BaseModel
from pydantic import Field
from pydantic import RootModel

from kikinzage.models.collectie import Collectie
from kikinzage.models.collectie import EigendomsinformatieProduct
from kikinzage.models.collectie import FieldAdresLocatie
from kikinzage.models.collectie import FieldOnroerendeZaak
from kikinzage.models.collectie import GevraagdGebied
from kikinzage.models.collectie import HPICollectie
from kikinzage.models.collectie import LocatieKadastraalObject
from kikinzage.models.collectie import OICollectie
from kikinzage.models.collectie import OLPCollectie
from kikinzage.models.collectie import PTCollectie
from kikinzage.models.eigendomsinformatie import AppartementsrechtSplitsing
from kikinzage.models.eigendomsinformatie import Beperkingsgebied
from kikinzage.models.eigendomsinformatie import Erfpachtcanon
from kikinzage.models.eigendomsinformatie import GezamenlijkAandeel
from kikinzage.models.eigendomsinformatie import Herverkavelingsgebied
from kikinzage.models.eigendomsinformatie import Mandeligheid
from kikinzage.models.eigendomsinformatie import PubliekrechtelijkeBeperking
from kikinzage.models.eigendomsinformatie import Tenaamstelling
from kikinzage.models.eigendomsinformatie import VerkavelObject
from kikinzage.models.eigendomsinformatie import ZakelijkRecht
from kikinzage.models.enum import Formaat
from kikinzage.models.enum import SeverityCode
from kikinzage.models.misc import NEN3610ID
from kikinzage.models.misc import PointGeoJSON
from kikinzage.models.misc import Waardelijst
from kikinzage.models.product import Product


class Adresnummer(RootModel[str]):
    root: str = Field(..., title="Adresnummer")


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


class DownloadGegevens(BaseModel):
    download_url: Optional[str] = Field(None, alias="downloadUrl")
    afgifte_id: Optional[str] = Field(None, alias="afgifteId")


class Foutbericht(BaseModel):
    type: Optional[AnyUrl] = Field(
        None, description="Link naar meer informatie over deze fout"
    )
    title: Optional[str] = Field(None, description="Beschrijving van de fout")
    status: Optional[int] = Field(None, description="Http status code")
    detail: Optional[str] = Field(None, description="Details over de fout")


class GeleverdProductBrondocument(BaseModel):
    product: Optional[DownloadGegevens] = None
    authentieke_akte: Optional[DownloadGegevens] = Field(None, alias="authentiekeAkte")


class GeleverdProductDatuminformatie(BaseModel):
    product: Optional[DatuminformatieProduct] = None


class InvalidParam(BaseModel):
    type: Optional[AnyUrl] = None
    name: Optional[str] = Field(None, description="Naam van de parameter")
    reason: Optional[str] = Field(
        None, description="Beschrijving van de fout op de parameterwaarde"
    )


class Melding(BaseModel):
    code: Optional[str] = None
    omschrijving: Optional[str] = None
    severity_code: Optional[SeverityCode] = Field(None, alias="severityCode")


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


class OpenbareRuimte(BaseModel):
    openbare_ruimte_naam: Optional[str] = Field(
        None, alias="openbareRuimteNaam", max_length=80, min_length=1
    )
    gerelateerde_woonplaats_naam: Optional[str] = Field(
        None, alias="gerelateerdeWoonplaatsNaam", max_length=80, min_length=1
    )


class ProcesVerwerking(BaseModel):
    proces_verwerkingscode: Optional[int] = Field(None, alias="procesVerwerkingscode")
    severity_code: Optional[SeverityCode] = Field(None, alias="severityCode")
    meldingen: Optional[List[Melding]] = None


class ProductGegevens(BaseModel):
    klantreferentie: Optional[str] = None
    productieordernummer: Optional[str] = None
    tijdstip_samenstelling_bericht: Optional[datetime] = Field(
        None, alias="tijdstipSamenstellingBericht"
    )
    aantal_kadastrale_objecten: Optional[int] = Field(
        None, alias="aantalKadastraleObjecten"
    )
    aanvraag_gegevens: Optional[str] = Field(None, alias="aanvraagGegevens")
    meldingen_product: Optional[List[MeldingProduct]] = Field(
        None, alias="meldingenProduct"
    )


class SignaleringPersoon(BaseModel):
    ten_behoeve_van: Optional[List[NEN3610ID]] = Field(None, alias="tenBehoeveVan")
    van: Optional[NEN3610ID] = None


class TypePostcode(RootModel[str]):
    root: str = Field(..., title="TypePostcode")


class AdresBuitenland(BaseModel):
    adres: Optional[str] = Field(None, max_length=50, min_length=1)
    identificatie: Optional[Adresnummer] = None
    land: Optional[Waardelijst] = None
    regio: Optional[str] = Field(None, max_length=39, min_length=1)
    woonplaats: Optional[str] = Field(None, max_length=80, min_length=1)


class AttenderingPersoon(BaseModel):
    van: Optional[NEN3610ID] = None
    ten_behoeve_van: Optional[List[NEN3610ID]] = Field(
        None, alias="tenBehoeveVan", title="tenBehoeveVan"
    )


class Brondocument(BaseModel):
    proces: Optional[ProcesVerwerking] = None
    product_gegevens: Optional[ProductGegevens] = Field(None, alias="productGegevens")
    geleverd_product: Optional[GeleverdProductBrondocument] = Field(
        None, alias="geleverdProduct"
    )


class BsnBody(BaseModel):
    burgerservicenummer: str = Field(..., pattern="^([0][0-9]{8})|([1-9][0-9]{7,8})$")
    formaat: Formaat
    klantreferentie: str = Field(..., max_length=20, min_length=3)
    gebruikeridentificatie: Optional[str] = Field(None, max_length=20)
    hyperlinkopproduct: Optional[bool] = None
    inkoopnummer: Optional[str] = Field(None, max_length=35)
    referentienummer: Optional[str] = Field(None, max_length=35)


class Datuminformatie(BaseModel):
    proces: Optional[ProcesVerwerking] = None
    product_gegevens: Optional[ProductGegevens] = Field(None, alias="productGegevens")
    geleverd_product: Optional[GeleverdProductDatuminformatie] = Field(
        None, alias="geleverdProduct"
    )


class FoutberichtBadRequest(Foutbericht):
    invalid_params: Optional[List[InvalidParam]] = Field(
        None,
        alias="invalidParams",
        description="Foutmelding per fout in een parameter. Alle gevonden fouten worden één keer teruggemeld.",
    )


class GeleverdProductKadastraalPersoonIdentificatie(BaseModel):
    negatieve_mededeling: Optional[NegatieveMededelingProduct] = Field(
        None, alias="negatieveMededeling"
    )
    product: Optional[NEN3610ID] = None


class KadastraalPersoonIdentificatie(BaseModel):
    proces: Optional[ProcesVerwerking] = None
    product_gegevens: Optional[ProductGegevens] = Field(None, alias="productGegevens")
    geleverd_product: Optional[NEN3610ID] = Field(None, alias="geleverdProduct")
    geleverd_product_kpi: Optional[
        GeleverdProductKadastraalPersoonIdentificatie
    ] = Field(None, alias="geleverdProductKPI")


class Nummeraanduiding(BaseModel):
    huisletter: Optional[str] = Field(None, max_length=1, pattern="[a-zA-Z]")
    huisnummer: Optional[int] = Field(None, max_length=5, min_length=1)
    huisnummertoevoeging: Optional[str] = Field(
        None, max_length=4, min_length=1, pattern="([a-z,A-Z,0-9])+"
    )
    identificatie: Optional[str] = None
    postcode: Optional[str] = Field(
        None, max_length=6, pattern="[1-9][0-9][0-9][0-9][A-Z][A-Z]"
    )
    gerelateerde_openbare_ruimte: Optional[OpenbareRuimte] = Field(
        None, alias="gerelateerdeOpenbareRuimte"
    )
    gerelateerde_woonplaats_naam: Optional[str] = Field(
        None, alias="gerelateerdeWoonplaatsNaam", max_length=80, min_length=1
    )


class ObjectlocatieBinnenland(FieldAdresLocatie):
    nummeraanduiding: Optional[Nummeraanduiding] = None


class ObjectlocatieBuitenland(FieldAdresLocatie):
    adres_buitenland: Optional[AdresBuitenland] = Field(None, alias="adresBuitenland")


class PostbusLocatie(FieldAdresLocatie):
    postbusnummer: Optional[int] = Field(None, max_length=7, min_length=1)
    postcode: Optional[TypePostcode] = None
    woonplaats_naam: Optional[str] = Field(
        None, alias="woonplaatsNaam", max_length=80, min_length=1
    )


class TypeOppervlak(BaseModel):
    soort_grootte: Optional[Waardelijst] = Field(None, alias="soortGrootte")
    waarde: Optional[float] = None


class Appartementsrecht(FieldOnroerendeZaak):
    pass


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


class HypotheekinformatieProduct(Product):
    met: Optional[HPICollectie] = None


class Leidingnetwerk(FieldOnroerendeZaak):
    aard: Optional[Waardelijst] = None
    omschrijving: Optional[str] = None


class ObjectlijstPersoonProduct(Product):
    met: Optional[OLPCollectie] = None


class OvergegaanInProduct(Product):
    met: Optional[OICollectie] = None


class Perceel(FieldOnroerendeZaak):
    kadastrale_grootte: Optional[TypeOppervlak] = Field(None, alias="kadastraleGrootte")
    indicatie_meettarief_verschuldigd: Optional[bool] = Field(
        None, alias="indicatieMeettariefVerschuldigd"
    )
    plaatscoordinaten: Optional[PointGeoJSON] = None


class AdresTreffersProduct(Product):
    met: Optional[ATCollectie] = None


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


class EigenaarsinformatieProduct(Product):
    met: Optional[EGICollectie] = None


class GeleverdProductEigenaarsinformatie(BaseModel):
    negatieve_mededeling: Optional[NegatieveMededelingProduct] = Field(
        None, alias="negatieveMededeling"
    )
    product: Optional[EigenaarsinformatieProduct] = None
    pdf: Optional[str] = None


class GeleverdProductObjectlijstPersoon(BaseModel):
    negatieve_mededeling: Optional[NegatieveMededelingProduct] = Field(
        None, alias="negatieveMededeling"
    )
    product: Optional[ObjectlijstPersoonProduct] = None
    pdf: Optional[str] = None


class ObjectlijstPersoon(BaseModel):
    proces: Optional[ProcesVerwerking] = None
    product_gegevens: Optional[ProductGegevens] = Field(None, alias="productGegevens")
    geleverd_product: Optional[GeleverdProductObjectlijstPersoon] = Field(
        None, alias="geleverdProduct"
    )


class PostcodeTreffersProduct(Product):
    met: Optional[PTCollectie] = None


class Eigenaarsinformatie(BaseModel):
    proces: Optional[ProcesVerwerking] = None
    product_gegevens: Optional[ProductGegevens] = Field(None, alias="productGegevens")
    geleverd_product: Optional[GeleverdProductEigenaarsinformatie] = Field(
        None, alias="geleverdProduct"
    )


class GeleverdProductEigendomsinformatie(BaseModel):
    product: Optional[EigendomsinformatieProduct] = None
    pdf: Optional[str] = None
    postcode_treffers: Optional[PostcodeTreffersProduct] = Field(
        None, alias="postcodeTreffers"
    )
    overgegaan_in: Optional[OvergegaanInProduct] = Field(None, alias="overgegaanIn")
    adres_treffers: Optional[AdresTreffersProduct] = Field(None, alias="adresTreffers")


class GeleverdProductHypotheekinformatie(BaseModel):
    product: Optional[HypotheekinformatieProduct] = None
    pdf: Optional[str] = None
    postcode_treffers: Optional[PostcodeTreffersProduct] = Field(
        None, alias="postcodeTreffers"
    )
    overgegaan_in: Optional[OvergegaanInProduct] = Field(None, alias="overgegaanIn")
    adres_treffers: Optional[AdresTreffersProduct] = Field(None, alias="adresTreffers")


class GeleverdProductKadastraleKaart(BaseModel):
    pdf: Optional[str] = None
    postcode_treffers: Optional[PostcodeTreffersProduct] = Field(
        None, alias="postcodeTreffers"
    )
    overgegaan_in: Optional[OvergegaanInProduct] = Field(None, alias="overgegaanIn")
    adres_treffers: Optional[AdresTreffersProduct] = Field(None, alias="adresTreffers")


class Hypotheekinformatie(BaseModel):
    proces: Optional[ProcesVerwerking] = None
    product_gegevens: Optional[ProductGegevens] = Field(None, alias="productGegevens")
    geleverd_product: Optional[GeleverdProductHypotheekinformatie] = Field(
        None, alias="geleverdProduct"
    )


class KadastraleKaart(BaseModel):
    proces: Optional[ProcesVerwerking] = None
    product_gegevens: Optional[ProductGegevens] = Field(None, alias="productGegevens")
    geleverd_product: Optional[GeleverdProductKadastraleKaart] = Field(
        None, alias="geleverdProduct"
    )


class Eigendomsinformatie(BaseModel):
    proces: Optional[ProcesVerwerking] = None
    product_gegevens: Optional[ProductGegevens] = Field(None, alias="productGegevens")
    geleverd_product: Optional[GeleverdProductEigendomsinformatie] = Field(
        None, alias="geleverdProduct"
    )
