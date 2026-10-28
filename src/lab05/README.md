<h1>ЛР5 — JSON и конвертации (JSON↔CSV, CSV→XLSX): Техническое задание</h1>

Цель: Разобраться с форматом JSON, сериализацией/десериализацией и табличными конвертациями.

<h3>Запуск</h3>

1. Активация виртуального окружения:
   ```bash
   .venv\Scripts\activate
   ```

2. Установка зависимостей:
   ```bash
   pip install -r requirements.txt
   ```

3. Запуск главного демонстрационного скрипта:
   ```bash
   python -m src.lab05.main
   ```
<h3>Описание тестовых сценариев и валидаций</h3>

1. Тест JSON → CSV
* **Вход**: `data/samples/people.json`.
* **Ожидаемый результат**: Файл `data/out/people_from_json.csv`. Количество строк должно быть равно `N + 1` (где N — число объектов, 1 — строка заголовков). Поля, которых не было у некоторых пользователей, стали пустыми, значения разделены`;` или `,`.

<img src="..\..\images\lab.05\in\people_json.png" width="45%"/> <img src="..\..\images\lab.05\out\people_from_json.png" width="50%"/>

Мой пример:

<img src="..\..\images\lab.05\in\products.png" width="50%"/> <img src="..\..\images\lab.05\out\products_from_json.png" width="50%"/>

<strong>При отсутствии ключа программа не падает</strong> 

2. Тест CSV → JSON
* **Вход**: `data/samples/people.csv`.
* **Ожидаемый результат**: Файл `data/out/people_from_csv.json` идентичен исходному по структуре ключей, все типы данных приведены к строковым.

<img src="..\..\images\lab.05\in\people_csv.png" width="50%"/> <img src="..\..\images\lab.05\out\people_from_csv.png" width="45%"/>

Мой пример:

<img src="..\..\images\lab.05\in\books.png" width="50%"/> <img src="..\..\images\lab.05\out\books_from_csv.png" width="45%"/>

3. Тест CSV → XLSX (Проверка Excel)
* **Вход**: `data/samples/cities.csv` (содержит названия городов и длинные описания/координаты).
* **Ожидаемый результат**: Файл `data/out/cities.xlsx`. Каждая ячейка читается, текст не скрыт за границами, колонки адаптировались под ширину содержимого.

<img src="..\..\images\lab.05\in\cities_csv.png" width="50%"/> <img src="..\..\images\lab.05\out\cities.png" width="45%"/>

Мой пример:

<img src="..\..\images\lab.05\in\games.png" width="50%"/> <img src="..\..\images\lab.05\out\games.png" width="45%"/>

<h3>Вывод успешного выполнения сценариев в терминале</h3>

<img src="..\..\images\lab.05\result.png" alt="Вывод выполненых сценариев"/>