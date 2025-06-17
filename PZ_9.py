"""
Вариант 30.
Сгенерировать словарь вида 10: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6:216},
удалить из него первый и последний элементы. Отобразить исходный и получившийся словарь. Использовать for, range.
"""

original_dict = {}
for i in range(7):
    original_dict[i] = i ** 3
modified_dict = original_dict.copy()
first_key = next(iter(modified_dict))
   del modified_dict[first_key]
last_key = list(modified_dict.keys())[-1]
   del modified_dict[last_key]
print("Исходный словарь:", original_dict)
print("Изменённый словарь:", modified_dict)
