input_line = input('in: ')
start = 0
for i in range(len(input_line)):
    if input_line[i].isupper():
        start = i
        break 

for step in range(1, len(input_line)):
    if input_line[start + step - 1].isdigit():
        result = ""
        for j in range(start, len(input_line), step):
            result += input_line[j]
            if input_line[j] == '.':
                print(result)
        break 