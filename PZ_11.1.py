"""
Вариант 30
Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной последовательности из целых положительных и отрицательных чисел. 
Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
Элементы первого и второго файлов:
Количeство элементов первого и второго файлов:
Индекс первого минимально элемента первого файла:
Индеке последнего максимального элемента второго файла:
Элементы кратные 4 первого и второго файлов:
"""


import random

def generate_numbers(count):
    return [random.randint(-100, 100) for _ in range(count)]

def write_numbers(filename, numbers):
    with open(filename, 'w') as f:
        f.write(' '.join(map(str, numbers)))

def read_numbers(filename):
    with open(filename, 'r') as f:
        return list(map(int, f.read().split()))

numbers1 = generate_numbers(10)
numbers2 = generate_numbers(15)
write_numbers('file1.txt', numbers1)
write_numbers('file2.txt', numbers2)

nums1 = read_numbers('file1.txt')
nums2 = read_numbers('file2.txt')

min_index1 = nums1.index(min(nums1))
max_index2 = len(nums2) - 1 - nums2[::-1].index(max(nums2))
multiples4_1 = [x for x in nums1 if x % 4 == 0]
multiples4_2 = [x for x in nums2 if x % 4 == 0]

with open('result.txt', 'w') as f:
    f.write(f"Элементы первого и второго файлов:\n")
    f.write(f"Первый файл: {nums1}\n")
    f.write(f"Второй файл: {nums2}\n\n")
    
    f.write(f"Количество элементов первого и второго файлов:\n")
    f.write(f"Первый файл: {len(nums1)}\n")
    f.write(f"Второй файл: {len(nums2)}\n\n")
    
    f.write(f"Индекс первого минимального элемента первого файла: {min_index1}\n")
    f.write(f"Индекс последнего максимального элемента второго файла: {max_index2}\n\n")
    
    f.write(f"Элементы кратные 4 первого и второго файлов:\n")
    f.write(f"Первый файл: {multiples4_1}\n")
    f.write(f"Второй файл: {multiples4_2}\n")

print("Файл result.txt успешно создан.")
