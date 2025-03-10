import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed


    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name and self.speed == other.speed


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
    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        run1 = Runner('Jack')
        for _ in range(1,11):
            run1.walk()
        self.assertEqual(run1.distance, 50)

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        run2 = Runner('Tom')
        for _ in range(1,11):
            run2.run()
        self.assertEqual(run2.distance, 100)

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run3 = Runner('Dave')
        run4 = Runner('Ed')
        for _ in range(1,11):
            run3.walk()
        for _ in range(1,11):
            run4.run()
        self.assertNotEqual(run3.distance, run4.distance)


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Yusane", 10)
        self.runner2 = Runner("Andrew", 9)
        self.runner3 = Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls):
        pass

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        tourn1 = Tournament(90, self.runner1, self.runner3)
        results = tourn1.start()
        self.all_results['tourn1'] = results
        self.assertTrue(results[1], self.runner1)

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        tourn2 = Tournament(90, self.runner2, self.runner3)
        results = tourn2.start()
        self.all_results['tourn2'] = results
        self.assertTrue(results[1], self.runner2)

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        tourn3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tourn3.start()
        self.all_results['tourn3'] = results
        self.assertTrue(results[1], self.runner1)


if __name__ == "__main__":
    unittest.main()
