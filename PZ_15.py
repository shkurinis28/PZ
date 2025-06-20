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
        print(f"Подключено к SQLite версии {sqlite3.version}")
        return conn
    except Error as e:
        print(e)
    
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
        print("Таблица 'Торговая_точка' создана успешно")
    except Error as e:
        print(e)

def add_trading_point(conn, этаж, площадь, наличие_кондиционера, стоимость_аренды_в_день):
  
    sql = '''INSERT INTO Торговая_точка(этаж, площадь, наличие_кондиционера, стоимость_аренды_в_день)
             VALUES(?,?,?,?)'''
    cursor = conn.cursor()
    cursor.execute(sql, (этаж, площадь, наличие_кондиционера, стоимость_аренды_в_день))
    conn.commit()
    return cursor.lastrowid

def get_all_trading_points(conn):
  
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Торговая_точка")
    rows = cursor.fetchall()
    
    for row in rows:
        print(f"ID: {row[0]}, Этаж: {row[1]}, Площадь: {row[2]} кв.м, Кондиционер: {'Да' if row[3] else 'Нет'}, Стоимость: {row[4]} руб/день")

def main():
    database = "trading_rent.db"
    
    conn = create_connection(database)
    
    if conn is not None:
     
        create_table(conn)
        
        add_trading_point(conn, 1, 50.5, True, 2500)
        add_trading_point(conn, 2, 30.0, False, 1800)
        add_trading_point(conn, 1, 75.2, True, 3500)
        
        print("\nСписок торговых точек:")
        get_all_trading_points(conn)
        
        conn.close()
    else:
        print("Ошибка! Не удалось создать соединение с базой данных.")

if name == '__main__':
    main()
  
