import random
from enum import unique

from faker import Faker
from src.domain.book import Book
from src.repository.repo_binary import BookBinaryRepo
from src.repository.repo_memory import IDNotFoundError, DuplicateIDError, UnrecognisedCommand, BookMemoryRepo


class BookService:
    def __init__(self, repo):
        self.list_of_books = []
        self.id_not_found = IDNotFoundError
        self.repo = repo

    def add(self, book):
        """
        Adds a valid book to the list of books
        :raises DuplicateIDError: if the inputted id is a duplicate
        :param book: book created using the domain Book
        """
        for entity in self.list_of_books:
            if book.id == entity.id:
                raise DuplicateIDError()

        self.list_of_books.append(book)
        self.repo.add(self.list_of_books)

    def remove(self, id):
        """
        Removes a book from the list based on its id
        :raises IDNotFoundError: if the inputted id is not one of the existing ones
        :param id: id is the unique id of a book
        """
        new_list = []
        for book in self.list_of_books:
            if book.id != id:
                new_list.append(book)
        if new_list == self.list_of_books:
            raise IDNotFoundError(f"ID {id} not found. List not modified.")
        else:
            self.list_of_books = new_list[:]
            self.repo.add(self.list_of_books)

    def update(self, id, command, update):
        """
        Updates an existing book based in its id
        :raises IDNotFoundError: if the inputted id is not one of the existing ones
        :param id: the id of the book the user wishes to update
        :param command: the field the user wishes to update
        :param update: the new value of the updated field
        """
        found = 0
        for book in self.list_of_books:
            if book.id == id:
                found = 1
                if command == '2':
                    book.title = update
                else:
                    book.author = update
        if found == 0:
            raise IDNotFoundError(f"ID {id} not found")
        self.repo.add(self.list_of_books)

    def return_list(self):
        list_of_books = []
        for book in self.list_of_books:
            list_of_books.append([book.id, book.title, book.author])
        return list_of_books

    def search(self, field, search):
        if field == 1:
            try:
                test_search = int(search)
            except ValueError:
                raise ValueError("The inputted id is supposed to be an integer")

        search_list = []
        for book in self.list_of_books:
            if field == 1:
                if search in str(book.id):
                    search_list.append(book)
            elif field == 2:
                if search.lower() in book.title.lower():
                    search_list.append(book)
            elif field == 3:
                if search.lower() in book.author.lower():
                    search_list.append(book)
            else:
                raise UnrecognisedCommand("Field has to be 2 or 3")

        return search_list

    def initialize(self):
        fake = Faker()
        self.list_of_books = self.repo.load_data()  # checks if there is data to load

        if len(self.list_of_books) == 0:
            for id in range(100, 120):
                title = fake.file_name()
                author = fake.name()
                book = Book(id, title, author)
                self.list_of_books.append(book)
            self.repo.add(self.list_of_books)

