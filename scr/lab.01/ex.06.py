amount = (input('amount: '))
entry = ''
for i in range(1, int(amount) + 1):
    entry += input(f'in_{i}: ')
in_person = entry.count('True')
in_absentia = entry.count('False')
print(f'out: {in_person} {in_absentia}')