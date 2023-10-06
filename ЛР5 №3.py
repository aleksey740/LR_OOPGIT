#Определение класса Student с конструктором и методамии.
class Student:
    def __init__(self, name, group_num, grades):
        self.full_name = name          #имя студента.
        self.group_number = group_num  #номер группы.
        self.grades = grades           #список оценок.
    def calculate_average_grade(self):
        if not self.grades:
            return 0.0                  #Если список оценок пуст, вернуть 0.0
        return sum(self.grades) / len(self.grades)  #Вернуть средний балл студента.
    def print_info(self):
        print("ФИ:", self.full_name)      #Вывод полного имени студента.
        print("Номер группы:", self.group_number)  #Вывод номера группы.
        print("Успеваемость:", self.grades)        #Вывод списка оценок.
        print("Средний балл:", self.calculate_average_grade())  #Вывод среднего балла.
        print("\n")
#Сооздание списка данных.
students_data = [
    ("Мишенков Иван", "ПО-21", [9, 5, 8, 10, 9]),
    ("Прокопчик Егор", "ПО-21", [5, 9, 7, 8, 8]),
    ("Побединский Архип", "ПО-21", [6, 8, 10, 7, 9]),
    ("Полторжицкий Никита", "ПО-21", [6, 5, 8, 9, 8]),
    ("Мацкойть Максим", "ПО-21", [8, 9, 8, 7, 9]),
    ("Шорец Иван", "ПО-21", [9, 10, 8, 9, 9]),
    ("Шанько Дмитрий", "ПО-21", [8, 5, 9, 8, 7]),
    ("Котович Владислав", "ПО-21", [10, 7, 6, 9, 8]),
    ("Дубовский Александр", "ПО-21", [9, 9, 8, 9, 9]),
    ("Савич Артем", "ПО-21", [9, 10, 9, 9, 8]),
]
students = []  #Создание пустого списка для объектов студентов.
for data in students_data:
    student = Student(data[0], data[1], data[2])  #Создание объекта Student и передача данных.
    students.append(student)  #Добавление объекта студента в список.
#Сортировка студентов по возрастанию среднего балла, используя метод calculate_average_grade.
students.sort(key=Student.calculate_average_grade)
#Вывод информации о студентах.
for student in students:
    student.print_info()
