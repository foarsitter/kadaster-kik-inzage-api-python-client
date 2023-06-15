from enum import Enum


class PersoonTypeEnum(Enum):
    NATUURLIJK_PERSOON = "NatuurlijkPersoon"
    NIET_NATUURLIJK_PERSOON = "NietNatuurlijkPersoon"


class AdresLocatieTypeEnum(Enum):
    OBJECTLOCATIE_BINNENLAND = "ObjectlocatieBinnenland"
    OBJECTLOCATIE_BUITENLAND = "ObjectlocatieBuitenland"
    POSTBUS_LOCATIE = "PostbusLocatie"


class AppartementsrechtSplitsingTypeEnum(Enum):
    HOOFSPLITSING = "Hoofsplitsing"
    ONDERSPLITSING = "Ondersplitsing"
    SPIEGELSPLITSING_ONDERSPLITSING = "SpiegelsplitsingOndersplitsing"
    SPIEGELSPLITSING_AFKOOP_ERFPACHT = "SpiegelsplitsingAfkoopErfpacht"


class Formaat(Enum):
    JSON = "json"
    PDF = "pdf"
    JSON_PDF = "json,pdf"
    PDF_JSON = "pdf,json"


class SeverityCode(Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class ObjectReferentieType(Enum):
    BAG = "BAG"
    BGT = "BGT"


class OnroerendeZaakTypeEnum(Enum):
    PERCEEL = "Perceel"
    APPARTEMENTSRECHT = "Appartementsrecht"
    LEIDINGNETWERK = "Leidingnetwerk"


class StukTypeEnum(Enum):
    TER_INSCHRIJVING_AANGEBODEN_STUK = "TerInschrijvingAangebodenStuk"
    KADASTERSTUK = "Kadasterstuk"


class ZekerheidsstellingTypeEnum(Enum):
    ZEKERHEIDSSTELLING_HYPOTHECAIR = "ZekerheidsstellingHypothecair"
    ZEKERHEIDSSTELLING_INZAKE_BESLAG = "ZekerheidsstellingInzakeBeslag"


class Type(Enum):
    POINT = "Point"
