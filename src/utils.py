import json
import os.path
from typing import Any

from src.external_api import currency_conversion


def financial_transactions_data(json_file_path: str) -> list[Any]:
    """Получение списка транзакций их файла"""
    if os.path.exists(json_file_path) is False:
        return []
    with open(json_file_path, encoding="UTF-8") as f:
        financial_transactions_list = json.load(f)
        if financial_transactions_list is [] or type(financial_transactions_list) is not list:
            return []
    return financial_transactions_list


def get_transactions_amount(transaction: dict[Any, Any]) -> float:
    """Получение суммы транзакции в рублях из транзакции"""
    if transaction["operationAmount"]["currency"]["code"] != "RUB":
        amount = currency_conversion(
            transaction["operationAmount"]["currency"]["code"], transaction["operationAmount"]["amount"]
        )
        return amount
    amount = float(transaction["operationAmount"]["amount"])
    return amount


# Реализуйте функцию, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
# тип данных — float. Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего
# курса валют и конвертации суммы операции в рубли. Для конвертации валюты воспользуйтесь
# Exchange Rates Data API: https://apilayer.com/exchangerates_data-api.
# Функцию конвертации поместите в модульexternal_api.Используйте переменные окружения из файла.env для
# сокрытия чувствительных данных (токенов доступа для API). Создайте шаблон файла.env и разместите в репозитории
# на GitHub.Напишите тесты для новых функций, используйте Mock и patch.
