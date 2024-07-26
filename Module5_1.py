import random


class House():
    def __init__(self, name, number_of_floors):
        self.number_of_floors = number_of_floors
        self.name = name
        print(self.name, self.number_of_floors)

    def go_to(self, new_floor):
        self.new_floor = new_floor
        new_floor = random.randint(1, new_floor)
        print(new_floor)
        if new_floor > self.number_of_floors or new_floor <1:
            print('Такого этажа не существует')


dom = House('ЖК Сердце города', 18)
dom.go_to(90)
