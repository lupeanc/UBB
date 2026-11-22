
class RepositoryError(Exception):
    def __init__(self, message: str = ""):
        self.__message = message

    @property
    def message(self):
        return self.__message

class GameOver(RepositoryError):
    def __init__(self, message = 'GAME OVER'):
        self.__message = message

    @property
    def message(self):
        return self.__message


class BoardMemoryRepo:
    def __init__(self):
        self._data = []
        for i in range(6):
            self._data.append([None] * 7)

    def add(self, board_list):
        self._data = board_list

    def load_data(self):
        return self._data