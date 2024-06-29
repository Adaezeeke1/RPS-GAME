import unittest
from game.rps import RPS


class TestRPS(unittest.TestCase):
    def test_rps_enum(self):
        self.assertEqual(RPS.ROCK.value, 1)
        self.assertEqual(RPS.PAPER.value, 2)
        self.assertEqual(RPS.SCISSORS.value, 3)


if __name__ == "__main__":
    unittest.main()
