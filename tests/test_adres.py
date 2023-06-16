from kikinzage.models import Collectie
from kikinzage.models import adres


def test_collection() -> None:
    c = Collectie()
    c.adres_locaties = [
        adres.ObjectlocatieBinnenland(),
        adres.ObjectlocatieBuitenland(),
        adres.PostbusLocatie(),
    ]

    d = Collectie.model_validate_json(c.model_dump_json(by_alias=True))

    assert d.adres_locaties
    assert len(d.adres_locaties) == 3
    assert isinstance(d.adres_locaties[0], adres.ObjectlocatieBinnenland)
    assert isinstance(d.adres_locaties[1], adres.ObjectlocatieBuitenland)
    assert isinstance(d.adres_locaties[2], adres.PostbusLocatie)
