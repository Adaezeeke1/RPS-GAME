import unittest
from unittest import TestCase, mock
from game.player import Player
from game.rps import RPS


class PlayerTest(TestCase):

    @mock.patch('utils.input_handler.get_valid_input', return_value=RPS.ROCK)
    def test_get_choice_rock(self, mock_get_valid_input):
        player = Player()
        choice = player.get_choice()
        self.assertEqual(choice, RPS.ROCK)

    @mock.patch('utils.input_handler.get_valid_input', return_value=RPS.PAPER)
    def test_get_choice_paper(self, mock_get_valid_input):
        player = Player()
        choice = player.get_choice()
        self.assertEqual(choice, RPS.PAPER)

    @mock.patch('utils.input_handler.get_valid_input', return_value=RPS.SCISSORS)
    def test_get_choice_scissors(self, mock_get_valid_input):
        player = Player()
        choice = player.get_choice()
        self.assertEqual(choice, RPS.SCISSORS)

    @mock.patch('utils.input_handler.get_valid_input', side_effect=['0', '4', 'abc', RPS.ROCK])
    def test_get_choice_invalid_input(self, mock_get_valid_input):
        player = Player()
        choice = player.get_choice()
        # Ensure the function continues to ask for input until valid
        self.assertEqual(choice, RPS.ROCK)

    # @mock.patch('utils.input_handler.get_valid_input', side_effect=ValueError('Invalid Input'))
    # def test_get_invalid_input(self, mock_get_valid_input):
    #     player = Player()
    #     with self.assertRaises(ValueError):
    #         player.get_choice()


if __name__ == '__main__':
    unittest.main()
