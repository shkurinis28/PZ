"""
Вариант 30.
﻿﻿﻿Сгенерировать двумерный список, в которой элемены больше 10 заменяются на О.
"""

import random

matrix = list(map(lambda _: list(map(lambda _: random.randint(1, 20), range(4))), range(3))

result = list(map(lambda row: list(map(lambda x: 0 if x > 10 else x, row)), matrix))

print("Сгенерированная матрица:")
print(matrix)
print("\nОбработанная матрица:")
print(result)
