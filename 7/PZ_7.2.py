"""
Вариант 30
Дана строка, состоящая из русских слов, набранных заглавными буквами и разделенных пробелами (одним или несколькими). 
Найти количество слов, которые начинаются и заканчиваются одной и той же буквой.#
"""

s = "АРБУЗ ШАЛАШ КАЗАК ТЕСТ ПРИВЕТ АННА"
words = s.split()
count = 0 
for word in words:
    if word[0] == word[-1]:  
        count += 1
print(count) 
