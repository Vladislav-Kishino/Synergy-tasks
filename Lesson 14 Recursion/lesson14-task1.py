# Задание №1
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def print_list_recursive(lst, index=0):
    if not lst:
        print("Конец списка")
        return
    
    if index < len(lst):
        print(lst[index])
        print_list_recursive(lst, index + 1)
    else:
        print("Конец списка")

print_list_recursive(my_list)