# Задание №2
n = int(input("Ведите количество чисел: "))
arr = list(map(int, input("Введите числа через пробел: ").split()))

if n > 0:
    print("Изменённый массив: ")
    new_arr = [arr[-1]] + arr[:-1]
    print(' '.join(map(str, new_arr)))
else:
    print()