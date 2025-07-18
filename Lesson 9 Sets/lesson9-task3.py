# Задание №3
numbers = input("Введите последовательность чисел через пробел: ").split()
seen = set()  # Множество для хранения уже встреченных чисел

for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)