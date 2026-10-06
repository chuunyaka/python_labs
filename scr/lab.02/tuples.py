# Задание 3

def format_record(rec):
    """
    Форматирует запись студента.
    Выбрасывает TypeError, если типы элементов неверны.
    Выбрасывает ValueError, если ФИО/группа пусты или GPA вне диапазона [0.0; 5.0].
    """
    full_name = str(rec[0]).split()
    group = str(rec[1]).strip()
    grade = rec[2]
    if (type(rec[0]) is not str) or (type(rec[1]) is not str) or (type(rec[2]) not in (float, int)):
        raise TypeError('Данные указаны не в том формате')
    if len(full_name) < 2:
        raise ValueError('ФИО должно содержать минимум Фамилию и Имя')
    if not group:
        raise ValueError('Группа не должна быть пустой')
    valid_dig = ['0', '1', '2', '3', '4']
    if str(grade)[0] not in valid_dig and str(grade) != '5.0':
        raise ValueError('GPA должен быть в диапазоне [0.00; 5.00]')

    new_str = ''
    if len(full_name) == 3:
        new_str += full_name[0].capitalize() + ' ' + full_name[1][0].upper() + '.' + full_name[2][0].upper() + '.'
    else:
        new_str += full_name[0].capitalize() + ' ' + full_name[1][0].upper() + '.' 
    new_str = new_str + ', гр. ' + group + ', ' + 'GPA' + ' ' f'{grade:.2f}'

    return new_str

print(f'("Иванов Иван Иванович", "BIVT-25", 4.6) → "{format_record(("Иванов Иван Иванович", "BIVT-25", 4.6))}"')
print(f'("Петров Пётр", "IKBO-12", 5.0) → "{format_record(("Петров Пётр", "IKBO-12", 5.0))}"')
print(f'("Петров Пётр Петрович", "IKBO-12", 5.0) → "{format_record(("Петров Пётр Петрович", "IKBO-12", 5.0))}"')
print(f'("  сидорова  анна   сергеевна ", "ABB-01", 3.999) → "{format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))}"')