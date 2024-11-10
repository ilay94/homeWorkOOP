import json
import logging
import os

from src.product import Product
from src.сategory import Category

# Настройка логера
logger = logging.getLogger("utils_log")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(__file__), "../logs/read_file_log.log"), mode="w", encoding="utf-8"
)
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_json_products(file_patch: str) -> list[Category]:
    """Функция чтения json файла, учитываем только списки"""
    try:
        logger.debug(f"Чтение файла {file_patch}")
        with open(file_patch, encoding="utf-8") as f:
            categorys = json.load(f)
            if isinstance(categorys, list):
                logger.debug(f"Чтение файла {file_patch} завершено успешно")
                return [
                    Category(
                        c.get("name"),
                        c.get("description"),
                        [
                            Product(p.get("name"), p.get("description"), p.get("price"), p.get("quantity"))
                            for p in c.get("products")
                        ],
                    )
                    for c in categorys
                ]

            else:
                logger.debug(f"Файл {file_patch} не содержит список категорий")
                return []
    except Exception as e:
        logger.error("В процессе чтения файла возникла ошибка:", exc_info=e)
        return []
