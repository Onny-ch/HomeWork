from unittest.mock import Mock

import requests

from src.external_api import currency_conversion


def test_currency_conversion_one():
    mock_response = '{"result": 4700.01 }'
    requests.get = Mock(return_value=Mock(text=mock_response))
    assert currency_conversion("USD", "1") == 4700.01
