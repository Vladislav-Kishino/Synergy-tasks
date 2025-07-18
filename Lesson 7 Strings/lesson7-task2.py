# Задание №2
s = input("Введите строку: ")

result = []
prev_char = None

for char in s:
    if char != ' ' or prev_char != ' ':
        result.append(char)
    prev_char = char
    
clean_string = ''.join(result)

print("Результат:", clean_string)