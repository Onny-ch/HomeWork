from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_files import read_csv, read_xls
from src.utils import financial_transactions_data, get_transactions_amount, search_in_transactions

if __name__ == "__main__":
    menu_items = ["JSON", "CSV", "XLSX"]
    status_items = ["EXECUTED", "CANCELED", "PENDING"]
    user_trans_data = []

    input_meet = input(
        """
Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n
"""
    )
    try:
        if input_meet == "1":
            user_trans_data = financial_transactions_data("data\\operations.json")
        if input_meet == "2":
            user_trans_data = read_csv("data\\transactions.csv")
        if input_meet == "3":
            user_trans_data = read_xls("data\\transactions_excel.xlsx")
    except Exception as ex:
        print(f"Случилась ошибка: {ex}")
        quit()

    print(f"Для обработки выбран {menu_items[int(input_meet) - 1]}-файл.")

    while True:
        input_status = input(
            """
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
\n"""
        ).upper()

        if input_status in status_items:
            user_trans_data = filter_by_state(user_trans_data, input_status)
            if not user_trans_data:
                print("Транзакций с данным статусом нет.")
                quit()
            print(f"\nОперации отфильтрованы по статусу {input_status}")
            break
        else:
            print(f"Статус операции {input_status} недоступен.")

    user_date_sort = input("\nОтсортировать операции по дате? Да/Нет ").upper()

    if user_date_sort == "ДА":
        sort_order = input("\nОтсортировать по возрастанию или по убыванию? По возрастанию/По убыванию ").upper()
        if sort_order == "ПО УБЫВАНИЮ":
            user_trans_data = sort_by_date(user_trans_data, True)
        user_trans_data = sort_by_date(user_trans_data)

    currency_code_order = input("\nВыводить только рублевые транзакции? Да/Нет ").upper()

    if currency_code_order == "ДА":
        user_trans_data = filter_by_currency(user_trans_data)

    descr_sort_order = input("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет ").upper()

    if descr_sort_order == "ДА":
        description_words = input("\nВведите слова для фильтрации: ").title()
        final_list = search_in_transactions(user_trans_data, description_words)

    if len(user_trans_data):
        print(
            f"""
Распечатываю итоговый список транзакций...\n
Всего банковских операций в выборке: {len(user_trans_data)}\n"""
        )
        print(user_trans_data)
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    print(
        get_transactions_amount(
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            }
        )
    )
