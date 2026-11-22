class FunctionCall:
    def __init__(self, function, *params):
        self.__function = function
        self.__params = params

    def call(self):
        # () - call operator in Python
        self.__function(*self.__params)

    def __call__(self, *args, **kwargs):
        self.call()


class Operation:
    def __init__(self, function_undo: FunctionCall, function_redo: FunctionCall):
        self.function_undo = function_undo
        self.function_redo = function_redo

    def undo(self):
        self.function_undo.call()

    def redo(self):
        self.function_redo.call()

class UndoServices:
    def __init__(self):
        self.__history = []
        self.__index = 0

    def record(self, operation):
        if self.__index > -1:
            while self.__index < len(self.__history):
                self.__history.pop()
        self.__history.append(operation)
        self.__index = len(self.__history)

    def undo(self) -> None:
        """
        Undo the last operations carried out
        :return: None
        """
        if self.__index == 0:
            print("There are no more actions to be undone!")
            return
            # raise UndoException("There are no more actions to be undone!")

        self.__index -= 1
        try:
            self.__history[self.__index].undo()
        except IndexError:
            print("There are no more actions to be undone!")
        self.__history[self.__index].undo()

    def redo(self) -> None:
        """
        Redoes the last undone operation
        :return: None
        """
        if self.__index == len(self.__history):
            print("There are no more actions to be redone!")
            return
            # raise UndoException("There are no more actions to be redone!")

        try:
            self.__history[self.__index].redo()
        except IndexError:
            print("There are no more actions to be redone!")
        self.__history[self.__index].redo()
        self.__index += 1