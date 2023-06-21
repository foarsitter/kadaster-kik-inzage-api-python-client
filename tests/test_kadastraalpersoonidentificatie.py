import datetime

import pytest

from kikinzage.client import AsyncClient
from kikinzage.client import DefaultClient
from kikinzage.models import KadastraalPersoonIdentificatie


def test_persoonsgegevens(kik: DefaultClient) -> None:
    response = kik.kadastraalpersoonidentificatie_persoonsgegevens(
        geslachtsnaam="Geslachtsnaam",
        voornamen="Voornamen",
        voorvoegselsgeslachtsnaam="van",
        geboortedatum=datetime.date(2000, 1, 1),
    )

    assert isinstance(response, KadastraalPersoonIdentificatie)


@pytest.mark.asyncio
async def test_persoonsgegevens_async(akik: AsyncClient) -> None:
    response = await akik.kadastraalpersoonidentificatie_persoonsgegevens(
        geslachtsnaam="Geslachtsnaam",
        voornamen="Voornamen",
        voorvoegselsgeslachtsnaam="van",
        geboortedatum=datetime.date(2000, 1, 1),
    )

    assert isinstance(response, KadastraalPersoonIdentificatie)
