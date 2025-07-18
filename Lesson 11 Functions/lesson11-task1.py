# Задание №1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def factorial_sequence(start_num):
    initial_factorial = factorial(start_num)
    
    result = []
    for num in range(initial_factorial, 0, -1):
        result.append(factorial(num))
    
    return result

number = int(input("Введите натуральное число: "))
factorial_list = factorial_sequence(number)

print(f"Факториал числа {number}: {factorial(number)}")
print(f"Список факториалов: {factorial_list}")