# Учебный проект e-commerce

## Описание:

Проект e-commerce - это приложение на Python для осуществления электронной коммерции.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/ilay94/pythonSkyProWidget.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Тестирование:
Для запуска тестирование воспользуйтесь командой:
#### при активированном виртуальном окружении
```
pytest --cov
```
#### через poetry
```
poetry run pytest --cov
```
#### генерировать отчет о покрытии в HTML-формате, где src — пакет c модулями, которые тестируем
```
pytest --cov=src --cov-report=html
```
## Использование:
#### Класс Product - описывает продукты и товары содержит поля:
```name: str ```  - название продукта 

```description: str ``` - описание продукта

```price: float ``` - цена продукта. Устанавливает цену на продукт, проверяет на отрицательность, проверяет на уменьшение цены

```quantity: int ``` - количество продукта

```new_product(product_params: dict, product_list=None)``` - создает новый продукт по переданному словарю, может проверять наличие похожего товара в переданном списке

```color: str``` - цвет продукта по умолчанию 

```__add__``` - складывает два продукта возвращаю сумму из цен товаров перемноженных на их количество

```___str_``` - возвращает описание экземпляра класса в виде "Название продукта, 80 руб. Остаток: 15 шт."

#### Класс Smartphone - описывает смартфоны, наследуется от Product:
```efficiency: float ```  - производительность

```model: str ```  - модель

```memory: int ```  - объем памяти

#### Класс LawnGrass - описывает траву газонную, наследуется от Product:
```country: str``` - странна производитель 

```germination_period: str``` - срок проростания

#### Класс Category - описывает категорию продуктов
```name: str ```  - название категории

```description: str ```  - описание категории

```products: str ```  - возвращает список продуктов категории в виде текста

```category_count```  - количество созданных категорий

```product_count```  - количество позиций товаров всех категорий

```add_product(product: Product)``` - добавляет продукт в список продуктов этой категории

```___str_``` - возвращает описание экземпляра класса в виде "Название категории, количество продуктов: 200 шт."

```get_products: list[Product]``` - возвращает список продуктов в виде объектов

### Класс IteratorProductInCategory
Создает итератор по продуктам в переданой при создании категории

#### Модуль read_file
```read_json_products(file_patch: str) -> list[Category]:``` - функция чтения категорий из json файла, учитываем только списки

## Документация:

Описание доступных функций представлена в виде Docstrings 

## Лицензия:

Этот проект лицензирован по [лицензии MIT](https://choosealicense.com/licenses/mit/).