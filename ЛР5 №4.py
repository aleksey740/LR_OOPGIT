class Counter:
    #Конструктор класса, инициализирует счетчик начальным значением
    def __init__(self):
        self.value = 0
    #Метод start_from, устанавливает начальное значение счетчика
    def start_from(self, initial_value=0):
        self.value = initial_value
    #Метод increment, увеличивает значение счетчика на 1
    def increment(self):
        self.value += 1
    #Метод display, выводит текущее значение счетчика
    def display(self):
        print(f"Текущее значение счетчика = {self.value}")
    #Метод reset, сбрасывает счетчик в начальное значение (0)
    def reset(self):
        self.value = 0
#ппример использования класса Counter
c1 = Counter()
c1.start_from()
c1.increment()
c1.display()  #печатает текущее значение счетчика = 1
c1.increment()
c1.display()  #печатает текущее значение счетчика = 2
c1.reset()
c1.display()  #печатает текущее значение счетчика = 0

c2 = Counter()
c2.start_from(3)
c2.display()  #печатает текущее значение счетчика = 3
c2.increment()
c2.display()  #печатает текущее значение счетчика = 4
