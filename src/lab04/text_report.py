import sys
import argparse
from pathlib import Path

try:
    from src.lab04.io_txt_csv import read_text, write_csv
except ImportError:
    from io_txt_csv import read_text, write_csv

from src.lib.text import normalize, tokenize, count_freq, top_n


def print_pretty_table(title: str, headers: list[str], rows: list) -> None:
    """Печатает отформатированную таблицу в консоль."""
    if not rows:
        print(f"\n--- {title} (Пусто) ---")
        return
    string_rows = [[str(cell) for cell in row] for row in rows]
    widths = [len(h) for h in headers]
    for row in string_rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))
            
    fmt = " | ".join(f"{{:<{w}}}" for w in widths)
    border = "-+-".join("-" * w for w in widths)
    
    print(f"\n--- {title} ---")
    print(fmt.format(*headers))
    print(border)
    for row in string_rows:
        print(fmt.format(*row))


def main() -> None:
    parser = argparse.ArgumentParser(description="ЛР4: Отчёты по текстовой статистике")
    parser.add_argument("--in", nargs="+", dest="inputs", default=["data/lab04/input.txt"],
                        help="Путь к одному или нескольким входным файлам")
    parser.add_argument("--out", default="data/lab04/report.csv",
                        help="Путь к базовому CSV-отчёту")
    parser.add_argument("--encoding", default="utf-8",
                        help="Кодировка входных файлов")
    parser.add_argument("--per-file", default=None,
                        help="Путь для сохранения отчёта по каждому файлу")
    parser.add_argument("--total", default=None,
                        help="Путь для сохранения сводного отчёта")

    args = parser.parse_args()
    total_out = args.total if args.total else args.out
    
    per_file_rows = []
    global_tokens = []  
    
    for file_str in args.inputs:
        file_path = Path(file_str)
        if not file_path.exists():
            print(f"Ошибка: Файл '{file_path}' не найден.", file=sys.stderr)
            sys.exit(1)
            
        try:
            text = read_text(file_path, encoding=args.encoding)
        except UnicodeDecodeError:
            print(f"Ошибка: Не удалось прочитать файл '{file_path}' в кодировке {args.encoding}.", file=sys.stderr)
            sys.exit(1)
            
        file_tokens = tokenize(normalize(text))
        global_tokens.extend(file_tokens)
        
        file_freq = count_freq(file_tokens)
        for word, count in file_freq.items():
            per_file_rows.append((file_path.name, word, count))

    total_freq = count_freq(global_tokens)
    
    sorted_total = top_n(total_freq, n=len(total_freq))
    write_csv(sorted_total, total_out, header=("word", "count"))
    
    if args.per_file:
        sorted_per_file = sorted(per_file_rows, key=lambda x: (x[0], -x[2], x[1]))
        write_csv(sorted_per_file, args.per_file, header=("file", "word", "count"))
        print_pretty_table("Отчёт по каждому файлу", ["file", "word", "count"], sorted_per_file)

    print_pretty_table("Сводный отчёт", ["word", "count"], sorted_total)

    total_words = len(global_tokens)
    unique_words = len(total_freq)
    final_top_5 = top_n(total_freq, n=5)
    
    print(f"\n=== Краткое резюме ===")
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in final_top_5:
        print(f"  {word}: {count}")


if __name__ == "__main__":
    main()
