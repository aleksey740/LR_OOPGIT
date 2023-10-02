#Определение класса C.
class C:
    #Конструктор класса C, который принимает аргументы a и b (со значением по умолчанию 5).
    def __init__(self, a, b=5):
        self.a = a  #Присваивание значения a атрибуту a объекта.
        self.b = b  #Присваивание значения b атрибуту b объекта.
    #Метод c, который возвращает сумму атрибутов a и b объекта.
    def c(self):
        return self.a + self.b
    #Метод d, который возвращает разность атрибутов a и b объекта.
    def d(self):
        return self.a - self.b
#Создание объекта a1 класса C с атрибутом a=5 и b=5 (по умолчанию).
a1 = C(5)
print(f'{a1.a} + {a1.b} = ', a1.c())  #Вывод результата сложения a и b через метод c().
#Создание объекта a2 класса C с атрибутами a=4 и b=6.
a2 = C(4, 6)
print(f'{a2.a} - {a2.b} = ', a2.d())  #Вывод результата вычитания a и b через метод d().
