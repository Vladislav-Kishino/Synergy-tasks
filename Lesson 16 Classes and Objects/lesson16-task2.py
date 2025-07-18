# Задание №2
class Черепашка:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        #Увеличивает y на s
        self.y += self.s
        print(f"Переместились вверх. Текущая позиция: (x: {self.x}, y: {self.y})")

    def go_down(self):
        #Уменьшает y на s
        self.y -= self.s
        print(f"Переместились вниз. Текущая позиция: (x: {self.x}, y: {self.y})")

    def go_left(self):
        #Уменьшает x на s
        self.x -= self.s
        print(f"Переместились влево. Текущая позиция: (x: {self.x}, y: {self.y})")

    def go_right(self):
        #Увеличивает x на s
        self.x += self.s
        print(f"Переместились вправо. Текущая позиция: (x: {self.x}, y: {self.y})")

    def evolve(self):
        #Увеличивает s на 1
        self.s += 1
        print(f"Шаг увеличен. Теперь s = {self.s}")

    def degrade(self):
        #Уменьшает s на 1 или вызывает ошибку, если s ≤ 1
        if self.s <= 1:
            raise ValueError("Невозможно уменьшить шаг: s уже минимальный")
        self.s -= 1
        print(f"Шаг уменьшен. Теперь s = {self.s}")

    def count_moves(self, x2, y2):
        #Возвращает минимальное количество ходов до точки (x2, y2)
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        
        steps_x = dx // self.s + (1 if dx % self.s != 0 else 0)
        steps_y = dy // self.s + (1 if dy % self.s != 0 else 0)
        
        return steps_x + steps_y

    def __str__(self):
        return f"Черепашка: позиция (x: {self.x}, y: {self.y}), шаг {self.s}"

    def __repr__(self):
        return self.str()


def main():
    print('"Черепашка"')
    print("Создание черепашки...")
    try:
        x = int(input("Введите начальную координату x (по умолчанию 0): ") or 0)
        y = int(input("Введите начальную координату y (по умолчанию 0): ") or 0)
        s = int(input("Введите начальный шаг s (по умолчанию 1): ") or 1)
        t = Черепашка(x, y, s)
    except ValueError:
        print("Ошибка ввода! Используются значения по умолчанию.")
        t = Черепашка()

    while True:
        print("\nМеню:")
        print("1. Переместиться вверх")
        print("2. Переместиться вниз")
        print("3. Переместиться влево")
        print("4. Переместиться вправо")
        print("5. Увеличить шаг (evolve)")
        print("6. Уменьшить шаг (degrade)")
        print("7. Рассчитать минимальные ходы до точки")
        print("8. Показать текущее состояние")
        print("9. Выход")

        choice = input("Выберите действие (1-9): ")

        if choice == "1":
            t.go_up()
        elif choice == "2":
            t.go_down()
        elif choice == "3":
            t.go_left()
        elif choice == "4":
            t.go_right()
        elif choice == "5":
            t.evolve()
        elif choice == "6":
            try:
                t.degrade()
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif choice == "7":
            try:
                x2 = int(input("Введите целевую координату x: "))
                y2 = int(input("Введите целевую координату y: "))
                moves = t.count_moves(x2, y2)
                print(f"Минимальное количество ходов: {moves}")
            except ValueError:
                print("Ошибка: введите целые числа для координат")
        elif choice == "8":
            print(t)
        elif choice == "9":
            print("Программа завершена.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите 1-9.")


if __name__ == "__main__":
    main()