# Инициалы и длина строки
full_name = input('ФИО: ')
newline = full_name.replace('-',' ')
newline = newline.split()
initials = ''
for i in range(len(newline)):
    initials += str(newline[i])[0]
clean_name = ' '.join(newline)
print(f'Инициалы: {initials}.\nДлина (символов): {len(clean_name)}')
