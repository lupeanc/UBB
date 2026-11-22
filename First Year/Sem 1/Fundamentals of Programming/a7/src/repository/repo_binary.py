import pickle

from src.domain.complex import ComplexNumber
from src.repository.repo_memory import ComplexNumberMemoryRepo


class ComplexNumberBinaryRepo(ComplexNumberMemoryRepo):

    def __init__(self, file_name: str = 'F:\\UBB\\Seminars\\a7-lupeanraisa\\src\\repository\\numbers.bin'):
        super().__init__()
        self.__file_name = file_name
        self.__load()

    def __load(self):
        try:
            fin = open(self.__file_name, "rb")
            self._data = pickle.load(fin)
            fin.close()
        except Exception:
            pass

    def __save(self):
        fout = open(self.__file_name, "wb")  # w - write, b - binary
        pickle.dump(self._data, fout)
        fout.close()

    def add(self, list_of_numbers):

        super().add(list_of_numbers)

        self.__save()

    # def load_data(self):
    #     return super().load_data()
