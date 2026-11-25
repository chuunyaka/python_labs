import random
from src.lab07.sorting import (
    bubble_sort,
    insertion_sort,
    selection_sort,
    merge_sort,
    counting_sort,
)
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast


def check_sorting(fn, trials=100) -> None:
    """Проверяет сортировку fn на trials случайных списках против sorted и контроль мутации исходного списка."""
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"


def check_search(trials=100) -> None:
    """Проверяет linear_search и binary_search на trials случайных списках, включая отсутствующие и крайние элементы."""
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-50, 50) for _ in range(n)]
        s_nums = sorted(nums)
        targets = [random.randint(-60, 60)] + (s_nums[:1] + s_nums[-1:])

        for x in targets:
            try:
                expected = nums.index(x)
            except ValueError:
                expected = -1
            assert linear_search(nums, x) == expected, f"linear_search: {x} в {nums}"

            idx = binary_search(s_nums, x)
            if expected == -1:
                assert idx == -1, f"binary_search: лишний индекс для {x} в {s_nums}"
            else:
                assert (
                    0 <= idx < len(s_nums) and s_nums[idx] == x
                ), f"binary_search: {x} в {s_nums}"


def check_two_sum(trials=100) -> None:
    """Проверяет согласованность и корректность индексов для two_sum_brute и two_sum_fast на trials случайных списках."""
    for _ in range(trials):
        n = random.randint(2, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]

        if random.random() > 0.3:
            target = random.choice(nums) + random.choice(nums)
        else:
            target = 999

        res_brute = two_sum_brute(nums, target)
        res_fast = two_sum_fast(nums, target)

        assert (res_brute is None) == (
            res_fast is None
        ), f"Расхождение на {nums}: brute={res_brute}, fast={res_fast} на target={target}"

        if res_brute is not None:
            i, j = res_brute
            assert i < j, f"brute вернул i >= j: {i}, {j}"
            assert (
                nums[i] + nums[j] == target
            ), f"brute ошибся с суммой для target={target}"

        if res_fast is not None:
            fi, fj = res_fast
            assert (
                fi < fj
            ), f"fast вернул i >= j: {fi}, {fj}"
            assert (
                nums[fi] + nums[fj] == target
            ), f"fast ошибся с суммой для target={target}"


if __name__ == "__main__":
    random.seed(42)
    for fn in (bubble_sort, insertion_sort, selection_sort, merge_sort):
        check_sorting(fn)
    check_sorting(lambda nums: counting_sort(nums, -100, 100))
    check_search()
    check_two_sum()
    print("OK: 700 проверок")
