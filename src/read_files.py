from typing import Any

import pandas as pd


def read_csv(csv_file: str) -> list[dict[Any, Any]]:
    """Функция считывания финансовых операций из CSV файла"""
    df = pd.read_csv(csv_file, delimiter=";")

    transactions_dict = df.to_dict(orient="records")
    return transactions_dict


def read_xls(xsl_file: str) -> list[dict[Any, Any]]:
    """Функция считывания финансовых операций из Excel файла"""
    df = pd.read_excel(xsl_file)

    transactions_dict = df.to_dict(orient="records")
    return transactions_dict
