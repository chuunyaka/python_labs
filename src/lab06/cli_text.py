import argparse
from src.lib.text import normalize, tokenize, count_freq, top_n

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "stats" and args.top < 1:
        parser.error("--top должен быть положительным числом")
        
    try:
        if args.command == "cat":
            with open(args.input, "r", encoding="utf-8") as f:
                number = 1
                for line in f:
                    clean_line = line.rstrip("\n")
                    if args.n:
                        print(f"{number}\t{clean_line}")
                        number += 1
                    else:
                        print(clean_line)

        elif args.command == "stats":
            with open(args.input, "r", encoding="utf-8") as f:
                text = f.read()

            normalized = normalize(text)
            tokens = tokenize(normalized)
            frequencies = count_freq(tokens)
            result = top_n(frequencies, n=args.top)

            print(f"--- Топ {args.top} слов ---")
            for word, count in result:
                print(f"{word}: {count}")

    except FileNotFoundError:
        parser.error(f"Файл '{args.input}' не найден. Проверьте путь.")

if __name__ == "__main__":
    main()