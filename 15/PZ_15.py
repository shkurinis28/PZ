"""
Вариант 30
Приложение СДАЧА В АРЕНДУ ТОРГОВЫХ ПЛОЩАДЕЙ для искогорой организации.
БД должна содержать таблицу Торговая точка со следующей структурой записи: этаж, площадь, наличие кондиционера и стоимость аренды в день.
"""

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ Создание подключения к базе данных SQLite """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f" Подключено к SQLite версии {sqlite3.version}")
        return conn
    except Error as e:
        print(f" Ошибка подключения: {e}")
    return conn

def create_table(conn):
    """ Создание таблицы Торговая_точка """
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
    """ Добавление новой торговой точки """
    sql = '''INSERT INTO Торговая_точка(этаж, площадь, наличие_кондиционера, стоимость_аренды_в_день)
             VALUES(?,?,?,?)'''
    cursor = conn.cursor()
    cursor.execute(sql, (этаж, площадь, наличие_кондиционера, стоимость_аренды_в_день))
    conn.commit()
    print(f" Добавлена торговая точка на {этаж} этаже, {площадь} кв.м")
    return cursor.lastrowid

def edit_trading_point(conn, id_точки, этаж=None, площадь=None, наличие_кондиционера=None, стоимость_аренды_в_день=None):
    """ Редактирование существующей торговой точки """
    try:
        cursor = conn.cursor()
        
        # Проверяем существование точки
        cursor.execute("SELECT * FROM Торговая_точка WHERE id = ?", (id_точки,))
        if not cursor.fetchone():
            print(f" Торговая точка с ID {id_точки} не найдена")
            return False
        
        # Формируем запрос для обновления только переданных полей
        updates = []
        params = []
        
        if этаж is not None:
            updates.append("этаж = ?")
            params.append(этаж)
        if площадь is not None:
            updates.append("площадь = ?")
            params.append(площадь)
        if наличие_кондиционера is not None:
            updates.append("наличие_кондиционера = ?")
            params.append(наличие_кондиционера)
        if стоимость_аренды_в_день is not None:
            updates.append("стоимость_аренды_в_день = ?")
            params.append(стоимость_аренды_в_день)
        
        if not updates:
            print(" Не указаны поля для редактирования")
            return False
        
        params.append(id_точки)
        sql = f"UPDATE Торговая_точка SET {', '.join(updates)} WHERE id = ?"
        
        cursor.execute(sql, params)
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f" Торговая точка ID {id_точки} успешно обновлена")
            return True
        else:
            print(" Не удалось обновить торговую точку")
            return False
            
    except Error as e:
        print(f" Ошибка при редактировании: {e}")
        return False

def delete_trading_point(conn, id_точки):
    """ Удаление торговой точки """
    try:
        cursor = conn.cursor()
        
        # Сначала проверяем существование точки
        cursor.execute("SELECT * FROM Торговая_точка WHERE id = ?", (id_точки,))
        точка = cursor.fetchone()
        
        if not точка:
            print(f" Торговая точка с ID {id_точки} не найдена")
            return False
        
        # Показываем информацию о точке перед удалением
        print(f"\n УДАЛЕНИЕ ТОРГОВОЙ ТОЧКИ:")
        print(f"   ID: {точка[0]}")
        print(f"   Этаж: {точка[1]}")
        print(f"   Площадь: {точка[2]} кв.м")
        print(f"   Кондиционер: {'Да' if точка[3] else 'Нет'}")
        print(f"   Стоимость: {точка[4]} руб/день")
        
        # Запрос подтверждения
        подтверждение = input("\n Вы уверены, что хотите удалить эту точку? (да/нет): ").lower()
        if подтверждение in ['да', 'yes', 'y', 'д']:
            cursor.execute("DELETE FROM Торговая_точка WHERE id = ?", (id_точки,))
            conn.commit()
            
            if cursor.rowcount > 0:
                print(f" Торговая точка ID {id_точки} успешно удалена")
                return True
            else:
                print(" Не удалось удалить торговую точку")
                return False
        else:
            print(" Удаление отменено")
            return False
            
    except Error as e:
        print(f" Ошибка при удалении: {e}")
        return False

def get_trading_point_by_id(conn, id_точки):
    """ Получение информации о конкретной торговой точке """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Торговая_точка WHERE id = ?", (id_точки,))
        точка = cursor.fetchone()
        
        if точка:
            print(f"\n ИНФОРМАЦИЯ О ТОЧКЕ ID {id_точки}:")
            print("-" * 40)
            print(f"   Этаж: {точка[1]}")
            print(f"   Площадь: {точка[2]} кв.м")
            print(f"   Кондиционер: {'Да' if точка[3] else '❌ Нет'}")
            print(f"   Стоимость аренды: {точка[4]} руб/день")
            print("-" * 40)
            return точка
        else:
            print(f" Торговая точка с ID {id_точки} не найдена")
            return None
    except Error as e:
        print(f" Ошибка при получении данных: {e}")
        return None

def get_all_trading_points(conn):
    """ Получение всех торговых точек """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Торговая_точка")
    rows = cursor.fetchall()
    
    print("\n" + "="*80)
    print(" СПИСОК ВСЕХ ТОРГОВЫХ ТОЧЕК")
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
        print(f"   Кондиционер: {' Да' if row[3] else 'Нет'}")
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
        print("Точки с кондиционером не найдены")
        return
    
    for row in rows:
        print(f"ID: {row[0]}, Этаж: {row[1]}, Площадь: {row[2]} кв.м, Стоимость: {row[4]} руб")

def calculate_total_income(conn):
    """ Расчет общего дохода в день """
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(стоимость_аренды_в_день) FROM Торговая_точка")
    total = cursor.fetchone()[0]
    
    print(f"\n Общий потенциальный доход в день: {total or 0} руб")

def add_sample_data(conn):
    """ Добавление тестовых данных """
    sample_data = [
        (1, 50.5, True, 2500),
        (2, 30.0, False, 1800),
        (1, 75.2, True, 3500),
        (3, 45.0, True, 2200),
        (2, 60.0, False, 2000),
        (1, 35.5, True, 1900),
        (3, 80.0, True, 4000)
    ]
    
    print("\n📥 Добавление тестовых данных...")

for data in sample_data:
        add_trading_point(conn, *data)

def demonstrate_edit_delete_functions(conn):
    """ Демонстрация работы функций редактирования и удаления """
    print("\n" + "="*60)
    print("ДЕМОНСТРАЦИЯ ФУНКЦИЙ РЕДАКТИРОВАНИЯ И УДАЛЕНИЯ")
    print("="*60)
    
    print("\n Точки до изменений:")
    get_all_trading_points(conn)
    
    print("\n РЕДАКТИРОВАНИЕ: Меняем стоимость у точки ID 1")
    get_trading_point_by_id(conn, 1)
    edit_trading_point(conn, 1, стоимость_аренды_в_день=3000)
    print("После редактирования:")
    get_trading_point_by_id(conn, 1)
    
    print("\n РЕДАКТИРОВАНИЕ: Меняем этаж и добавляем кондиционер у точки ID 2")
    get_trading_point_by_id(conn, 2)
    edit_trading_point(conn, 2, этаж=1, наличие_кондиционера=True)
    print("После редактирования:")
    get_trading_point_by_id(conn, 2)
    
    # Демонстрация удаления (закомментировано, чтобы не удалять данные)
    # print("\n УДАЛЕНИЕ: Удаляем точку ID 7")
    # delete_trading_point(conn, 7)
    
    print("\n Точки после изменений:")
    get_all_trading_points(conn)

def main():
    """ Основная функция приложения """
    database = "trading_rent.db"
    
    print("ПРИЛОЖЕНИЕ ДЛЯ АРЕНДЫ ТОРГОВЫХ ПЛОЩАДЕЙ")
    print("С ФУНКЦИЯМИ УДАЛЕНИЯ И РЕДАКТИРОВАНИЯ")
    print("="*50)
    
    conn = create_connection(database)
    
    if conn is not None:
        create_table(conn)
        
        add_sample_data(conn)
        
        get_all_trading_points(conn)
        
        search_by_floor(conn, 1)
        search_by_floor(conn, 2)
        
        get_points_with_air_conditioning(conn)
        
        calculate_total_income(conn)
        
        demonstrate_edit_delete_functions(conn)
        
        # Закрытие соединения
        conn.close()
        print(f"\n Приложение завершило работу. База данных сохранена в файле: {database}")
    else:
        print(" Ошибка! Не удалось создать соединение с базой данных.")

if name == '__main__':
    main()
