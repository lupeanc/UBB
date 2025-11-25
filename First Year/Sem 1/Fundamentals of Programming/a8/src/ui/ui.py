import random
from src.domain.book import Book
from src.domain.client import Client
from src.domain.rental import Rental
from src.repository.repo_binary import BookBinaryRepo, ClientBinaryRepo, RentalBinaryRepo
from src.repository.repo_memory import UnrecognisedCommand, RepositoryError, IDNotFoundError, BookMemoryRepo, \
    ClientMemoryRepo, RentalMemoryRepo
from src.repository.repo_text import BookTextRepo, ClientTextRepo, RentalTextRepo
from src.services.book_services import BookService
from src.services.client_services import ClientService
from src.services.rental_services import RentalService
from src.ui.menus import Menu

class UI:
    def __init__(self):
        self.menu = Menu()

        properties_file = open("settings.properties", "r")
        repo = str(properties_file.readline().strip("\n").split("=")[1])
        if repo == 'inmemory':
            self.book_service = BookService(BookMemoryRepo())
            self.client_service = ClientService(ClientMemoryRepo())
            self.rental_service = RentalService(BookMemoryRepo(), ClientMemoryRepo(), RentalMemoryRepo())
        elif repo == 'binaryfiles':
            book_file = str(properties_file.readline().strip("\n").split("=")[1])
            self.book_service = BookService(BookBinaryRepo(book_file))

            client_file = str(properties_file.readline().strip("\n").split("=")[1])
            self.client_service = ClientService(ClientBinaryRepo(client_file))

            rental_file = str(properties_file.readline().strip("\n").split("=")[1])
            self.rental_service = RentalService(BookBinaryRepo(book_file),ClientBinaryRepo(client_file), RentalBinaryRepo(rental_file))
        elif repo == 'text':
            book_file = str(properties_file.readline().strip("\n").split("=")[1])
            self.book_service = BookService(BookTextRepo(book_file))

            client_file = str(properties_file.readline().strip("\n").split("=")[1])
            self.client_service = ClientService(ClientTextRepo(client_file))

            rental_file = str(properties_file.readline().strip("\n").split("=")[1])
            self.rental_service = RentalService(BookTextRepo(book_file), ClientTextRepo(client_file), RentalTextRepo(rental_file))
        else:
            raise UnrecognisedCommand("Improper Settings")

    def start(self):
        self.book_service.initialize()
        self.client_service.initialize()
        self.rental_service.initialize(self.book_service.return_list(), self.client_service.return_list())
        while True:
            try:
                self.menu.start()
                command = input(">")

                # MANAGE
                if command == '1':
                    self.menu.manage()
                    manage = input(">")
                    self.menu.book_or_client()
                    entity_nb = input(">")

                    # MANAGE BOOK
                    if entity_nb == '1':
                        id, title, author = self.menu.create_book()
                        book = Book(id, title, author)

                        # ADD
                        if manage == '1':
                            self.book_service.add(book)

                        # REMOVE
                        elif manage == '2':
                            id = self.menu.remove()
                            self.book_service.remove(id)
                            # re-initializes list so we dont have removed books in the rentals list
                            # self.rental_service.initialize(self.book_service.return_list(), self.client_service.return_list())
                            list_of_book_ids = [rental[1] for rental in self.rental_service.return_list()]
                            if id in list_of_book_ids:
                                self.rental_service.return_rental(id)

                        #UPDATE
                        elif manage == '3':
                            id, command, update = self.menu.update_book()
                            self.book_service.update(id, command, update)
                        else:
                            raise UnrecognisedCommand("Command has to be 1, 2 or 3")

                    # MANAGE CLIENT
                    elif entity_nb == '2':
                        id, name = self.menu.create_client()
                        client = Client(int(id), name)

                        # ADD
                        if manage == '1':
                            pass
                            self.client_service.add(client)

                        # REMOVE
                        elif manage == '2':
                            id = self.menu.remove()
                            self.client_service.remove(id)
                            list_of_client_ids = [[rental[4], rental[1]] for rental in self.rental_service.return_list()]
                            for entity in list_of_client_ids:
                                if id == entity[0]:
                                    self.rental_service.return_rental(entity[1])

                        # UPDATE
                        elif manage == '3':
                            id, command, update = self.menu.update_client()
                            self.client_service.update(id, command, update)
                        else:
                            raise UnrecognisedCommand("Command has to be 1, 2 or 3")

                    else:
                        raise UnrecognisedCommand("Command has to be 1 or 2")

                elif command == '2':
                    cmd = self.menu.rent_return()

                    if cmd == 1:
                        rental_id, book_id, start_date, end_date, client_id = self.menu.get_rental()
                        rental = Rental(rental_id, book_id, start_date, end_date, client_id)
                        self.rental_service.rent(rental)

                    elif cmd == 2:
                        book_id = self.menu.get_return()
                        self.rental_service.return_rental(book_id)

                    else:
                        raise UnrecognisedCommand("Command has to be 1 or 2")

                # SEARCH
                elif command == '3':
                    self.menu.book_or_client()
                    search_for = input(">")

                    #SEARCH FOR BOOK
                    if search_for == '1':
                        field, search = self.menu.search_book_field()
                        search_list = self.book_service.search(field, search)

                        if len(search_list) != 0:
                            for book in search_list:
                                print(book)
                        else:
                            print("No results")

                    #SEARCH FOR CLIENT
                    elif search_for == '2':
                        field, search = self.menu.search_client_field()
                        search_list = self.client_service.search(field, search)
                        if len(search_list) != 0:
                            for client in search_list:
                                print(client)
                        else:
                            print("No results")

                    else:
                        raise UnrecognisedCommand("Command has to be 1 or 2")

                elif command == '4':
                    print("1.Books")
                    print("2. Clients")
                    print("3. Rentals")
                    display_cmd = input(">")
                    if display_cmd == '1':
                        for book in self.book_service.return_list():
                            print(f"{book[0]}: {book[1]} by {book[2]}")
                    elif display_cmd == '2':
                        for client in self.client_service.return_list():
                            print(f"{client[0]}: {client[1]}")
                    elif display_cmd == '3':
                        for rental in self.rental_service.return_list():
                            print(f"{rental[0]}: {rental[1]} - {rental[2]} to {rental[3]} by {rental[4]}")
                # EXIT
                elif command == '0':
                    break
                else:
                    raise UnrecognisedCommand("Unrecognised command")
            except ValueError as ve:
                print(ve)
            except RepositoryError as re:
                print(re)


if __name__ == "__main__":
    ui = UI()
    ui.start()