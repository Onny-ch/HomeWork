import logging

logger = logging.getLogger('masks')
file_handler = logging.FileHandler('logs\\masks.log', mode='w', encoding='UTF-8')
file_formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_mask_card_number(card_name: str) -> str:
    """Функция, маскирующая номер карты"""
    try:
        logger.info('Маскируем номер карты')
        return f"{card_name[:4]} {card_name[4:6]}** **** {card_name[-4:]}"
    except Exception as ex:
        logging.error(f'произошла ошибка {ex}')
        return ''


def get_mask_account(account_name: str) -> str:
    """Функция, маскирующая номер банковского аккаунта"""
    try:
        logger.info('Маскируем номер банковского аккаунта')
        masc_account = "**" + account_name[-4:]
        return masc_account
    except Exception as ex:
        logging.error(f'Произошла ошибка {ex}')
        return ''
