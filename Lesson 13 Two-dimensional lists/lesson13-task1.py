# Задание №1
import random

def create_matrix(rows, cols, min_val=-200, max_val=200):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0])) for i in range(len(matrix1))]]

def print_matrix(matrix, name):
    print(f"\nМатрица {name}:")
    for row in matrix:
        print(row)

# Создаем две матрицы 10x10
matrix_1 = create_matrix(10, 10)
matrix_2 = create_matrix(10, 10)

# Складываем матрицы
matrix_3 = add_matrices(matrix_1, matrix_2)

# Выводим результаты
print_matrix(matrix_1, "1")
print_matrix(matrix_2, "2")
print_matrix(matrix_3, "3 (сумма 1 и 2)")