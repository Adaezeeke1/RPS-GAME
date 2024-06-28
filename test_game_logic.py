import unittest
from unittest.mock import patch, MagicMock
from game.game_logic import RockPaperScissorsGame
from game.rps import RPS


class TestRockPaperScissorsGame(unittest.TestCase):
    def setUp(self):
        self.game = RockPaperScissorsGame()
        self.game.player.get_choice = MagicMock()
        self.game.computer.get_choice = MagicMock()

    def test_determine_winner(self):
        self.game.determine_winner(RPS.ROCK, RPS.SCISSORS)
        self.assertEqual(self.game.score["player"], 1)
        self.assertEqual(self.game.score["computer"], 0)

        self.game.determine_winner(RPS.PAPER, RPS.ROCK)
        self.assertEqual(self.game.score["player"], 2)
        self.assertEqual(self.game.score["computer"], 0)

        self.game.determine_winner(RPS.SCISSORS, RPS.PAPER)
        self.assertEqual(self.game.score["player"], 3)
        self.assertEqual(self.game.score["computer"], 0)

        self.game.determine_winner(RPS.SCISSORS, RPS.ROCK)
        self.assertEqual(self.game.score["player"], 3)
        self.assertEqual(self.game.score["computer"], 1)

        self.game.determine_winner(RPS.ROCK, RPS.ROCK)
        self.assertEqual(self.game.score["player"], 3)
        self.assertEqual(self.game.score["computer"], 1)

    @patch('builtins.input', side_effect=['y', 'n'])
    def test_play_again(self, mock_input):
        self.assertTrue(self.game.play_again())
        self.assertFalse(self.game.play_again())

    def test_display_choices(self):
        with patch('builtins.print') as mock_print:
            self.game.display_choices(RPS.ROCK, RPS.PAPER)
            mock_print.assert_any_call("\nYou chose: ROCK.")
            mock_print.assert_any_call("Python chose: PAPER.\n")

    def test_display_score(self):
        with patch('builtins.print') as mock_print:
            self.game.score = {"player": 1, "computer": 2, "ties": 3}
            self.game.display_score()
            mock_print.assert_any_call("Scoreboard:")
            mock_print.assert_any_call("You: 1")
            mock_print.assert_any_call("Python: 2")

    def test_final_winner_message(self):
        self.game.score = {"player": 2, "computer": 1}
        self.assertEqual(self.game.final_winner_message(), "\n🏆 Congrats! You smashed it!")

        self.game.score = {"player": 0, "computer": 3}
        self.assertEqual(self.game.final_winner_message(), "\n🤖 oof... Better luck next time!")

        self.game.score = {"player": 1, "computer": 1}
        self.assertEqual(self.game.final_winner_message(), "\n🤝 A tie! Good game!")


if __name__ == "__main__":
    unittest.main()
