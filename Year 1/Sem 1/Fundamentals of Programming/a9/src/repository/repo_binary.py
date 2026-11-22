import pickle
from datetime import date

from src.domain.book import Book
from src.domain.client import Client
from src.domain.rental import Rental
from src.repository.repo_memory import BookMemoryRepo, ClientMemoryRepo, RentalMemoryRepo


class BookBinaryRepo(BookMemoryRepo):

    def __init__(self, file_name: str ):
        super().__init__()
        self.__file_name = file_name
        self.__load()

    def __load(self):
        try:
            fin = open(self.__file_name, "rb")
            self._data = pickle.load(fin)
            fin.close()
        except FileNotFoundError:
            pass

    def __save(self):
        fout = open(self.__file_name, "wb")  # w - write, b - binary
        pickle.dump(self._data, fout)
        fout.close()

    def add(self, list_of_books):

        super().add(list_of_books)
        self.__save()

    def __len__(self):
        return len(self._data)

class ClientBinaryRepo(ClientMemoryRepo):

    def __init__(self, file_name: str ):
        super().__init__()
        self.__file_name = file_name
        self.__load()

    def __load(self):
        try:
            fin = open(self.__file_name, "rb")
            self._data = pickle.load(fin)
            fin.close()
        except FileNotFoundError:
            pass

    def __save(self):
        fout = open(self.__file_name, "wb")  # w - write, b - binary
        pickle.dump(self._data, fout)
        fout.close()

    def add(self, list_of_clients):

        super().add(list_of_clients)

        self.__save()

    def __len__(self):
        return len(self._data)

class RentalBinaryRepo(RentalMemoryRepo):

    def __init__(self, file_name: str):
        super().__init__()
        self.__file_name = file_name
        self.__load()

    def __load(self):
        try:
            fin = open(self.__file_name, "rb")
            self._data = pickle.load(fin)
            fin.close()
        except FileNotFoundError:
            pass

    def __save(self):
        fout = open(self.__file_name, "wb")  # w - write, b - binary
        pickle.dump(self._data, fout)
        fout.close()

    def add(self, list_of_rentals):

        super().add(list_of_rentals)

        self.__save()

    def __len__(self):
        return len(self._data)

# NON UNIT
def test_add():
    # NOTE: Errors are checked in the Services class
    # BOOK ADD
    repo_book = BookBinaryRepo("books.bin")
    list_of_books = [Book(100, 'title', 'author')]

    repo_book.add(list_of_books)
    assert repo_book.__len__() == 1

    list_of_books.append(Book(101, 'title2', 'author2'))
    repo_book.add(list_of_books)
    assert repo_book.__len__() == 2

    # CLIENT ADD
    repo_client = ClientBinaryRepo("clients.bin")
    list_of_clients = [Client(100, 'name')]

    repo_client.add(list_of_clients)
    assert repo_client.__len__() == 1

    list_of_clients.append(Client(101, 'name'))
    repo_client.add(list_of_clients)
    assert repo_client.__len__() == 2

    # RENTALS ADD
    repo_rental = RentalBinaryRepo("rentals.bin")
    list_of_rentals = [Rental(100, 'book name', date(2024, 11, 30), date(2024, 12, 4), 101)]

    repo_rental.add(list_of_rentals)
    assert repo_rental.__len__() == 1

    list_of_rentals.append(Rental(101, 'book name', date(2024, 10, 30), date(2024, 12, 4), 102))
    repo_client.add(list_of_rentals)
    assert repo_rental.__len__() == 2
# test_add()
