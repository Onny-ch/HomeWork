import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("logs\\masks.log", mode="w", encoding="UTF-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_mask_card_number(card_name: str) -> str:
    """Функция, маскирующая номер карты"""
    if 13 <= len(card_name) <= 19:
        logger.info("Маскируем номер карты.")
        return f"{card_name[:4]} {card_name[4:6]}** **** {card_name[-4:]}"
    else:
        logging.error("Неверный формат карты.")
        return ""


def get_mask_account(account_name: str) -> str:
    """Функция, маскирующая номер банковского аккаунта"""
    if len(account_name) == 20:
        logger.info("Маскируем номер банковского аккаунта.")
        masc_account = "**" + account_name[-4:]
        return masc_account
    else:
        logging.error("Неверно указан номер банковского аккаунта.")
        return ""
