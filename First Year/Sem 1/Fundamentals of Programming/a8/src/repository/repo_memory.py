from datetime import date

from pyexpat.errors import messages

from src.domain.book import Book
from src.domain.client import Client
from src.domain.rental import Rental


class RepositoryError(Exception):
    def __init__(self, message: str = ""):
        self.__message = message

    @property
    def message(self):
        return self.__message

class DuplicateIDError(RepositoryError):
    def __init__(self, message = 'Duplicate ID'):
        self.__message = message

    @property
    def message(self):
        return self.__message

class IDNotFoundError(RepositoryError):
    def __init__(self, message):
        self.__message = message

    @property
    def message(self):
        return self.__message

class UnrecognisedCommand(RepositoryError):
    def __init__(self, message):
        self.__message = message

    @property
    def message(self):
        return self.__message

class ImproperProperty(RepositoryError):
    def __init__(self, message = "Improper property file"):
        self.__message = message

    @property
    def message(self):
        return self.__message

class AlreadyRented(RepositoryError):
    def __init__(self, message = 'You cannot rent this book during the specified time period'):
        self.__message = message

    @property
    def message(self):
        return self.__message

class BookMemoryRepo:

    def __init__(self):
        self._data = []

    def add(self, list_of_books):
        self._data = list_of_books

    def load_data(self):
        return self._data

    def __len__(self):
        return len(self._data)

    def find(self, elem_id):
        if elem_id not in self._data:  # is the elem_id already a key in the dict?
            return None
        return self._data[elem_id]

class ClientMemoryRepo:

    def __init__(self):
        self._data = []

    def add(self, list_of_clients):
        self._data = list_of_clients

    def load_data(self):
        return self._data

    def __len__(self):
        return len(self._data)

    def find(self, elem_id):
        if elem_id not in self._data:  # is the elem_id already a key in the dict?
            return None
        return self._data[elem_id]

class RentalMemoryRepo:

    def __init__(self):
        self._data = []

    def add(self, list_of_rentals):
        self._data = list_of_rentals

    def load_data(self):
        return self._data

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
    repo_book = BookMemoryRepo()
    list_of_books = [Book(100, 'title', 'author')]

    repo_book.add(list_of_books)
    assert repo_book.__len__() == 1

    list_of_books.append(Book(101, 'title2', 'author2'))
    repo_book.add(list_of_books)
    assert repo_book.__len__() == 2

    # CLIENT ADD
    repo_client = ClientMemoryRepo()
    list_of_clients = [Client(100, 'name')]

    repo_client.add(list_of_clients)
    assert repo_client.__len__() == 1

    list_of_clients.append(Client(101, 'name'))
    repo_client.add(list_of_clients)
    assert repo_client.__len__() == 2

    # RENTALS ADD
    repo_rental = RentalMemoryRepo()
    list_of_rentals = [Rental(100, 'book name', date(2024, 11, 30), date(2024, 12, 4), 101)]

    repo_rental.add(list_of_rentals)
    assert repo_rental.__len__() == 1

    list_of_rentals.append(Rental(101, 'book name', date(2024, 10, 30), date(2024, 12, 4), 102))
    repo_client.add(list_of_rentals)
    assert repo_rental.__len__() == 2
# test_add()