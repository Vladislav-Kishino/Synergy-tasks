# Задание №3
m = int(input("Максимальная грузоподъемность лодки: "))
n = int(input("Количество рыбаков: "))
weights = [int(input("Вес рыбака: ")) for _ in range(n)]

# Фильтруем рыбаков: оставляем только тех, кого можно перевезти
valid_weights = [w for w in weights if w <= m]
valid_weights.sort()  # Сортируем допустимые веса

left = 0
right = len(valid_weights) - 1
boats = 0

while left <= right:
    # Пробуем посадить вместе самого легкого и самого тяжелого из оставшихся
    if valid_weights[left] + valid_weights[right] <= m:
        left += 1  # Легкий рыбак переправлен
    right -= 1  # Тяжелый рыбак переправлен
    boats += 1  # Использована одна лодка

print("Минимальное количество лодок для переправки рыбаков: ", (boats))