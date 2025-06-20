"""
Вариант 30.
﻿﻿﻿Составить генератор (yield), который преобразует все буквенные символы в
заглавные.
"""

def uppercase_generator(input_string):
    for char in input_string:
        yield char.upper()

input_str = "Hello World! 123"
print(f"Исходная строка: {input_str}")

print("Преобразованная строка:", end=" ")
for upper_char in uppercase_generator(input_str):
    print(upper_char, end="")

result = ''.join(uppercase_generator(input_str))
print("\nРезультат как строка:", result)
