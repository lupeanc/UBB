class ComplexNumberMemoryRepo:

    def __init__(self):
        self._data = []

    def add(self, list_of_numbers):
        self._data = list_of_numbers

    def load_data(self):
        return self._data
