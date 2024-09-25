import json
import logging
import os.path
import re
from typing import Any

from src.external_api import currency_conversion

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs\\utils.log", mode="w", encoding="UTF-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def financial_transactions_data(json_file_path: str) -> list[Any]:
    """Получение списка транзакций их файла"""
    try:
        logger.info(f"Получение списка транзакций из файла {json_file_path}")
        if os.path.exists(json_file_path) is False:
            return []
        with open(json_file_path, encoding="UTF-8") as f:
            financial_transactions_list = json.load(f)
            if financial_transactions_list is [] or type(financial_transactions_list) is not list:
                return []
        return financial_transactions_list
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []


def get_transactions_amount(transaction: dict[Any, Any]) -> float:
    """Получение суммы транзакции в рублях из транзакции"""
    try:
        logger.info("Получение суммы транзакции в рублях")
        if transaction["operationAmount"]["currency"]["code"] != "RUB":
            amount = currency_conversion(
                transaction["operationAmount"]["currency"]["code"], transaction["operationAmount"]["amount"]
            )
            return amount
        amount = float(transaction["operationAmount"]["amount"])
        return amount
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return float()


def search_in_transactions(list_of_trans_dicts: list[dict[Any, Any]], search_string: str) -> list[dict[Any, Any]]:
    """Функция, которая ищет данные в списке словарей с данными транзакций по строке поиска"""
    findall_trans_list = [
        el
        for el in list_of_trans_dicts
        if "description" in el and re.search(search_string, el["description"], flags=re.IGNORECASE)
    ]
    return findall_trans_list
