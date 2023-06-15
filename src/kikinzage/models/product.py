from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

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
