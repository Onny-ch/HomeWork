from src.external_api import currency_conversion


def test_currency_conversion():
    assert currency_conversion('RUB', '4700.01') == 4700.01
