"""
Вариант 30
В двумерном списке все элементы, не лежащие на главной диагонали увеличить в 2 раза.
"""


def double_non_diagonal(matrix):
    return [
        list(map(lambda item: item * 2 if row != col else item, row_data))
        for row, row_data in enumerate(matrix)
        for col, item in enumerate(row_data)
    ]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = double_non_diagonal(matrix)
for row in result:
    print(row)
