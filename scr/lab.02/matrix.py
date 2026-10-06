# Задание 2

# 1
def transpose(mat):
    if len(mat) == 0:
        return []

    first_row_len = len(mat[0])
    for row in mat:
        if len(row) != first_row_len:
            raise ValueError

    new_mat = []
    for j in range(first_row_len):
        new_row = []
        for i in range(len(mat)):
            new_row.append(mat[i][j])
        new_mat.append(new_row)

    return new_mat

print(f'[[1, 2, 3]] →{transpose([[1, 2, 3]])}')
print(f'[[1], [2], [3]] → {transpose([[1], [2], [3]])}')
print(f'[[1, 2], [3, 4]] → {transpose([[1, 2], [3, 4]])}')
print(f'[] → {transpose([])}')
print(f'[[1, 2], [3]] → {transpose([[1, 2], [3]])}')

# 2
def row_sums(mat):
    first_row_len = len(mat[0])
    for row in mat:
        if len(row) != first_row_len:
            raise ValueError

    new_mat = []
    for row in mat:
        new_mat.append(sum(row))
    return new_mat

print(f'[[1, 2, 3], [4, 5, 6]] → {row_sums([[1, 2, 3], [4, 5, 6]])}')
print(f'[[-1, 1], [10, -10]] → {row_sums([[-1, 1], [10, -10]])}')
print(f'[[0, 0], [0, 0]] → {row_sums([[0, 0], [0, 0]])}')
print(f'[[1, 2], [3]] → {row_sums([[1, 2], [3]])}')

# 3
def col_sums(mat):
    if len(mat) == 0:
        return [] 
    
    first_row_len = len(mat[0])
    for row in mat:
        if len(row) != first_row_len:
            raise ValueError
        
    new_mat = []
    for j in range(first_row_len):
        current_sum = 0
        for i in range(len(mat)):
            current_sum += (mat[i][j])
        new_mat.append(current_sum)

    return new_mat

print(f'[[1, 2, 3], [4, 5, 6]] → {col_sums([[1, 2, 3], [4, 5, 6]])}')
print(f'[[-1, 1], [10, -10]] → {col_sums([[-1, 1], [10, -10]])}')
print(f'[[0, 0], [0, 0]] → {col_sums([[0, 0], [0, 0]])}')
print(f'[[1, 2], [3]] → {col_sums([[1, 2], [3]])}')