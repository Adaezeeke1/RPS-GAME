import unittest
from game.computer import Computer
from game.rps import RPS


class TestComputer(unittest.TestCase):
    def test_get_choice(self):
        computer = Computer()
        for _ in range(10):
            choice = computer.get_choice()
            self.assertIn(choice, list(RPS))


if __name__ == "__main__":
    unittest.main()
