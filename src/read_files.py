import pandas as pd
import json

from typing import Any


def read_csv(csv_file: Any) -> str:
    df = pd.read_csv(csv_file, delimiter=";")

    transactions_dict = df.to_json(orient="records", indent=4)
    return transactions_dict


def read_xls(xsl_file: Any) -> str:
    df = pd.read_excel(xsl_file, )

    transactions_dict = df.to_json(orient="records", indent=4)
    return transactions_dict


if __name__ == "__main__":
    print(read_csv('data\\transactions.csv'))
    print(read_xls('data\\transactions_excel.xlsx'))
