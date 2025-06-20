"""
Вариант 30.
﻿﻿﻿Сгенерировать двумерный список, в которой элемены больше 10 заменяются на О.
"""

import random
size = 4
matrix = [[random.randint(1, 15) for _ in range(size)] for _ in range(size)]

print("Исходная матрица:")
for row in matrix:
    print(row)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > 10:
            matrix[i][j] = 0

print("\nМатрица после замены элементов > 10 на 0:")
for row in matrix:
    print(row)
