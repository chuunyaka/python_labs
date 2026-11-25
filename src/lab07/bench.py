import random
import timeit
from pathlib import Path
from src.lab04.io_txt_csv import write_csv
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort, merge_sort, counting_sort
from src.lab07.search import linear_search, binary_search, two_sum_fast, two_sum_brute


def bench_sorts(n: int) -> list[tuple]:
    """Замеряет время работы sorted, merge_sort и квадратичных сортировок на списке длины n."""
    data = [random.randint(-100_000, 100_000) for _ in range(n)]
    rows = []
    t = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("sort", n, "sorted", f"{t:.6f}"))
    t_merge = timeit.timeit(lambda: merge_sort(data), number=1)
    rows.append(("sort", n, "merge_sort", f"{t_merge:.6f}")) 
    for name, fn in (
        ("bubble_sort", bubble_sort),
        ("insertion_sort", insertion_sort),
        ("selection_sort", selection_sort),
    ):
        if n == 100_000:
            rows.append(("sort", n, name, "> 60.0"))
        else:
            t = timeit.timeit(lambda: fn(data), number=1)
            rows.append(("sort", n, name, f"{t:.6f}"))
    return rows


def bench_search() -> list[tuple]:
    """Сравнивает 10 000 запросов линейного и бинарного поиска на списке из 100 000 элементов (включая время сортировки)."""
    rows = []
    n = 100_000
    data = [random.randint(0, 200_000) for _ in range(n)]
    queries = [random.randint(0, 200_000) for _ in range(10_000)]

    t_lin = timeit.timeit(lambda: [linear_search(data, q) for q in queries], number=1)
    rows.append(("search", n, "linear_search", f"{t_lin:.6f}"))

    t_sort = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("search", n, "sorted (presort)", f"{t_sort:.6f}"))

    sorted_data = sorted(data)
    t_bin = timeit.timeit(
        lambda: [binary_search(sorted_data, q) for q in queries], number=1
    )
    rows.append(("search", n, "binary_search", f"{t_bin:.6f}"))

    return rows


def bench_two_sum(n: int) -> list[tuple]:
    """Сравнивает время работы two_sum_brute и two_sum_fast на списке длины n с гарантированным ответом."""
    data = [random.randint(-100_000, 100_000) for _ in range(n)]
    target = data[-2] + data[-1]
    rows = []

    t_brute = timeit.timeit(lambda: two_sum_brute(data, target), number=1)
    rows.append(("two_sum", n, "two_sum_brute", f"{t_brute:.6f}"))

    t_fast = timeit.timeit(lambda: two_sum_fast(data, target), number=1)
    rows.append(("two_sum", n, "two_sum_fast", f"{t_fast:.6f}"))

    return rows

def bench_counting() -> list[tuple]:
    """Сравнивает counting_sort и sorted на большом списке с узким диапазоном значений."""
    n = 100_000
    data = [random.randint(0, 100) for _ in range(n)]
    rows = []

    t_sorted = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("sort_narrow", n, "sorted", f"{t_sorted:.6f}"))

    t_count = timeit.timeit(lambda: counting_sort(data, 0, 100), number=1)
    rows.append(("sort_narrow", n, "counting_sort", f"{t_count:.6f}"))

    return rows


def print_table(rows: list[tuple]) -> None:
    """Выводит результаты замеров в консоль в виде выровненной таблицы."""
    header = f"{'task':<11} | {'n':>8} | {'impl':<20} | {'seconds':>10}"
    print(header)
    print("-" * len(header))
    for task, n, impl, seconds in rows:
        print(f"{task:<11} | {n:>8} | {impl:<20} | {seconds:>10}")


if __name__ == "__main__":
    random.seed(42)
    rows = []

    for n in (1_000, 10_000, 100_000):
        rows.extend(bench_sorts(n))

    rows.extend(bench_search())

    for n in (1_000, 10_000):
        rows.extend(bench_two_sum(n))

    rows.extend(bench_counting())

    print_table(rows)

    out_path = Path("data/lab07/bench.csv")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    write_csv(rows, out_path, header=("task", "n", "impl", "seconds"))
