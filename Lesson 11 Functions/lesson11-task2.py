# Задание №2
def main():
    print()
import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "Желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return 'год'
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return 'года'
    else:
        return 'лет'

def print_pet(pet_id, pet_name, pet_info):
    age = pet_info["Возраст питомца"]
    print(f'Это {pet_info["Вид питомца"]} по кличке "{pet_name}". '
          f'Возраст питомца: {age} {get_suffix(age)}. '
          f'Имя владельца: {pet_info["Имя владельца"]}')

def create():
    try:
        last_id = max(pets.keys()) if pets else 0
        new_id = last_id + 1
        
        name = input("Введите кличку питомца: ").strip()
        if not name:
            print("Ошибка: кличка не может быть пустой")
            return
            
        pet_type = input("Введите вид питомца: ").strip()
        age = int(input("Введите возраст питомца: "))
        owner = input("Введите имя владельца: ").strip()
        
        pets[new_id] = {
            name: {
                "Вид питомца": pet_type,
                "Возраст питомца": age,
                "Имя владельца": owner
            }
        }
        print(f"Питомец {name} успешно добавлен с ID: {new_id}")
    except ValueError:
        print("Ошибка: возраст должен быть числом")

def read():
    try:
        pet_id = int(input("Введите ID питомца: "))
        if pet_id not in pets:
            print("Питомец с таким ID не найден")
            return
            
        pet_name, pet_info = next(iter(pets[pet_id].items()))
        print_pet(pet_id, pet_name, pet_info)
    except ValueError:
        print("Ошибка: ID должен быть числом")

def update():
    try:
        pet_id = int(input("Введите ID питомца для обновления: "))
        if pet_id not in pets:
            print("Питомец с таким ID не найден")
            return
            
        old_name, old_info = next(iter(pets[pet_id].items()))
        
        print("\nТекущая информация:")
        print_pet(pet_id, old_name, old_info)
        
        print("\nВведите новые данные (оставьте пустым для сохранения текущего значения):")
        new_name = input(f"Кличка питомца [{old_name}]: ").strip() or old_name
        pet_type = input(f"Вид питомца [{old_info['Вид питомца']}]: ").strip() or old_info['Вид питомца']
        
        while True:
            age_input = input(f"Возраст [{old_info['Возраст питомца']}]: ").strip()
            if not age_input:
                age = old_info['Возраст питомца']
                break
            try:
                age = int(age_input)
                break
            except ValueError:
                print("Ошибка: возраст должен быть числом")
                
        owner = input(f"Имя владельца [{old_info['Имя владельца']}]: ").strip() or old_info['Имя владельца']

        if new_name != old_name:
            pets[pet_id] = {new_name: {
                "Вид питомца": pet_type,
                "Возраст питомца": age,
                "Имя владельца": owner
            }}
        else:
            pets[pet_id][old_name] = {
                "Вид питомца": pet_type,
                "Возраст питомца": age,
                "Имя владельца": owner
            }
            
        print("Информация успешно обновлена")
    except ValueError:
        print("Ошибка: ID должен быть числом")

def delete():
    try:
        pet_id = int(input("Введите ID питомца для удаления: "))
        if pet_id in pets:
            pet_name = next(iter(pets[pet_id].keys()))
            del pets[pet_id]
            print(f"Питомец {pet_name} успешно удален")
        else:
            print("Питомец с таким ID не найден")
    except ValueError:
        print("Ошибка: ID должен быть числом")

def list_all():
    if not pets:
        print("В базе нет питомцев")
        return
        
    print("\nСписок всех питомцев:")
    for pet_id, pet_data in pets.items():
        pet_name, pet_info = next(iter(pet_data.items()))
        print(f"ID: {pet_id}")
        print_pet(pet_id, pet_name, pet_info)
        print()

def main():
    commands = {
        'create': create,
        'read': read,
        'update': update,
        'delete': delete,
        'list': list_all,
        'stop': lambda: None
    }
    
    print("Добро пожаловать в систему учета питомцев ветеринарной клиники!")
    
    while True:
        print("\nДоступные команды:")
        print("create - добавить нового питомца")
        print("read - просмотреть информацию о питомце")
        print("update - обновить информацию о питомце")
        print("delete - удалить питомца")
        print("list - показать всех питомцев")
        print("stop - завершить работу")
        
        command = input("\nВведите команду: ").lower().strip()
        
        if command == 'stop':
            print("Работа программы завершена.")
            break
        elif command in commands:
            commands[command]()
        else:
            print("Неизвестная команда. Попробуйте еще раз.")

if __name__ == "__main__":
    main()