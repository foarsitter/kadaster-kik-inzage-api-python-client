from kikinzage.models import Collectie
from kikinzage.models import ObjectlocatieBinnenland
from kikinzage.models import ObjectlocatieBuitenland
from kikinzage.models import PostbusLocatie


def test_collection_with_adres_locaties() -> None:
    c = Collectie()
    c.adres_locaties = [
        ObjectlocatieBinnenland(),
        ObjectlocatieBuitenland(),
        PostbusLocatie(),
    ]

    d = Collectie.model_validate_json(c.model_dump_json(by_alias=True))

    assert d.adres_locaties
    assert len(d.adres_locaties) == 3
    assert isinstance(d.adres_locaties[0], ObjectlocatieBinnenland)
    assert isinstance(d.adres_locaties[1], ObjectlocatieBuitenland)
    assert isinstance(d.adres_locaties[2], PostbusLocatie)
