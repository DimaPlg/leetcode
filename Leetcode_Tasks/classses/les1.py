# Задача 1
# Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации
# (отвечающий за добавку к выбираемому лимонаду). В этом классе реализуйте метод show_my_drink(),
# выводящий на печать Газировка и {ДОБАВКА} в случае наличия добавки, а иначе отобразится следующая фраза:
# Обычная газировка.

class Soda:
    def __init__(self, topping = None):
        self.topping = topping

    def show_my_drink(self):
        if self.topping is None:
            print('Обычная газировка')
        else:
            print(f'Газировка и {self.topping}')

s1 = Soda()
s1.show_my_drink()
s2 = Soda('малина')
s2.show_my_drink()

# Задача 2
# Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
# Для этого он решил создать класс TriangleChecker, принимающий только положительные числа.
# С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
# – Ура, можно построить треугольник!;
# – С отрицательными числами ничего не выйдет!;
# – Нужно вводить только числа!;
# – Жаль, но из этого треугольник не сделать.

class TriangleChecker:

    def __init__(self, sides):
        self.sides = sides

    def is_triangle(self):
        if all(isinstance(side, (int, float)) for side in self.sides):
            if min(self.sides) > 0:
                if 2 * max(self.sides) < sum(self.sides):
                    return 'Ура, можно построить треугольник!'
                else:
                    return 'Жаль, но из этого треугольник не сделать.'
            return 'С отрицательными числами ничего не выйдет!'
        return 'Нужно вводить только числа!'

triangle1 = TriangleChecker([2, 3, 4])
print(triangle1.is_triangle())
triangle2 = TriangleChecker([77, 3, 4])
print(triangle2.is_triangle())
triangle3 = TriangleChecker([77, 3, 'Сторона3'])
print(triangle3.is_triangle())
triangle4 = TriangleChecker([77, -3, 4])
print(triangle4.is_triangle())