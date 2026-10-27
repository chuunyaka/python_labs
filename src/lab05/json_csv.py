import csv
import json
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    j_path = Path(json_path)
    c_path = Path(csv_path)
    if not j_path.exists():
        raise FileNotFoundError(f"Файл не найден: {json_path}")

    with j_path.open('r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Неверный формат JSON или пустой файл")

    if not isinstance(data,list):
        raise ValueError("JSON должен содержать список объектов")
    if len(data) == 0:
        raise ValueError("Пустой список в JSON")

    fieldnames = []
    seen_keys = set()

    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Все элементы списка в JSON должны быть словарями")

        for key in item.keys():
            if key not in seen_keys:
                seen_keys.add(key)
                fieldnames.append(key)

    if not fieldnames:
        raise ValueError("Объекты JSON не содержат ключей для создания колонок")

    c_path.parent.mkdir(parents=True, exist_ok=True) 
    with c_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames = fieldnames, restval="", extrasaction="ignore")
        w.writeheader()
        w.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    c_path = Path(csv_path)
    j_path = Path(json_path)

    if not c_path.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    with c_path.open("r", newline="", encoding="utf-8") as f:
        content = f.read()
        if not content.strip():
            raise ValueError("CSV файл пуст")
        f.seek(0)

        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("В CSV нет заголовков")

        data = list(reader)
        if len(data) == 0:
            raise ValueError("В CSV нет сторк с данными")

    j_path.parent.mkdir(parents=True, exist_ok=True)
    with j_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)