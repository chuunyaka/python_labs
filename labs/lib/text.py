# Задание А
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Приводит строку в нижний регистр, меняет ё/Ё на е/Е, 
    заменяет невидимые управляющие символы на пробелы, схлопывает повторяющиеся пробелы в один.
    """
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')

    text = text.replace("\t", " ").replace("\r", " ").replace("\n", " ")

    return ' '.join(text.split())


def tokenize(text: str) -> list[str]:
    """Извлекает слова с помощью регулярного выражения."""
    return re.findall(r"\w+(?:-\w+)*", text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Подсчитывает частоту встречаемости слов."""
    freq = {}
    for w in sorted(tokens):
        freq[w] = freq.get(w, 0) + 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Возвращает топ-N значений по убыванию, при равенстве - по алфавиту."""
    pairs = sorted(freq.items(), key=lambda p: (-p[1], p[0]))
    top = pairs[:n]
    return top

def run_tests():
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"

    assert tokenize("привет, мир!") == ["привет", "мир"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]

    assert count_freq(["a","b","a","c","b","a"]) == {"a":3, "b":2, "c":1}
    assert top_n({"a":3, "b":2, "c":1}, 2) == [("a",3), ("b",2)]

    assert count_freq(["bb","aa","bb","aa","cc"]) == {'aa': 2, 'bb': 2, 'cc': 1}
    assert top_n({'aa': 2, 'bb': 2, 'cc': 1}, 2) == [("aa",2), ("bb",2)]

run_tests()