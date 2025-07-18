# Задание №1
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    def __init__(self, name, max_speed, mileage):
        Transport.__init__(self, name, max_speed, mileage)
    
    def __str__(self):
        return f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}"

bus = Autobus("Renaul Logan", 180, 12)

print(bus)