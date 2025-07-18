# Задание №1
print("Введите количество чисел: ")
n = int(input())

numbers = []
print(f"Введите {n} чисел через пробел, остальные числа считаться не будут: ")

while len(numbers) < n:
    remaining = n - len(numbers)
    if remaining > 1:
        print(f"Осталось ввести {remaining} чисел.")
    else:
        print("Осталось ввести 1 число:")
    
    parts = input().split()
    for part in parts:
        if len(numbers) < n:
            numbers.append(int(part))
        else:
            break

unique_count = len(set(numbers))
print(f"Количество различных чисел: {unique_count}")