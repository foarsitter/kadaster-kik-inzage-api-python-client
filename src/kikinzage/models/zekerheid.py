from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from .enum import ZekerheidsstellingTypeEnum
from .misc import NEN3610ID
from .misc import Waardelijst


class FieldZekerheidsstelling(BaseModel):
    identificatie: Optional[NEN3610ID] = None
    type: Optional[ZekerheidsstellingTypeEnum] = None
    omschrijving_betrokken_recht: Optional[Waardelijst] = Field(
        None, alias="omschrijvingBetrokkenRecht"
    )
    toelichting_bewaarder: Optional[str] = Field(None, alias="toelichtingBewaarder")
    is_gebaseerd_op: Optional[NEN3610ID] = Field(None, alias="isGebaseerdOp")
    is_vermeld_in: Optional[List[NEN3610ID]] = Field(
        None, alias="isVermeldIn", min_length=0
    )
    rust_op_object: Optional[NEN3610ID] = Field(None, alias="rustOpObject")
    heeft: Optional[List[NEN3610ID]] = None
    heeft_meer_overig_betrokken_kadastraal_objecten: Optional[bool] = Field(
        None, alias="heeftMeerOverigBetrokkenKadastraalObjecten"
    )


class ZekerheidsstellingHypothecair(FieldZekerheidsstelling):
    pass


class ZekerheidsstellingInzakeBeslag(FieldZekerheidsstelling):
    aard: Optional[Waardelijst] = None
