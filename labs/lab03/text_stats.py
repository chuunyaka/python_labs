import sys

from labs.lib.text import normalize, tokenize, count_freq, top_n

def main():
    raw_text = sys.stdin.readline()

    normalized_text = normalize(raw_text)

    tokens = tokenize(normalized_text)

    freq = count_freq(tokens)

    top_5 = top_n(freq)

    total_words = len(tokens)
    unique_words = len(freq)

    print(f'Всего слов: {total_words}')
    print(f'Уникальных слов: {unique_words}')
    print('Топ-5:')

    for word, num in top_5:
        print(f'{word}:{num}')

main()