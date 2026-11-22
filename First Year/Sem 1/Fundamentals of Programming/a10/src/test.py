from src.board import ConnectFourBoard
import unittest
from unittest.mock import MagicMock


class TestPlaceChip(unittest.TestCase):

    def setUp(self):
        """Set up a GameBoard instance before each test."""
        self.board = ConnectFourBoard()
        self.board.data = [[" " for _ in range(7)] for _ in range(6)]  # A 6x7 grid

    def test_place_chip_valid_player_move(self):
        """Test placing a chip for the player in a valid position."""
        self.board.calculate_chip_coords = MagicMock(return_value=(5, 0))  # Bottom-left corner
        self.board.gravity_check = MagicMock(return_value=True)
        self.board.is_space_available = MagicMock(return_value=True)
        self.board.check_if_won = MagicMock(return_value=False)
        self.board.check_if_full = MagicMock(return_value=False)

        self.board.place_chip(["A", 5], turn=1)

        self.assertEqual(self.board.data[5][0], "🔵")
        self.board.check_if_won.assert_called_with("🔵")

    def test_place_chip_valid_computer_move(self):
        """Test placing a chip for the computer in a valid position."""
        self.board.calculate_chip_coords = MagicMock(return_value=(5, 1))  # Bottom second column
        self.board.gravity_check = MagicMock(return_value=True)
        self.board.is_space_available = MagicMock(return_value=True)
        self.board.check_if_won = MagicMock(return_value=False)
        self.board.check_if_full = MagicMock(return_value=False)

        self.board.place_chip(["B", 5], turn=2)

        self.assertEqual(self.board.data[5][1], "🔴")
        self.board.check_if_won.assert_called_with("🔴")

    def test_place_chip_game_won(self):
        """Test that a GameOver exception is raised when the game is won."""
        self.board.calculate_chip_coords = MagicMock(return_value=(5, 2))
        self.board.gravity_check = MagicMock(return_value=True)
        self.board.is_space_available = MagicMock(return_value=True)
        self.board.check_if_won = MagicMock(return_value=True)

    def test_place_chip_board_full(self):
        """Test that a GameOver exception is raised when the board is full."""
        self.board.calculate_chip_coords = MagicMock(return_value=(5, 3))
        self.board.gravity_check = MagicMock(return_value=True)
        self.board.is_space_available = MagicMock(return_value=True)
        self.board.check_if_won = MagicMock(return_value=False)
        self.board.check_if_full = MagicMock(return_value=True)

    def test_place_chip_invalid_position(self):
        """Test that a ValueError is raised for an invalid position."""
        self.board.calculate_chip_coords = MagicMock(return_value=(5, 4))
        self.board.gravity_check = MagicMock(return_value=False)

        with self.assertRaises(ValueError):
            self.board.place_chip(["E", 5], turn=1)

    def test_place_chip_space_unavailable(self):
        """Test that a ValueError is raised when the space is unavailable."""
        self.board.calculate_chip_coords = MagicMock(return_value=(5, 5))
        self.board.gravity_check = MagicMock(return_value=True)
        self.board.is_space_available = MagicMock(return_value=False)

        with self.assertRaises(ValueError):
            self.board.place_chip(["F", 5], turn=1)


if __name__ == "__main__":
    unittest.main()