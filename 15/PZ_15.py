"""
Вариант 30
Приложение СДАЧА В АРЕНДУ ТОРГОВЫХ ПЛОЩАДЕЙ для искогорой организации.
БД должна содержать таблицу Торговая точка со следующей структурой записи: этаж, площадь, наличие кондиционера и стоимость аренды в день.
"""

import sqlite3
from datetime import datetime

class TradePointDB:
    def __init__(self, db_name="trade_points.db"):
        self.db_name = db_name
        self.create_table()
    
    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Торговая_точка (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                этаж INTEGER NOT NULL,
                площадь REAL NOT NULL,
                кондиционер BOOLEAN NOT NULL,
                стоимость_аренды REAL NOT NULL,
                дата_добавления TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def add_sample_data(self):
        sample_data = [
            (1, 25.5, True, 1500.0),
            (1, 18.0, False, 1200.0),
            (2, 35.0, True, 2000.0),
            (2, 28.5, True, 1800.0),
            (3, 42.0, True, 2500.0),
            (1, 15.0, False, 1000.0),
            (3, 30.0, False, 1700.0),
            (2, 22.0, True, 1600.0),
            (1, 20.0, True, 1400.0),
            (3, 38.0, True, 2200.0)
        ]
        
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.executemany('''
            INSERT INTO Торговая_точка (этаж, площадь, кондиционер, стоимость_аренды)
            VALUES (?, ?, ?, ?)
        ''', sample_data)
        
        conn.commit()
        conn.close()
        print("Добавлено 10 примеров торговых точек")
    
    def add_trade_point(self):
        print("\n--- ДОБАВЛЕНИЕ НОВОЙ ТОРГОВОЙ ТОЧКИ ---")
        
        try:
            floor = int(input("Введите этаж: "))
            area = float(input("Введите площадь (м²): "))
            ac_input = input("Наличие кондиционера (да/нет): ").lower()
            ac = True if ac_input in ['да', 'д', 'yes', 'y'] else False
            price = float(input("Введите стоимость аренды в день: "))
            
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO Торговая_точка (этаж, площадь, кондиционер, стоимость_аренды)
                VALUES (?, ?, ?, ?)
            ''', (floor, area, ac, price))
            
            conn.commit()
            conn.close()
            print("Торговая точка успешно добавлена!")
            
        except ValueError:
            print("Ошибка ввода данных!")
        except Exception as e:
            print(f"Ошибка при добавлении: {e}")
    
    def search_trade_points(self):
        print("\n--- ПОИСК ТОРГОВЫХ ТОЧЕК ---")
        print("1. Поиск по этажу")
        print("2. Поиск по диапазону площади")
        print("3. Поиск точек с кондиционером и максимальной стоимости")
        
        try:
            choice = int(input("Выберите тип поиска (1-3): "))
            
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            if choice == 1:
                floor = int(input("Введите этаж для поиска: "))
                cursor.execute('''
                    SELECT * FROM Торговая_точка 
                    WHERE этаж = ?
                ''', (floor,))
                
            elif choice == 2:
                min_area = float(input("Минимальная площадь: "))
                max_area = float(input("Максимальная площадь: "))
                cursor.execute('''
                    SELECT * FROM Торговая_точка 
                    WHERE площадь BETWEEN ? AND ?
                ''', (min_area, max_area))
                
            elif choice == 3:
              max_price = float(input("Максимальная стоимость аренды: "))
                cursor.execute('''
                    SELECT * FROM Торговая_точка 
                    WHERE кондиционер = ? AND стоимость_аренды <= ?
                ''', (True, max_price))
                
            else:
                print("Неверный выбор!")
                return
            
            results = cursor.fetchall()
            self.display_results(results)
            conn.close()
            
        except ValueError:
            print("Ошибка ввода данных!")
        except Exception as e:
            print(f"Ошибка при поиске: {e}")
    
    def delete_trade_points(self):
        print("\n--- УДАЛЕНИЕ ТОРГОВЫХ ТОЧЕК ---")
        print("1. Удаление по ID")
        print("2. Удаление точек на определенном этаже")
        print("3. Удаление точек с площадью меньше указанной")
        
        try:
            choice = int(input("Выберите тип удаления (1-3): "))
            
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            if choice == 1:
                point_id = int(input("Введите ID точки для удаления: "))
                cursor.execute('''
                    DELETE FROM Торговая_точка 
                    WHERE id = ?
                ''', (point_id,))
                
            elif choice == 2:
                floor = int(input("Введите этаж для удаления всех точек: "))
                cursor.execute('''
                    DELETE FROM Торговая_точка 
                    WHERE этаж = ?
                ''', (floor,))
                
            elif choice == 3:
                min_area = float(input("Удалить точки с площадью меньше: "))
                cursor.execute('''
                    DELETE FROM Торговая_точка 
                    WHERE площадь < ?
                ''', (min_area,))
                
            else:
                print("Неверный выбор!")
                return
            
            conn.commit()
            deleted_count = cursor.rowcount
            conn.close()
            
            print(f"Удалено записей: {deleted_count}")
            
        except ValueError:
            print("Ошибка ввода данных!")
        except Exception as e:
            print(f"Ошибка при удалении: {e}")
    
    def update_trade_points(self):
        print("\n--- РЕДАКТИРОВАНИЕ ТОРГОВЫХ ТОЧЕК ---")
        print("1. Изменение стоимости аренды для этажа")
        print("2. Добавление кондиционера точкам на этаже")
        print("3. Увеличение стоимости для точек с кондиционером")
        
        try:
            choice = int(input("Выберите тип редактирования (1-3): "))
            
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            if choice == 1:
                floor = int(input("Введите этаж: "))
                new_price = float(input("Новая стоимость аренды: "))
                cursor.execute('''
                    UPDATE Торговая_точка 
                    SET стоимость_аренды = ? 
                    WHERE этаж = ?
                ''', (new_price, floor))
                
            elif choice == 2:
                 floor = int(input("Введите этаж: "))
                cursor.execute('''
                    UPDATE Торговая_точка 
                    SET кондиционер = ? 
                    WHERE этаж = ?
                ''', (True, floor))
                
            elif choice == 3:
                increase_percent = float(input("Процент увеличения стоимости: "))
                cursor.execute('''
                    UPDATE Торговая_точка
                    SET стоимость_аренды = стоимость_аренды * (1 + ? / 100)
                    WHERE кондиционер = ?
                ''', (increase_percent, True))
                
            else:
                print("Неверный выбор!")
                return
            
            conn.commit()
            updated_count = cursor.rowcount
            conn.close()
            
            print(f"Обновлено записей: {updated_count}")
            
        except ValueError:
            print("Ошибка ввода данных!")
        except Exception as e:
            print(f"Ошибка при редактировании: {e}")
    
    def display_all_points(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM Торговая_точка')
        results = cursor.fetchall()
        
        print("\n--- ВСЕ ТОРГОВЫЕ ТОЧКИ ---")
        self.display_results(results)
        
        conn.close()
    
    def display_results(self, results):
        if not results:
            print("Записи не найдены")
            return
        
        print(f"\n{'ID':<4} {'Этаж':<6} {'Площадь':<10} {'Кондиц.':<8} {'Стоимость':<12} {'Дата добавления':<20}")
        print("-" * 70)
        
        for row in results:
            ac_status = "Да" if row[3] else "Нет"
            print(f"{row[0]:<4} {row[1]:<6} {row[2]:<10} {ac_status:<8} {row[4]:<12} {row[5]:<20}")

def main():
    db = TradePointDB()
    
    while True:
        print("\n=== СИСТЕМА АРЕНДЫ ТОРГОВЫХ ПЛОЩАДЕЙ ===")
        print("1. Добавить примеры данных (10 позиций)")
        print("2. Добавить новую торговую точку")
        print("3. Поиск торговых точек")
        print("4. Удаление торговых точек")
        print("5. Редактирование торговых точек")
        print("6. Показать все торговые точки")
        print("7. Выход")
        
        try:
            choice = int(input("Выберите действие: "))
            
            if choice == 1:
                db.add_sample_data()
            elif choice == 2:
                db.add_trade_point()
            elif choice == 3:
                db.search_trade_points()
            elif choice == 4:
                db.delete_trade_points()
            elif choice == 5:
                db.update_trade_points()
            elif choice == 6:
                db.display_all_points()
            elif choice == 7:
                print("Выход из программы")
                break
            else:
                print("Неверный выбор!")
                
        except ValueError:
            print("Ошибка ввода! Введите число от 1 до 7")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if name == "__main__":
    main()

                
