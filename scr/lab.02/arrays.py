# Задание 1

# 1
# def min_max(nums): 
#     if len(nums) == 0:
#         raise ValueError
#     nums_sort = sorted(nums)
#     min_num = nums_sort[0]
#     max_num = nums_sort[-1]
#     if min_num.is_integer():
#         min_num = int(min_num)
#     if max_num.is_integer():
#         max_num = int(max_num)
#     return (min_num,max_num)
# print(f'[3, -1, 5, 5, 0] → {min_max([3, -1, 5, 5, 0])}')
# print(f'[42] → {min_max([42])}')
# print(f'[-5, -2, -9] → {min_max([-5, -2, -9])}')
# print(f'[1.5, 2, 2.0, -3.1] → {min_max([1.5, 2, 2.0, -3.1])}')
# print(f'[] → {min_max([])}')

# 2
# def unique_sorted(nums):
#     new_list = set(nums)
#     new_list = list(new_list)
#     clean_list = []
#     while len(new_list) != 0:
#         clean_list.append(min(new_list))
#         new_list.remove(min(new_list))
#     return clean_list
# print(f'[3, 1, 2, 1, 3] → {unique_sorted([3, 1, 2, 1, 3])}')
# print(f'[] → {unique_sorted([])}')
# print(f'[-1, -1, 0, 2, 2] → {unique_sorted([-1, -1, 0, 2, 2])}')
# print(f'[1.0, 1, 2.5, 2.5, 0] → {unique_sorted([1.0, 1, 2.5, 2.5, 0])}')

# 3
def flatten(mat):
    new_list = []
    for row in mat:
        if type(row) is not list and type(row) is not tuple:
            raise TypeError
        new_list.extend(row)
    return new_list
print(f'[[1, 2], [3, 4]] → {flatten([[1, 2], [3, 4]])}')
print(f'[[1, 2], (3, 4, 5)] → {flatten([[1, 2], (3, 4, 5)])}')
print(f'[[1], [], [2, 3]] → {flatten([[1], [], [2, 3]])}')
print(f'[[1, 2], "ab"] → {flatten([[1, 2], "ab"])}')