import unittest
from unittest.mock import patch
from utils.input_handler import get_valid_input
from game.rps import RPS


class TestInputHandler(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '4', '2', '3'])
    def test_get_valid_input_enum(self, mock_input):
        valid_choices = list(map(RPS, range(1, 4)))
        self.assertEqual(get_valid_input("Enter choice: ", valid_choices, RPS), RPS.ROCK)
        self.assertEqual(get_valid_input("Enter choice: ", valid_choices, RPS), RPS.PAPER)
        self.assertEqual(get_valid_input("Enter choice: ", valid_choices, RPS), RPS.SCISSORS)

    @patch('builtins.input', side_effect=['y', 'n', 'z'])
    def test_get_valid_input_non_enum(self, mock_input):
        self.assertEqual(get_valid_input("Enter choice: ", ['y', 'n']), 'y')
        self.assertEqual(get_valid_input("Enter choice: ", ['y', 'n']), 'n')


if __name__ == "__main__":
    unittest.main()
