class Vehicle:
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
        self.__COLOR_VARIANTS = ["blue", "red", "green", "black", "white"]

    def get_model(self):
        return f'Модель: {self.__model}'

    def horse_power(self):
        return f'Мощность двигателя: {self.__engine_power}hp'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.horse_power())
        print(self.get_color())
        print(f'владелец: {self.owner}')

    def __contains__(self, new_color):
        return new_color.lower() in self.__COLOR_VARIANTS.lower()

    def set_color(self, new_color):
        for color in self.__COLOR_VARIANTS:
            if new_color.lower() == color.lower():
                self.__color = new_color
                return
        print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)
        self.__PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
