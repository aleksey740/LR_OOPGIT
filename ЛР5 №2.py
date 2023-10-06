import math  #Импорт модуля math для использования функции sqrt.

class Triangle:
    # Конструктор класса.
    def __init__(self, a, b, c):
        self.a = a  #поле 'a' длиной первой стороны.
        self.b = b  #поле 'b' длиной второй стороны.
        self.c = c  #поле 'c' длиной третьей стороны.

    #Метод для вычисления периметра треугольника.
    def perimeter(self):
        p = self.a + self.b + self.c  #Вычисляем сумму длин всех сторон.
        return p  #Возвращаем результат.

    #Метод для вычисления площади треугольника по формуле Герона.
    def area(self):
        p = self.perimeter()  #Вычисляем периметр с помощью ранее определенного метода.
        s = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))  #Вычисляем площадь по формуле Герона.
        return s  #Возвращаем результат.

#Создаем объект треугольника с сторонами.
triangle = Triangle(5, 6, 7)

#Вывод результата.
print(f'P = {triangle.perimeter()}, (P = {triangle.a} + {triangle.b} + {triangle.c})')
print(f'S = {triangle.area()}, (S = {triangle.perimeter()}({triangle.perimeter()} - {triangle.a})({triangle.perimeter()} - {triangle.b})({triangle.perimeter()} - {triangle.c}))')
