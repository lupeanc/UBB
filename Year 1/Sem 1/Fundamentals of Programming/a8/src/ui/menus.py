from datetime import date

from src.repository.repo_memory import UnrecognisedCommand, IDNotFoundError
from src.services.book_services import BookService


class Menu:

    def start(self):
        print("1. Manage books and clients")
        print("2. Rent/Return")
        print("3. Search")
        print("4. Display")
        print("0. Exit")

    def manage(self):
        print("1. Add")
        print("2. Remove")
        print("3. Update")

    def rent_return(self):
        print("1. Rent")
        print("2. Return")

        try:
            command = int(input(">>"))
        except ValueError:
            raise ValueError("Command has to be an integer")

        return command


    def book_or_client(self):
        print("1. Book")
        print("2. Client")

#ADD
    def create_book(self):
        try:
            id = input("id: ")
            title = input("title: ")
            author = input("author: ")
            return id, title, author
        except ValueError:
            raise ValueError("id has to be an integers")

    def create_client(self):
        try:
            id = int(input("id: "))
            name = input("name: ")
            return id, name
        except ValueError:
            raise ValueError("id has to be an integers")

#REMOVE BASED ON ID
    def remove(self):
        try:
            id = input("id: ")
            return id
        except ValueError:
            raise ValueError("id has to be an integer")

# UPDATE BASED ON ID
    def update_book(self):
        try:
            id_to_be_updated = int(input("id to be updated: "))

            # print("1. id")
            print("2. Title")
            print("3. Author")
            command = int(input())

            if command == '1':
                update = int(input(">"))
            elif command == '2' or command == '3':
                update = input(">")
            else:
                raise UnrecognisedCommand("Command has to be 1 or 2")

            return id_to_be_updated, command, update

        except ValueError:
            raise ValueError("id/command have to be integers")

    def update_client(self):
        try:
            id_to_be_updated = int(input("id to be updated: "))

            # print("1. id")
            print("2. Name")
            command = int(input())

            return id_to_be_updated, command

        except ValueError:
            raise ValueError("id/command have to be integers")

# RENT/RETURN
    def get_rental(self):
        try:
            rental_id = int(input("Rental ID: "))
        except ValueError:
            raise ValueError("The Rental ID has to be an integer")

        try:
            client_id = int(input("Client ID: "))
        except ValueError:
            raise ValueError("The Client ID has to be an integer")

        try:
            book_id = int(input("Book ID: "))
        except ValueError:
            raise ValueError("The Book ID has to be an integer")

        print("From: ")
        try:
            day_start = int(input("Day: "))
            month_start = int(input("Month: "))
            # year_start = int(input("Year: "))

            if day_start < 0  or day_start > 30:
                raise ValueError("Day value has to be between 1 and 30")
            if month_start < 0 or month_start > 12:
                raise ValueError("Month value has to be between 1 and 12")
        except ValueError:
            raise ValueError("Day/Month have to be integers")

        print("To: ")
        try:
            day_end = int(input("Day: "))
            month_end = int(input("Month: "))

            if day_end < 0 or day_end > 30:
                raise ValueError("Day value has to be between 1 and 30")
            if month_end < 0 or month_end > 12:
                raise ValueError("Month value has to be between 1 and 12")
        except ValueError:
            raise ValueError("Day/Month have to be integers")

        return rental_id, book_id, date(2024, month_start, day_start), date(2024, month_end, day_end), client_id

    def get_return(self):
        try:
            book_id = int(input("Book ID: "))
            return book_id
        except ValueError:
            raise ValueError("The Book ID has to be an integer")


# SEARCH BASED ON <field>
    def search_book_field(self):
        print("Search by:")
        print("1. id")
        print("2. Title")
        print("3. Author")

        try:
            field = int(input(">>"))
        except ValueError:
            raise ValueError("Field has to be an integer")

        search = input("Search: ")
        return field, search

    def search_client_field(self):
        print("Search by:")
        print("1. id")
        print("2. Name")

        try:
            field = int(input(">>>"))
        except ValueError:
            raise ValueError("Field has to be an integer")

        search = input("Search: ")
        return field, search

