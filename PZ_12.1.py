"""
Вариант 30.
﻿﻿Даны средние значения температур за каждый месяц в году. Найти минимальное и максимальное значения температур за год. 
Вывести значения температур по временам года.
"""

def analyze_temperatures(temperatures):
    if len(temperatures) != 12:
        raise ValueError("Должно быть 12 значений температур - по одному на каждый месяц")
    
    min_temp = min(temperatures)
    max_temp = max(temperatures)
    print(f"Минимальная температура за год: {min_temp}")
    print(f"Максимальная температура за год: {max_temp}")
    
    seasons = {
        "Зима": temperatures[0:2] + [temperatures[11]],  # Декабрь, Январь, Февраль
        "Весна": temperatures[2:5],                      # Март, Апрель, Май
        "Лето": temperatures[5:8],                       # Июнь, Июль, Август
        "Осень": temperatures[8:11]                      # Сентябрь, Октябрь, Ноябрь
    }
    
    for season, temps in seasons.items():
        print(f"{season}: {temps}")

year_temperatures = [-5, -7, 2, 8, 15, 20, 23, 21, 16, 10, 3, -2]  
analyze_temperatures(year_temperatures)
