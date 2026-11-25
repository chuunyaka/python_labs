def bubble_sort(nums) -> list:
    """Возвращает новый список, отсортированный пузырьком по возрастанию."""
    new_list = list(nums)
    n = len(new_list)
    for step in range(n - 1):
        swapped = False
        for i in range(n - 1 - step):
            if new_list[i] > new_list[i + 1]:
                new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
                swapped = True
        if not swapped:
            break
    return new_list


# print(bubble_sort([8, 5, 3, 7, 1, 6]))


def insertion_sort(nums) -> list:
    """Возвращает новый список, отсортированный вставками по возрастанию."""
    new_list = list(nums)
    n = len(new_list)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if new_list[j] < new_list[j - 1]:
                new_list[j], new_list[j - 1] = new_list[j - 1], new_list[j]
            else:
                break
    return new_list


# print(insertion_sort([3, 5, -8, 7, 1, -6]))


def selection_sort(nums) -> list:
    """Возвращает новый список, отсортированный выбором по возрастанию."""
    new_list = list(nums)
    n = len(new_list)
    for i in range(n - 1):
        key = new_list[i]
        min_index = i
        for j in range(i + 1, n):
            if key > new_list[j]:
                key = new_list[j]
                min_index = j
        if min_index != i:
            new_list[i], new_list[min_index] = new_list[min_index], new_list[i]

    return new_list


# print(selection_sort([3, 5, -8, 7, 1, -6]))


def merge_sort(nums) -> list:
    """Возвращает новый список, отсортированный слиянием (снизу вверх) по возрастанию."""
    new_list = list(nums)
    n = len(new_list)
    width = 1
    while width < n:
        for i in range(0, n, 2 * width):
            left = new_list[i : i + width]
            right = new_list[i + width : i + 2 * width]
            merged = []
            l = 0
            r = 0
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    merged.append(left[l])
                    l += 1
                else:
                    merged.append(right[r])
                    r += 1
            merged.extend(left[l:])
            merged.extend(right[r:])
            new_list[i : i + len(merged)] = merged
        width *= 2
    return new_list


# print(merge_sort([3, 5, -8, 7, 1, -6]))


def counting_sort(nums, lo, hi):
    """Возвращает новый список целых чисел из диапазона [lo, hi], отсортированный подсчётом."""
    if not nums:
        return []
    counts = [0] * (hi - lo + 1)
    for x in nums:
        counts[x - lo] += 1
    result = []
    for i, cnt in enumerate(counts):
        result.extend([lo + i] * cnt)
    return result


# print(counting_sort([3, 5, -8, 7, 1, -6], -8, 7))
