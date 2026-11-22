import datetime
import random
from datetime import date, timedelta
from enum import unique
from types import NoneType

from src.domain.rental import Rental
from src.repository.repo_binary import RentalBinaryRepo
from src.repository.repo_memory import RentalMemoryRepo, UnrecognisedCommand, IDNotFoundError, AlreadyRented, \
    DuplicateIDError
from src.services.book_services import BookService
from src.services.client_services import ClientService

class BookPopularityDTO:  # DTO - data transfer object
    def __init__(self, book, client_count: int):
        self.__book = book
        self.__client_count = client_count

    @property
    def book(self):
        return self.__book

    @property
    def clients(self):
        return self.__client_count

    def __lt__(self, other):
        return self.__client_count > other.__client_count

class RentalService:
    def __init__(self, book_repo, client_repo, rental_repo):
        self.list_of_rentals = rental_repo.load_data()
        self.book_service = BookService(book_repo)
        self.client_service = ClientService(client_repo)
        self.book_repo = book_repo
        self.repo = rental_repo

    def rent(self, rental):
        if len(self.list_of_rentals) == 0:
            self.list_of_rentals.append(rental)
        else:
            for entity in self.list_of_rentals:
                if rental.id == entity.id:
                    raise DuplicateIDError("Duplicate rental ID")
                else:
                    self.list_of_rentals.append(rental)
                    break

        self.repo.add(self.list_of_rentals)

    def return_rental(self, book_id, rental_id):
        new_list = []
        for rental in self.list_of_rentals:
            if rental.id != rental_id:
                new_list.append(rental)
        if new_list == self.list_of_rentals:
            pass
            # raise IDNotFoundError(f"ID {id} not found. List not modified.")
        else:
            self.list_of_rentals = new_list[:]
            self.repo.add(self.list_of_rentals)

    def return_list(self):
        list_of_rentals = []
        for rental in self.list_of_rentals:
            list_of_rentals.append([rental.id, rental.book, rental.start, rental.end, rental.client])
        return list_of_rentals

    def initialize(self):
        list_of_clients = self.client_service.return_list()
        list_of_books = self.book_service.return_list()

        book_ids = []
        client_ids = []
        for book in list_of_books:
            book_ids.append(book[0])

        for client in list_of_clients:
            client_ids.append(client[0])

        if len(self.list_of_rentals) == 0:
            for id in range(300, 320):
                book_id = random.randint(100, 115)
                client_id = random.randint(200, 215)
                start = date(2024, random.randint(1, 12), random.randint(1, 20))
                end = date(2024, start.month, start.day+random.randint(1, 8))

                rental = Rental(id, book_id, start, end, client_id)
                self.list_of_rentals.append(rental)
            self.repo.add(self.list_of_rentals)

    def most_active_clients(self):
        client_rental_number = []

        for rental in self.list_of_rentals:
            if len(client_rental_number) == 0:
                time_delta = rental.end - rental.start
                client_rental_number.append([rental.client, time_delta])
            else:
                for client in client_rental_number:
                    if rental.client == client[0]:
                        time_delta = rental.end - rental.start
                        client[1] += time_delta
                        break
                    else:
                        time_delta = rental.end - rental.start
                        client_rental_number.append([rental.client, time_delta])
        result_not_desc = []
        result = []
        for client in client_rental_number:
            client_id = client[0]
            result_not_desc.append([client_id, client[1]])
        result_not_desc = sorted(result_not_desc, key=lambda x: x[1], reverse=True)

        for i in range(5):
            client_id = result_not_desc[i][0]
            result.append([client_id, result_not_desc[i][1]])

        return result

    def most_popular_books(self):
        book_rental_number = []

        for rental in self.list_of_rentals:
            if len(book_rental_number) == 0:
                book_rental_number.append([rental.book, 1])
            else:
                found = 0
                for book in book_rental_number:
                    if rental.book == book[0]:
                        book[1] += 1
                        found = 1
                if found == 0:
                    book_rental_number.append([rental.book, 1])
        result_not_desc= []
        result = []
        for book in book_rental_number:
            book_id = book[0]
            result_not_desc.append([book_id, book[1]])
        result_not_desc = sorted(result_not_desc, key=lambda x: x[1], reverse=True)

        for i in range(5):
            book_id = result_not_desc[i][0]
            result.append([book_id, result_not_desc[i][1]])

        return result

