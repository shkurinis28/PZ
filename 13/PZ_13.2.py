"""
﻿В двумерном списке все элементы, не лежащие на главной диагонали увеличить в 2 раза.
"""

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i != j:  
            matrix[i][j] *= 2
print("\nМатрица после увеличения недиагональных элементов:")
for row in matrix:
    print(row)
