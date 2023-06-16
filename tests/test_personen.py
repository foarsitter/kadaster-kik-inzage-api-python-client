from kikinzage.models import Collectie
from kikinzage.models import GeregistreerdPersoon
from kikinzage.models import NatuurlijkPersoon
from kikinzage.models import NietNatuurlijkPersoon


def test_collection() -> None:
    c = Collectie()
    c.personen = [
        NietNatuurlijkPersoon(statutaireNaam="test"),
        NatuurlijkPersoon(betreft=GeregistreerdPersoon(bsn="123456789")),
    ]

    d = Collectie.model_validate_json(c.model_dump_json(by_alias=True))

    assert d.personen
    assert len(d.personen) == 2
    assert isinstance(d.personen[0], NietNatuurlijkPersoon)
    assert d.personen[0].statutaire_naam == "test"
    assert isinstance(d.personen[1], NatuurlijkPersoon)
    assert d.personen[1]
    assert d.personen[1].betreft
    assert d.personen[1].betreft.bsn == "123456789"
