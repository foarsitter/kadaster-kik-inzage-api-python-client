from kikinzage.models import AdresLocatieTypeEnum


def test_loading_models() -> None:
    assert AdresLocatieTypeEnum.POSTBUS_LOCATIE.value == "PostbusLocatie"
