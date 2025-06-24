"""
Вариант 30
Создайте базовый класс "Фигура" со свойствами "ширина" и "высота". 
От этого класса унаследуйте классы "Прямоугольник" и "Квадрат". Для класса "Квадрат"
"""

class Figure:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Фигура: ширина = {self.width}, высота = {self.height}"


class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__(width, height)

    def __str__(self):
        return f"Прямоугольник: ширина = {self.width}, высота = {self.height}"


class Square(Figure):
    def __init__(self, side):
        super().__init__(side, side) 
    def __str__(self):
        return f"Квадрат: сторона = {self.width}" 
