def linear_search(nums, x) -> int:
    """Индекс первого вхождения x или -1."""
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1


def binary_search(sorted_nums, x) -> int:
    """Индекс x в отсортированном по возрастанию списке или -1.
    На неотсортированном списке результат не определён.
    """
    lo, hi = 0, len(sorted_nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_nums[mid] == x:
            return mid
        if sorted_nums[mid] < x:
            lo = mid + 1
        if sorted_nums[mid] > x:
            hi = mid - 1
    return -1


def two_sum_brute(nums, target) -> tuple[int, int] | None:
    """Возвращает пару индексов (i, j) с i < j, для которых nums[i] + nums[j] == target, или None (перебор)."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


def two_sum_fast(nums, target) -> tuple[int, int] | None:
    """Возвращает пару индексов (i, j) с i < j, для которых nums[i] + nums[j] == target, или None (через словарь)."""
    seen = {}
    for i, x in enumerate(nums):
        obj = target - x
        if obj in seen:
            return (seen[obj], i)
        else:
            seen[x] = i
    return None
