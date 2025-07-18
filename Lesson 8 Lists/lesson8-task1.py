# Задание №1
n = int(input("Введите количество чисел: "))

numbers = [int(input("Введите число: ")) for _ in range(n)]
reversed_numbers = numbers[::-1]
print("Перевёрнутый массив: ")
for num in reversed_numbers:
    print(num)