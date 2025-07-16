# Задание №2
x = int(input("Введите натуральное число: "))
count = 0

for i in range(1, int(x**0.5) + 1):
    if x % i == 0:
        count += 1
        if i != x // i:
            count += 1

print(f"Количество натуральных делителей числа {x}: {count}")