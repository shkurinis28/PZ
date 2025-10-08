"""
Вариант 30
Приложение СДАЧА В АРЕНДУ ТОРГОВЫХ ПЛОЩАДЕЙ для искогорой организации.
БД должна содержать таблицу Торговая точка со следующей структурой записи: этаж, площадь, наличие кондиционера и стоимость аренды в день.
"""
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f" Подключено к SQLite версии {sqlite3.version}")
        return conn
    except Error as e:
        print(f" Ошибка подключения: {e}")
    return conn

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Торговая_точка (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            этаж INTEGER NOT NULL,
            площадь REAL NOT NULL,
            наличие_кондиционера BOOLEAN NOT NULL,
            стоимость_аренды_в_день REAL NOT NULL
        );
        """)
        print(" Таблица 'Торговая_точка' создана успешно")
    except Error as e:
        print(f" Ошибка создания таблицы: {e}")

def add_trading_point(conn, этаж, площадь, наличие_кондиционера, стоимость_аренды_в_день):
    sql = '''INSERT INTO Торговая_точка(этаж, площадь, наличие_кондиционера, стоимость_аренды_в_день)
             VALUES(?,?,?,?)'''
    cursor = conn.cursor()
    cursor.execute(sql, (этаж, площадь, наличие_кондиционера, стоимость_аренды_в_день))
    conn.commit()
    print(f" Добавлена торговая точка на {этаж} этаже, {площадь} кв.м")
    return cursor.lastrowid

def get_all_trading_points(conn):
    """ Получение всех торговых точек """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Торговая_точка")
    rows = cursor.fetchall()
    
    print("\n" + "="*80)
    print("СПИСОК ВСЕХ ТОРГОВЫХ ТОЧЕК")
    print("="*80)
    
    if not rows:
        print(" Торговые точки не найдены")
        return
    
    total_area = 0
    total_income = 0
    
    for row in rows:
        print(f" ID: {row[0]}")
        print(f"   Этаж: {row[1]}")
        print(f"   Площадь: {row[2]} кв.м")
        print(f"   Кондиционер: {'Да' if row[3] else 'Нет'}")
        print(f"   Стоимость аренды: {row[4]} руб/день")
        print("-" * 40)
        
        total_area += row[2]
        total_income += row[4]
    
    print(f" ОБЩАЯ СТАТИСТИКА:")
    print(f"   Всего точек: {len(rows)}")
    print(f"   Общая площадь: {total_area} кв.м")
    print(f"   Общий доход в день: {total_income} руб")
    print("="*80)

def search_by_floor(conn, этаж):
    """ Поиск торговых точек по этажу """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Торговая_точка WHERE этаж = ?", (этаж,))
    rows = cursor.fetchall()
    
    print(f"\n Поиск по {этаж} этажу:")
    print("-" * 40)
    
    if not rows:
        print("Точки не найдены")
        return
    
    for row in rows:
        print(f"ID: {row[0]}, Площадь: {row[2]} кв.м, Кондиционер: {'Да' if row[3] else 'Нет'}, Стоимость: {row[4]} руб")

def get_points_with_air_conditioning(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Торговая_точка WHERE наличие_кондиционера = True")
    rows = cursor.fetchall()
    
    print(f"\n Точки с кондиционером:")
    print("-" * 40)
    
    if not rows:
        print(" Точки с кондиционером не найдены")
        return
    
    for row in rows:
        print(f"ID: {row[0]}, Этаж: {row[1]}, Площадь: {row[2]} кв.м, Стоимость: {row[4]} руб")

def calculate_total_income(conn):
    
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(стоимость_аренды_в_день) FROM Торговая_точка")
    total = cursor.fetchone()[0]
    
    print(f"\n Общий потенциальный доход в день: {total or 0} руб")

def add_sample_data(conn):
    
    sample_data = [
        (1, 50.5, True, 2500),
        (2, 30.0, False, 1800),
        (1, 75.2, True, 3500),
        (3, 45.0, True, 2200),
        (2, 60.0, False, 2000),
        (1, 35.5, True, 1900),
        (3, 80.0, True, 4000)
    ]
    
    print("\n Добавление тестовых данных...")
    for data in sample_data:
add_trading_point(conn, *data)

def main():
    
    database = "trading_rent.db"
    
    print("ПРИЛОЖЕНИЕ ДЛЯ АРЕНДЫ ТОРГОВЫХ ПЛОЩАДЕЙ")
    print("="*50)
    
    # Создание подключения к базе данных
    conn = create_connection(database)
    
    if conn is not None:
        # Создание таблицы
        create_table(conn)
        
        # Добавление тестовых данных
        add_sample_data(conn)
        
        # Демонстрация функционала
        get_all_trading_points(conn)
        
        # Поиск по этажам
        search_by_floor(conn, 1)
        search_by_floor(conn, 2)
        
        # Точки с кондиционером
        get_points_with_air_conditioning(conn)
        
        # Расчет дохода
        calculate_total_income(conn)
        
        # Закрытие соединения
        conn.close()
        print(f"\n Приложение завершило работу. База данных сохранена в файле: {database}")
    else:
        print("Ошибка! Не удалось создать соединение с базой данных.")

if name == '__main__':
    main()
