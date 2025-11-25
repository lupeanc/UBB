from texttable import Texttable
from src.repo_memory import GameOver


# aka C4 board hahaha get it cause C4 is a 'f- explosive'
class ConnectFourBoard:
    def __init__(self):
        self.data = []
        for i in range(6):
            self.data.append([None] * 7)

    @staticmethod
    def calculate_chip_coords(tokens):
        """
        Calculates the coords based on the inputted command
        :param tokens: split up position command (eg. A5 -> ['A', 5])
        :return: coordinates as a list (eg A5 -> [0, 5])
        """
        coords = [0] * 2
        if tokens[0] == 'A':
            coords[1] = 0
        elif tokens[0] == 'B':
            coords[1] = 1
        elif tokens[0] == 'C':
            coords[1] = 2
        elif tokens[0] == 'D':
            coords[1] = 3
        elif tokens[0] == 'E':
            coords[1] = 4
        elif tokens[0] == 'F':
            coords[1] = 5
        elif tokens[0] == 'G':
            coords[1] = 6
        else:
            raise ValueError("Invalid command")

        coords[0] = int(tokens[1])
        return coords

    def place_chip(self, tokens, turn):
        """
        Places the chip on the board
        :param tokens: split up position command (eg. A5 -> ['A', 5])
        :param turn: whose turn it is (player has uneven turns, computer has even turns)
        :raises GameOver if the board is full/if someone won
        """
        coords = self.calculate_chip_coords(tokens)
        if self.gravity_check(coords) and self.is_space_available(coords):
            # Player: turn 1
            if turn % 2 == 1:
                self.data[coords[0]][coords[1]] = '🔵'
                is_won = self.check_if_won('🔵')
                if is_won:
                    winner = '🔵'
            else:
                self.data[coords[0]][coords[1]] = '🔴'
                is_won = self.check_if_won('🔴')
                if is_won:
                    winner = '🔴'
        else:
            raise ValueError()

        is_full = self.check_if_full()
        if is_full:
            raise GameOver("Board is full")

        if is_won:
            raise GameOver(f"{winner} has won!")


    """
    CHECKERS
    """
    # Checks if the space inputted by the user already contains a chip
    def is_space_available(self, coords):
        """
        Checks if the space is empty or not
        :param coords: coordinates as a list (eg A5 -> [0, 5])
        :return: true if the space is empty, false if the space is already occupied
        """
        if self.data[coords[0]][coords[1]] == '🔴' or self.data[coords[0]][coords[1]] == '🔵':
            return False
        else:
            return True

    def gravity_check(self, coords):
        """
        Checks if placement respects the laws of gravity
        :param coords: coordinates as a list (eg A5 -> [0, 5])
        :return: true if chip is on the last row or if it has another chip under it, false if it doesn't have any respect for Isaac Newton
        """
        space_below = [None] * 2
        space_below[0] = coords[0] + 1
        space_below[1] = coords[1]

        # Case 1: check if the chip is on the lowest row
        if space_below[0] == 6:
            return True

        # Case 2: check if chip is supported by a different chip already present
        if self.is_space_available(space_below) == False:
            return True

        return False

    def check_if_won(self, chip):
        """
        Checks if anyone has won
        :param chip: chip :D (🔴 or 🔵)
        :return: true if someone won, false if otherwise
        """
        # Check horizontal
        try:
            for y in range(7):
                for x in range(3):
                    if self.data[x][y] == chip and self.data[x+1][y] == chip and self.data[x+2][y] == chip and self.data[x+3][y] == chip:
                        return True

            # Check vertical
            for y in range(4):
                for x in range(6):
                    if self.data[x][y] == chip and self.data[x][y+1] == chip and self.data[x][y+2] == chip and self.data[x][y+3] == chip:
                        return True

            # Check diagonal (top left -> bottom right)
            for y in range(4):
                for x in range(2, 3):
                    if self.data[x][y] == chip and self.data[x+1][y-1] == chip and self.data[x+2][y-2] == chip and self.data[x+3][y-3] == chip:
                        return True

            # Check diagonal (top right -> bottom left)
            for y in range(4):
                for x in range(5):
                    if self.data[x][y] == chip and self.data[x+1][y+1] == chip and self.data[x+2][y+2] == chip and self.data[x+3][y+3] == chip:
                        return True

            return False
        except IndexError:
            pass

    def check_if_won_2(self, chip):
        """
        Checks if anyone has won
        :param chip: chip :D (🔴 or 🔵)
        :return: true if someone won, false if otherwise
        """
        # Check horizontal
        try:
            for y in range(7):
                for x in range(5):
                    if self.data[x][y] == chip and self.data[x+1][y] == chip and self.data[x+2][y] == chip and self.data[x+3][y] == chip:
                        return True

            # Check vertical
            for y in range(7):
                for x in range(6):
                    if self.data[x][y] == chip and self.data[x][y+1] == chip and self.data[x][y+2] == chip and self.data[x][y+3] == chip:
                        return True

            # Check diagonal (top left -> bottom right)
            for y in range(4):
                for x in range(2, 5):
                    if self.data[x][y] == chip and self.data[x+1][y-1] == chip and self.data[x+2][y-2] == chip and self.data[x+3][y-3] == chip:
                        return True

            # Check diagonal (top right -> bottom left)
            for y in range(4):
                for x in range(5):
                    if self.data[x][y] == chip and self.data[x+1][y+1] == chip and self.data[x+2][y+2] == chip and self.data[x+3][y+3] == chip:
                        return True

            return False
        except IndexError:
            pass

    def check_if_full(self):
        """
        Checks if the board is full
        :return: true if it is, false if it isn't
        """
        for row in self.data:
            if None in row:
                return False
        return True

    def __str__(self):
        t = Texttable()
        t.header(['/', 'A', 'B', 'C', 'D', 'E', 'F', 'G'])
        for row in range(6):
            row_data = [row + 1] + [' '] * 7  # initialize an empty row

            for column in range(7):
                symbol = ' '
                if self.data[row][column] == '🔵':
                    symbol = '🔵'
                elif self.data[row][column] == '🔴':
                    symbol = '🔴'
                row_data[column + 1] = symbol
            t.add_row(row_data)
        return t.draw()

    def return_list(self):
        return self.data
        # board_list = []
        # for data in self.data:
        #     board_list.append(data)
        # return board_list