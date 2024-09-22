from typing import Any

import pandas as pd


def read_csv(csv_file: Any) -> str:
    """Функция считывания финансовых операций из CSV файла"""
    df = pd.read_csv(csv_file, delimiter=";")

    transactions_dict = df.head().to_json(orient="records", indent=4)
    return transactions_dict


def read_xls(xsl_file: Any) -> str:
    """Функция считывания финансовых операций из Excel файла"""
    df = pd.read_excel(xsl_file)

    transactions_dict = df.to_json(orient="records", indent=4)
    return transactions_dict
