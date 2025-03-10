import unittest
import tests12_3

testST = unittest.TestSuite()
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests12_3.TournamentTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests12_3.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testST)
