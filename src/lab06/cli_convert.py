import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_to_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()


    try:
        if args.cmd == "json2csv":
            json_to_csv(args.input, args.output)
            print("Готово! JSON успешно переведен в CSV.")

        elif args.cmd == "csv2json":
            csv_to_json(args.input, args.output)
            print("Готово! CSV успешно переведен в JSON.")

        elif args.cmd == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
            print("Готово! CSV успешно переведен в XLSX.")

    except FileNotFoundError:
        parser.error(f"Входной файл '{args.input}' не существует.")


if __name__ == "__main__":
    main()