# Задание №3
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

even_numbers = [str(x) for x in range(a, b + 1) if x % 2 == 0]

print(' '.join(even_numbers))