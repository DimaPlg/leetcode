# Задача 3
# Евгения создала класс KgToPounds с параметром kg, куда передается определенное количество килограмм,
# а с помощью метода to_pounds() они переводятся в фунты. Чтобы закрыть доступ к переменной kg она
# реализовала методы set_kg() - для задания нового значения килограммов, get_kg() - для вывода текущего значения кг.
# Из-за этого возникло неудобство: нам нужно теперь использовать эти 2 метода для задания и вывода значений.
# Помогите ей переделать класс с использованием функции property() и свойств-декораторов. Код приведен ниже.
from dataclasses import dataclass
from typing import NamedTuple

from django.template.defaultfilters import length


class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205


    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')

#
# Николай – оригинальный человек.
# Он решил создать класс Nikola, принимающий при инициализации 2 параметра: имя и возраст. Но на этом он не успокоился.
# Не важно, какое имя передаст пользователь при создании экземпляра, оно всегда будет содержать “Николая”.
# В частности - если пользователя на самом деле зовут Николаем, то с именем ничего не произойдет, а если его зовут,
# например, Максим, то оно преобразуется в “Я не Максим, а Николай”.
# Более того, никаких других атрибутов и методов у экземпляра не может быть добавлено, даже если кто-то и вздумает
# так поступить (т.е. если некий пользователь решит прибавить к экземпляру свойство «отчество» или метод «приветствие»,
# то ничего у такого хитреца не получится).

class Nikola:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        if name == 'Nikola':
            self.name = name
        else:
            self.name = f' Я не {name}, а Николай'
        self.age = age


# pound1 = KgToPounds(3)
# print(pound1.to_pounds())
# print(pound1.kg)
# pound1.kg = '23'

nik = Nikola(name='Mihail', age=2)
print(nik.name)

# Строки в Питоне сравниваются на основании значений символов. Т.е. если мы захотим выяснить, что больше:
# Apple или Яблоко, – то Яблоко окажется бОльшим. А все потому, что английская буква A имеет значение 65
# (берется из таблицы кодировки), а русская буква Я – 1071 (с помощью функции ord() это можно выяснить).
# Такое положение дел не устроило Анну. Она считает, что строки нужно сравнивать по количеству входящих в них символов.
#
# Для этого девушка создала класс RealString и реализовала озвученный инструментарий. Сравнивать между собой
# можно как объекты класса, так и обычные строки с экземплярами класса RealString. К слову, Анне понадобилось только
# 3 метода внутри класса (включая __init__()) для воплощения задуманного.

class RealString:

    def __init__(self, line):
        self.line = str(line)

    def __eq__(self, other):
        if not isinstance(other, RealString):
            other = RealString(other)
        return len(self.line) == len(other.line)

    def __lt__(self, other):
        if not isinstance(other, RealString):
            other = RealString(other)
        return len(self.line) < len(other.line)

    def __le__(self, other):
        return self == other or self < other

str1 = RealString('fwd')
str2 = RealString(34224)
str3 = RealString([1,'12',34])
str4 = 45646
str5 = 'edgfsg'
print(str1 <= str4)
print(str3 <= str4)
print(str2 <= str5)
