import json
from datetime import date

from src.domain.book import Book
from src.domain.client import Client
from src.domain.rental import Rental
from src.repository.repo_memory import BookMemoryRepo, ClientMemoryRepo, RentalMemoryRepo


class BookTextRepo(BookMemoryRepo):

    def __init__(self, file_name: str ):
        super().__init__()
        self.__file_name = file_name
        self.__load()

    def __load(self):
        try:
            fin = open(self.__file_name, "r")
            self._data = json.load(fin)

            fin.close()
        except FileNotFoundError:
            pass

    def __save(self):
        fout = open(self.__file_name, "w")
        json.dump([b.to_dict() for b in self._data], fout)
        fout.close()

    def add(self, list_of_books):

        super().add(list_of_books)

        self.__save()

    def __len__(self):
        return len(self._data)

    def find(self, elem_id):
        if elem_id not in self._data:  # is the elem_id already a key in the dict?
            return None
        return self._data[elem_id]

class ClientTextRepo(ClientMemoryRepo):

    def __init__(self, file_name: str ):
        super().__init__()
        self.__file_name = file_name
        self.__load()

    def __load(self):
        try:
            fin = open(self.__file_name, "r")
            self._data = json.load(fin)

            fin.close()
        except FileNotFoundError:
            pass

    def __save(self):
        fout = open(self.__file_name, "w")
        json.dump([c.to_dict() for c in self._data], fout)
        fout.close()

    def add(self, list_of_clients):

        super().add(list_of_clients)

        self.__save()

    def __len__(self):
        return len(self._data)

    def find(self, elem_id):
        if elem_id not in self._data:  # is the elem_id already a key in the dict?
            return None
        return self._data[elem_id]

class RentalTextRepo(RentalMemoryRepo):

    def __init__(self, file_name: str):
        super().__init__()
        self.__file_name = file_name
        self.__load()

    def __load(self):
        try:
            fin = open(self.__file_name, "r")
            self._data = json.load(fin)

            fin.close()
        except FileNotFoundError:
            pass

    def __save(self):
        fout = open(self.__file_name, "w")
        json.dump([r.to_dict() for r in self._data], fout)
        fout.close()

    def add(self, list_of_rentals):

        super().add(list_of_rentals)

        self.__save()

    def __len__(self):
        return len(self._data)

    def find(self, elem_id):
        if elem_id not in self._data:  # is the elem_id already a key in the dict?
            return None
        return self._data[elem_id]

# NON UNIT
def test_add():
    # NOTE: Errors are checked in the Services class
    # BOOK ADD
    repo_book = BookTextRepo('books.t')
    list_of_books = [Book(100, 'title', 'author')]

    repo_book.add(list_of_books)
    assert repo_book.__len__() == 1

    list_of_books.append(Book(101, 'title2', 'author2'))
    repo_book.add(list_of_books)
    assert repo_book.__len__() == 2

    # CLIENT ADD
    repo_client = ClientTextRepo('clients.t')
    list_of_clients = [Client(100, 'name')]

    repo_client.add(list_of_clients)
    assert repo_client.__len__() == 1

    list_of_clients.append(Client(101, 'name'))
    repo_client.add(list_of_clients)
    assert repo_client.__len__() == 2

    # RENTALS ADD
    repo_rental = RentalTextRepo('rentals.t')
    list_of_rentals = [Rental(100, 'book name', date(2024, 11, 30), date(2024, 12, 4), 101)]

    repo_rental.add(list_of_rentals)
    assert repo_rental.__len__() == 1

    list_of_rentals.append(Rental(101, 'book name', date(2024, 10, 30), date(2024, 12, 4), 102))
    repo_rental.add(list_of_rentals)
    assert repo_rental.__len__() == 2
# test_add()