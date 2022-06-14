"""
1. Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду).
В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».
"""


class Soda:
    def __init__(self, ingr):
        self.ingr = ingr

    def show_my_drink(self):
        if self.ingr:
            print("Газировка с добавкой " + self.ingr)
        else:
            print("Обычная газировка")


additional = "мята" or None  # оставить нужное

make_soda = Soda(additional)

make_soda.show_my_drink()

"""
2. Николай – оригинальный человек. 
Он решил создать класс Nikola, принимающий при инициализации 2 параметра: имя и возраст. Но на этом он не успокоился. 
Не важно, какое имя передаст пользователь при создании экземпляра, оно всегда будет содержать “Николая”. 
В частности - если пользователя на самом деле зовут Николаем, то с именем ничего не произойдет, а если его зовут, например, Максим, то оно преобразуется в “Я не Максим, а Николай”.
Более того, никаких других атрибутов и методов у экземпляра не может быть добавлено, даже если кто-то и вздумает так поступить (т.е. если некий пользователь решит прибавить к экземпляру свойство «отчество» или метод «приветствие», то ничего у такого хитреца не получится).
Для ограничения количества наборов свойств и методов в экземпляре применяется специальный магический атрибут __slots__.
"""


class Nikola:
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age
        if self.name != "Николай":
            print(f"Я не {name}, а Николай")


a = Nikola("Костя", 25)

"""
3. Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age. По умолчанию name = Ivan, age = 18, groupNumber = 10A.
Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge, setGroupNumber.
Метод getName нужен для получения данных об имени конкретного студента, метод getAge нужен для получения данных о возрасте конкретного студента, 
Mетод setGroupNumberнужен для получения данных о номере группы конкретного студента. 
Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, метод setGroupNumber позволяет изменить номер группы установленный по умолчанию.
В программе необходимо создать пять экземпляров класса Student, установить им разные имена, возраст и номер группы.
"""


class Student:
    def __init__(self):
        self.name = "Ivan"
        self.age = 18
        self.groupNumber = "10A"

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, group):
        self.groupNumber = group


# можно при создании объекта сразу закидывать нужные параметры чтоб не городить лишний код, но в условии вроде не так написано

a1 = Student()
a2 = Student()
a3 = Student()
a4 = Student()
a5 = Student()

a1.setNameAge("Ban", 25)
a1.setGroupNumber("B12")

a2.setNameAge("Klara", 21)
a2.setGroupNumber("B2")

print(a1.name, a1.age, a1.groupNumber)
print(a2.name, a2.age, a2.groupNumber)

"""
4. Напишите программу с классом Math. 
Создайте два атрибута — a и b. 
Напишите методы addition — сложение, multiplication — умножение,division— деление, subtraction — вычитание.
При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.
"""


class Math:
    a = 0
    b = 0

    def addition(self, a, b):
        return a + b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

    def subtraction(self, a, b):
        return a - b


proc = Math()
print(proc.subtraction(5, 6))


"""
5.Напишите программу с классом Car.
Создайте конструктор класса Car.
Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
Напишите пять методов.
Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
Третий — присвоение автомобилю года выпуска.
Четвертый метод — присвоение автомобилю типа.
Пятый — присвоение автомобилю цвета.
"""


class Car:
    def __init__(self):
        self.color = "red"
        self.type = "cabrio"
        self.year = 2022

    def start_engine(self):
        print("Автомобиль заведен")

    def stop_engine(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year

    def set_type(self, car_type):
        self.type = car_type

    def set_color(self, color):
        self.type = color
