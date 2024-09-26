import os

import requests
from dotenv import load_dotenv


def currency_conversion(currency_code: str, amount: str) -> float:
    """Функция, конвертирующая любую валюту в рубль и возвращающая пересчитанные деньги"""
    load_dotenv(".env")
    api_key = os.getenv("API_KEY")

    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"to": "RUB", "from": currency_code, "amount": amount}
    headers = {"apikey": api_key}

    request_data = requests.get(url=url, params=params, headers=headers).text

    pos = request_data.index("result")
    converted_amount = float(request_data[pos + 9: -2])
    return converted_amount
