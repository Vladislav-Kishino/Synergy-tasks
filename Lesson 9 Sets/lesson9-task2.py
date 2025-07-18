# Задание №2
print("Введите первый список чисел (каждое число на новой строке, завершите пустой строкой):")
list1 = []
while True:
    line = input().strip()
    if line == "":
        break
    list1.append(int(line))

print("Введите второй список чисел (каждое число на новой строке, завершите пустой строкой):")
list2 = []
while True:
    line = input().strip()
    if line == "":
        break
    list2.append(int(line))

set1 = set(list1)
set2 = set(list2)

common_numbers = set1 & set2

print(f"Количество чисел, содержащихся в обоих списках: {len(common_numbers)}")