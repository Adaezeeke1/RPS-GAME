import unittest
from unittest.mock import patch
from utils.input_handler import get_valid_input


class InputHandlerTest(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_valid_number_input(self, mock_input):
        # Test if get_valid_input returns the number itself for valid input
        result = get_valid_input("Enter a number", range(1, 4))
        self.assertEqual(result, 1)

    # @patch('builtins.input', side_effect=['4'])
    # def test_invalid_input(self, mock_input):
    #     result = get_valid_input("Enter a number", range(1, 4))
    #     self.assertEqual(result, "Invalid input. Please enter a valid number.")
    #
    # @patch('builtins.input', return_value="abc")
    # def test_invalid_input_non_integer(self, mock_input):
    #     result = get_valid_input("Enter a number", range(1, 4))
    #     self.assertIsNone(result)

    @patch('builtins.input', side_effect=['4', '1'])
    def test_invalid_input(self, mock_input):
        with self.assertLogs() as cm:
            get_valid_input("Enter a number", range(1, 4))
        self.assertIn("Invalid input. Please enter one of [1, 2, 3].", cm.output[0])

    @patch('builtins.input', side_effect=["abc", '1'])
    def test_invalid_input_non_integer(self, mock_input):
        with self.assertLogs() as cm:
            get_valid_input("Enter a number", range(1, 4))
        self.assertIn("Invalid input. Please enter a valid number.", cm.output[0])


if __name__ == '__main__':
    unittest.main()
