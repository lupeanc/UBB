import random

from src.board import ConnectFourBoard


class ComputerStrategy:
    def __init__(self, board:ConnectFourBoard):
        self.__board = board

    def place_chips(self):
        """
        Places chips for computer
        """
        available_choices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        valid = 0
        while valid == 0:
            coords = [random.choice(available_choices), random.randint(0, 7)]
            try:
                self.__board.place_chip(coords, 2)
                valid = 1
            except Exception:
                pass

class ConnectFour:
    def __init__(self):
        self.__board = ConnectFourBoard()
        self.__computer_strategy = ComputerStrategy(self.__board)

    @property
    def c4_board(self):
        return self.__board

    def place_chip_player(self, tokens, turn):
        self.__board.place_chip(tokens, turn)

    def place_chip_computer(self):
        self.__computer_strategy.place_chips()