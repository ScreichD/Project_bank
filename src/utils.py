import json
import logging
import os
from json import JSONDecodeError

# Создаем основные конфигурации logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    filename="utils.log",
    filemode="w",
    encoding="utf-8",
)
# Создаем логи для отдельных частей функции
open_file_logger = logging.getLogger("app.file")
find_file_logger = logging.getLogger("find.file")
convert_file_logger = logging.getLogger("convert.file")

path_to_file = os.path.join(os.path.dirname(__file__), "data", "operations.json")


def file_opening(path_to_file: str) -> list[dict]:
    """Функция принимает путь к JSON файлу и возвращает список словарей с транзакциями"""
    try:
        find_file_logger.info("Поиск файла")
        with open(path_to_file, encoding="utf-8") as file_json:
            open_file_logger.info("Открытие файла json")
            try:
                transactions_info = json.load(file_json)
                convert_file_logger.info("Конвертирование в Python файл")
            except JSONDecodeError:
                transactions_info = []
                convert_file_logger.error("Ошибка конвертации")
                return transactions_info
        if not isinstance(transactions_info, list):
            open_file_logger.error("Ошибка чтения файла")
            return []
        return transactions_info
    except FileNotFoundError:
        transactions_info = []
        find_file_logger.error("Файл не найден")
        return transactions_info
    