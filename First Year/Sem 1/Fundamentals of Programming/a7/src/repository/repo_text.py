import json

from src.domain.complex import ComplexNumber
from src.repository.repo_memory import ComplexNumberMemoryRepo


class ComplexNumberTextRepo(ComplexNumberMemoryRepo):

    def __init__(self, file_name: str = 'F:\\UBB\\Seminars\\a7-lupeanraisa\\src\\repository\\numbers.txt'):
        super().__init__()
        self.__file_name = file_name
        self.__load()

    def __load(self):
        try:
            fin = open(self.__file_name, "r")
            # data = json.load(fin)
            # self._data = [ComplexNumber.from_dict(d) for d in data]
            self._data = json.load(fin)

            fin.close()
        except Exception:
            pass

    def __save(self):
        fout = open(self.__file_name, "w")
        json.dump([cn.to_dict() for cn in self._data], fout)
        fout.close()

    def add(self, list_of_numbers):

        super().add(list_of_numbers)

        self.__save()