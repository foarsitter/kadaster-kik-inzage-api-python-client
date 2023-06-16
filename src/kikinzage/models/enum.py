from enum import Enum


class PersoonTypeEnum(str, Enum):
    NATUURLIJK_PERSOON = "NatuurlijkPersoon"
    NIET_NATUURLIJK_PERSOON = "NietNatuurlijkPersoon"


class AdresLocatieTypeEnum(str, Enum):
    OBJECTLOCATIE_BINNENLAND = "ObjectlocatieBinnenland"
    OBJECTLOCATIE_BUITENLAND = "ObjectlocatieBuitenland"
    POSTBUS_LOCATIE = "PostbusLocatie"


class AppartementsrechtSplitsingTypeEnum(str, Enum):
    HOOFSPLITSING = "Hoofsplitsing"
    ONDERSPLITSING = "Ondersplitsing"
    SPIEGELSPLITSING_ONDERSPLITSING = "SpiegelsplitsingOndersplitsing"
    SPIEGELSPLITSING_AFKOOP_ERFPACHT = "SpiegelsplitsingAfkoopErfpacht"


class Formaat(str, Enum):
    JSON = "json"
    PDF = "pdf"
    JSON_PDF = "json,pdf"
    PDF_JSON = "pdf,json"


class SeverityCode(str, Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class ObjectReferentieType(str, Enum):
    BAG = "BAG"
    BGT = "BGT"


class OnroerendeZaakTypeEnum(str, Enum):
    PERCEEL = "Perceel"
    APPARTEMENTSRECHT = "Appartementsrecht"
    LEIDINGNETWERK = "Leidingnetwerk"


class StukTypeEnum(str, Enum):
    TER_INSCHRIJVING_AANGEBODEN_STUK = "TerInschrijvingAangebodenStuk"
    KADASTERSTUK = "Kadasterstuk"


class ZekerheidsstellingTypeEnum(str, Enum):
    ZEKERHEIDSSTELLING_HYPOTHECAIR = "ZekerheidsstellingHypothecair"
    ZEKERHEIDSSTELLING_INZAKE_BESLAG = "ZekerheidsstellingInzakeBeslag"


class Type(str, Enum):
    POINT = "Point"
