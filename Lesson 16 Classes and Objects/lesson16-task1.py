# Задание №1
class Касса:
    def __init__(self, initial_amount=0):
        self.деньги = initial_amount
    
    def top_up(self, x):
        if x > 0:
            self.деньги += x
        else:
            raise ValueError("Сумма должна быть положительной")
    
    def count_1000(self):
        return self.деньги // 1000
    
    def take_away(self, x):
        if x <= 0:
            raise ValueError("Сумма должна быть положительной")
        if x > self.деньги:
            raise ValueError("Недостаточно денег в кассе")
        self.деньги -= x

def main():
    print('Добро пожаловать в программу "Касса"')
    начальная_сумма = int(input("Введите начальную сумму денег в кассе: "))
    касса = Касса(начальная_сумма)
    
    while True:
        print("\nМеню:")
        print("1. Пополнить кассу")
        print("2. Проверить количество тысяч")
        print("3. Изъять деньги")
        print("4. Показать текущий баланс")
        print("5. Выход")
        
        выбор = input("Выберите действие (1-5): ")
        
        if выбор == "1":
            сумма = int(input("Введите сумму для пополнения: "))
            try:
                касса.top_up(сумма)
                print(f"Касса пополнена. Текущий баланс: {касса.деньги} руб.")
            except ValueError as e:
                print(f"Ошибка: {e}")
        
        elif выбор == "2":
            тысяч = касса.count_1000()
            print(f"В кассе {тысяч} полных тысяч руб.")
        
        elif выбор == "3":
            сумма = int(input("Введите сумму для изъятия: "))
            try:
                касса.take_away(сумма)
                print(f"Успешно. Остаток: {касса.деньги} руб.")
            except ValueError as e:
                print(f"Ошибка: {e}")
        
        elif выбор == "4":
            print(f"Текущий баланс: {касса.деньги} руб.")
        
        elif выбор == "5":
            print("Программа завершена.")
            break
        
        else:
            print("Неверный ввод. Выберите 1-5.")

if __name__ == "__main__":
    main()