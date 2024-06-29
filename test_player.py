import unittest
from unittest.mock import patch
from game.player import Player
from game.rps import RPS


class TestPlayer(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '2', '3'])
    def test_get_choice(self, mock_input):
        player = Player()
        self.assertEqual(player.get_choice(), RPS.ROCK)
        self.assertEqual(player.get_choice(), RPS.PAPER)
        self.assertEqual(player.get_choice(), RPS.SCISSORS)


if __name__ == "__main__":
    unittest.main()
