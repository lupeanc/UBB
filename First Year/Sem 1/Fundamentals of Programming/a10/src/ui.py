from src.board import ConnectFourBoard
from src.game import ConnectFour
from src.repo_memory import GameOver


class UI:
    def __init__(self):
        self.__game = ConnectFour()
        self.c4_checks = ConnectFourBoard()
        self.__turn = 1

    def place_chip_player(self):
        input_coords = input("Player move: ")
        input_coords = input_coords.upper().strip()
        tokens = input_coords.split()

        if len(tokens) == 2:
            tokens[1] = int(tokens[1])-1

            self.__game.place_chip_player(tokens, self.__turn)
            self.__turn += 1
        else:
            raise ValueError("Invalid input")

    def start(self):
        print(ConnectFourBoard())
        try:
            self.place_chip_player()
        except ValueError:
            print("Invalid input")

        while True:
            try:
                if self.__turn % 2 == 1:
                    print(self.__game.c4_board)
                    self.place_chip_player()

                else:
                    self.__game.place_chip_computer()
                    self.__turn += 1

            except ValueError:
                print("Invalid input")
            except GameOver as go:
                print(self.__game.c4_board)
                print(go)
                break


if __name__ == "__main__":
    ui = UI()
    ui.start()

