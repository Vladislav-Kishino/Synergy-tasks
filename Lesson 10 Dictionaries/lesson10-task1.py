# Задание №1
pets = {}

def get_pet_age_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return 'год'
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return 'года'
    else:
        return 'лет'

def add_pet():
    name = input("Введите кличку питомца: ")
    pet_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")
    
    pets[name] = {
        'Вид питомца': pet_type,
        'Возраст питомца': age,
        'Имя владельца': owner
    }

def print_pet_info(name):
    pet = pets[name]
    age = pet['Возраст питомца']
    age_suffix = get_pet_age_suffix(age)
    
    print(f"Это {pet['Вид питомца']} по кличке \"{name}\". Возраст питомца: {age} {age_suffix}. Имя владельца: {pet['Имя владельца']}")

add_pet()
for pet_name in pets.keys():
    print_pet_info(pet_name)