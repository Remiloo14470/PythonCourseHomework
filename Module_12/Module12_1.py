import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        run1 = Runner('Jack')
        for _ in range(1,11):
            run1.walk()
        self.assertEqual(run1.distance, 50)
    def test_run(self):
        run2 = Runner('Tom')
        for _ in range(1,11):
            run2.run()
        self.assertEqual(run2.distance, 100)

    def test_challenge(self):
        run3 = Runner('Dave')
        run4 = Runner('Ed')
        for _ in range(1,11):
            run3.walk()
        for _ in range(1,11):
            run4.run()
        self.assertNotEqual(run3.distance, run4.distance)


if __name__ == '__main__':
    unittest.main()
