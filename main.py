from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_data, mask_account_card

if __name__ == '__main__':
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
    print(get_data("2018-07-11T02:26:18.671407"))
    print(mask_account_card("Maestro 1596837868705199".strip()))
    print(mask_account_card("Счет 64686473678894779589".strip()))
    print(mask_account_card("MasterCard 7158300734726758".strip()))
    print(mask_account_card("Счет 35383033474447895560".strip()))
    print(mask_account_card("Visa Classic 6831982476737658".strip()))
    print(mask_account_card("Visa Platinum 8990922113665229".strip()))
    print(mask_account_card("Visa Gold 5999414228426353".strip()))
    print(mask_account_card("Счет 73654108430135874305".strip()))
