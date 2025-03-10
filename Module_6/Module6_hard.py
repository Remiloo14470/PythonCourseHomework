import math


class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count

        self.__color = color if self.__is_valid_color(*color) else (0, 0, 0)
        self.filled = False

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        else:
            print("Некорректные значения цвета. Цвет остается прежним.")

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print(f"Некорректные значения сторон. Стороны остаются прежними. Требуется {self.sides_count} сторон.")

    def __is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in sides)

    def __len__(self):
        return sum(self.__sides)

    def info(self):
        return f"Figure: sides={self.__sides}, color={self.__color}, filled={self.filled}, perimeter={len(self)}"


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        self.__radius = self.__calculate_radius(self.get_sides()[0])

    def __calculate_radius(self, circumference):
        return circumference / (2 * math.pi)

    def get_radius(self):
        return self.__radius

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def info(self):
        return (f"Circle: radius={self.get_radius()}, color={self.get_color()}, "
                f"filled={self.filled}, circumference={self.get_sides()[0]}, area={self.get_square()}")


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        self.__height = self.__calculate_height(*self.get_sides())

    def __calculate_height(self, side1, side2, side3):
        s = (side1 + side2 + side3) / 2  # Полупериметр
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))  # Площадь по формуле Герона
        return 2 * area / side1  # Высота, если side1 — основание

    def get_height(self):
        return self.__height

    def get_square(self):
        return 0.5 * self.get_sides()[0] * self.__height

    def info(self):
        return (f"Triangle: sides={self.get_sides()}, height={self.get_height()}, color={self.get_color()}, "
                f"filled={self.filled}, area={self.get_square()}")

class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0, 0, 0), *sides):
        if len(sides) != 1:
            sides = [1]
        super().__init__(color, *([sides[0]] * self.sides_count))

    def get_volume(self):
        return self.get_sides()[0] ** 3


    def info(self):
        return (f"Cube: side_length={self.get_sides()[0]}, color={self.get_color()}, "
                f"filled={self.filled}, volume={self.get_volume()}")


# Примеры создания объектов и проверки их работы:

# Создаем круг с одной стороной (10) и цветом (200, 200, 100)
circle1 = Circle((200, 200, 100), 10)

# Создаем куб с одной стороной (6) и цветом (222, 35, 130)
cube1 = Cube((222, 35, 130), 6)

# Проверка изменения цветов:

# Изменяем цвет круга на (55, 66, 77)
circle1.set_color(55, 66, 77)  # Изменится, так как цвет корректен
print(circle1.get_color())  # Ожидаемый вывод: [55, 66, 77]

# Пытаемся изменить цвет куба на некорректный (300, 70, 15)
cube1.set_color(300, 70, 15)  # Не изменится, так как r > 255
print(cube1.get_color())  # Ожидаемый вывод: [222, 35, 130]

# Проверка изменения сторон:

# Пытаемся изменить стороны куба с некорректным количеством сторон (5 вместо 12)
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится, так как нужно 12 сторон
print(cube1.get_sides())  # Ожидаемый вывод: [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

# Изменяем сторону круга на новую длину (15)
circle1.set_sides(15)  # Изменится, так как sides_count для круга = 1
print(circle1.get_sides())  # Ожидаемый вывод: [15]

# Проверка периметра (длины) круга:

# Получаем длину окружности круга (периметр)
print(len(circle1))  # Ожидаемый вывод: 15

# Проверка объема куба:

# Получаем объем куба
print(cube1.get_volume())  # Ожидаемый вывод: 216
