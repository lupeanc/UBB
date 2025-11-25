import random
from datetime import date, timedelta
from enum import unique

from src.domain.rental import Rental
from src.repository.repo_binary import RentalBinaryRepo
from src.repository.repo_memory import RentalMemoryRepo, UnrecognisedCommand, IDNotFoundError, AlreadyRented, \
    DuplicateIDError
from src.services.book_services import BookService
from src.services.client_services import ClientService


class RentalService:
    def __init__(self, book_repo, client_repo, rental_repo):
        self.list_of_rentals = []
        self.book_service = BookService(book_repo)
        self.client_service = ClientService(client_repo)
        self.repo = rental_repo

    def rent(self, rental):
        for entity in self.list_of_rentals:
            if rental.id == entity.id:
                raise DuplicateIDError
            if rental.book == entity.book:
                if rental.end < entity.start or rental.start > entity.end:
                    self.list_of_rentals.append(rental)
                else:
                    raise AlreadyRented()
            else:
                self.list_of_rentals.append(rental)
        self.repo.add(self.list_of_rentals)

    def return_rental(self, id):
        new_list = []
        for rental in self.list_of_rentals:
            if rental.book != id:
                new_list.append(rental)
        if new_list == self.list_of_rentals:
            raise IDNotFoundError(f"ID {id} not found. List not modified.")
        else:
            self.list_of_rentals = new_list[:]
            self.repo.add(self.list_of_rentals)

    def initialize(self, list_of_books, list_of_clients):
        list_of_book_ids = [book[0] for book in list_of_books]
        list_of_client_ids = [client[0] for client in list_of_clients]

        if len(self.list_of_rentals) == 0:
            for rental_id in range(300, 305):
                date_start = date(2024, random.randint(1, 12), random.randint(1, 30))
                rental_days = timedelta(days=random.randint(1, 10))
                rental = Rental(rental_id, random.choice(list_of_book_ids), date_start, date_start + rental_days, random.choice(list_of_client_ids))
                self.list_of_rentals.append(rental)
            self.repo.add(self.list_of_rentals)

    def return_list(self):
        list_of_rentals = []
        for rental in self.list_of_rentals:
            list_of_rentals.append([rental.id, rental.book, rental.start, rental.end, rental.client])
        return list_of_rentals
