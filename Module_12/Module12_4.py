import logging
import unittest

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")
class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            run1 = Runner('Jack', -5)
            for _ in range(1, 11):
                run1.walk()
            self.assertEqual(run1.distance, 50)
            logging.info('"test_walk" успешно выполнен')
        except ValueError as err:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            run2 = Runner(17, 12)
            for _ in range(1, 11):
                self.assertEqual(run2.distance, 100)
            logging.info('"test_run" успешно выполнен')
        except TypeError as err:
            logging.warning('Неверный тип данных для обьекта Runner')

    def test_challenge(self):
        run3 = Runner('Dave')
        run4 = Runner('Ed')
        for _ in range(1, 11):
            run3.walk()
        for _ in range(1, 11):
            run4.run()


if __name__ == '__main__':
    unittest.main()

# first = Runner('Вося', -5)
# second = Runner(17, 5)
# third = Runner('Арсен', 10)

# t = Tournament(101, first, second)
# print(t.start())
