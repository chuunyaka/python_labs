import sys
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_to_xlsx import csv_to_xlsx

def run_pipeline() -> None:
    print("Запуск сценариев демонстрации ЛР5...\n")
    
    #1. JSON -> CSV
    print("№1: Конвертируем JSON в CSV...")
    json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
    print("Создано: data/out/people_from_json.csv\n")
    json_to_csv("data/samples/products.json", "data/out/products_from_json.csv")
    print("Создано: data/out/products_from_json.csv\n")
    
    #2. CSV -> JSON
    print("№2: Конвертируем исходный CSV в JSON...")
    csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
    print("Создано: data/out/people_from_csv.json\n")
    csv_to_json("data/samples/books.csv", "data/out/books_from_csv.json")
    print("Создано: data/out/books_from_csv.json\n")
    
    #3. CSV -> XLSX
    print("№3: Конвертируем результирующий CSV в Excel...")
    csv_to_xlsx("data/samples/cities.csv", "data/out/cities.xlsx")
    print("Создано: data/out/cities.xlsx\n")
    csv_to_xlsx("data/samples/games.csv", "data/out/games.xlsx")
    print("Создано: data/out/games.xlsx\n")
    
    print("Все демонстрационные сценарии успешно выполнены!")

if __name__ == "__main__":
    try:
        run_pipeline()
    except FileNotFoundError as e:
        print(f" Ошибка: Отсутствует необходимый файл -> {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print("Критическая ошибка валидации данных", file=sys.stderr)
        print(f"Детали: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Непредвиденная системная ошибка: {e}", file=sys.stderr)
        sys.exit(1)
