from src.domain.book import Book
from src.domain.client import Client
from src.repository.repo_binary import BookBinaryRepo, ClientBinaryRepo
from src.repository.repo_memory import DuplicateIDError, IDNotFoundError, BookMemoryRepo, ClientMemoryRepo
from src.repository.repo_text import BookTextRepo, ClientTextRepo
from src.services.book_services import BookService
from src.services.client_services import ClientService

import unittest

class TestBookServiceM(unittest.TestCase):
    def setUp(self):
        # Set up a fresh BookService instance before each test
        self.service = BookService(BookMemoryRepo())

    def test_add(self):
        # Test adding valid books
        book1 = Book(100, 'title1', 'author1')
        self.service.add(book1)
        self.assertEqual(self.service.return_list(), [[100, 'title1', 'author1']])

        book2 = Book(101, 'Modern Warfare 2: Ghost', 'Lapham/West')
        book3 = Book(102, 'title3', 'author3')
        self.service.add(book2)
        self.service.add(book3)

        # Test adding a book with invalid ID
        with self.assertRaises(ValueError):
            invalid_book = Book('dcf', 'title', 'author')
            self.service.add(invalid_book)

        # Test adding a book with duplicate ID
        with self.assertRaises(DuplicateIDError):
            duplicate_book = Book(100, 'title', 'author')
            self.service.add(duplicate_book)

    def test_remove(self):
        # Add some books first to ensure remove works
        self.service.add(Book(100, 'title1', 'author1'))
        self.service.add(Book(101, 'Modern Warfare 2: Ghost', 'Lapham/West'))
        self.service.add(Book(102, 'title3', 'author3'))

        # Remove a valid book by ID
        self.service.remove(101)
        self.assertEqual(
            self.service.return_list(), [[100, 'title1', 'author1'], [102, 'title3', 'author3']]
        )

        # Try to remove a non-existent book
        with self.assertRaises(IDNotFoundError):
            self.service.remove(200)

    def test_update(self):
        # Add some books first to ensure update works
        self.service.add(Book(100, 'title1', 'author1'))
        self.service.add(Book(104, 'title3', 'author3'))


        # Update book title
        self.service.update(104, '2', 'title5')
        self.assertEqual(
            self.service.return_list(), [[100, 'title1', 'author1'], [104, 'title5', 'author3']]
        )

        # Update book author
        self.service.update(104, '3', 'author6')
        self.assertEqual(
            self.service.return_list(), [[100, 'title1', 'author1'], [104, 'title5', 'author6']]
        )

        # Try to update a non-existent book
        with self.assertRaises(IDNotFoundError):
            self.service.update(200, '3', 'author')

class TestBookServiceB(unittest.TestCase):
    def setUp(self):
        # Set up a fresh BookService instance before each test
        self.service = BookService(BookBinaryRepo('books.b'))

    def test_add(self):
        # Test adding valid books
        book1 = Book(100, 'title1', 'author1')
        self.service.add(book1)
        self.assertEqual(self.service.return_list(), [[100, 'title1', 'author1']])

        book2 = Book(101, 'Modern Warfare 2: Ghost', 'Lapham/West')
        book3 = Book(102, 'title3', 'author3')
        self.service.add(book2)
        self.service.add(book3)

        # Test adding a book with invalid ID
        with self.assertRaises(ValueError):
            invalid_book = Book('dcf', 'title', 'author')
            self.service.add(invalid_book)

        # Test adding a book with duplicate ID
        with self.assertRaises(DuplicateIDError):
            duplicate_book = Book(100, 'title', 'author')
            self.service.add(duplicate_book)

    def test_remove(self):
        # Add some books first to ensure remove works
        self.service.add(Book(100, 'title1', 'author1'))
        self.service.add(Book(101, 'Modern Warfare 2: Ghost', 'Lapham/West'))
        self.service.add(Book(102, 'title3', 'author3'))

        # Remove a valid book by ID
        self.service.remove(101)
        self.assertEqual(
            self.service.return_list(), [[100, 'title1', 'author1'], [102, 'title3', 'author3']]
        )

        # Try to remove a non-existent book
        with self.assertRaises(IDNotFoundError):
            self.service.remove(200)

    def test_update(self):
        # Add some books first to ensure update works
        self.service.add(Book(100, 'title1', 'author1'))
        self.service.add(Book(104, 'title3', 'author3'))


        # Update book title
        self.service.update(104, '2', 'title5')
        self.assertEqual(
            self.service.return_list(), [[100, 'title1', 'author1'], [104, 'title5', 'author3']]
        )

        # Update book author
        self.service.update(104, '3', 'author6')
        self.assertEqual(
            self.service.return_list(), [[100, 'title1', 'author1'], [104, 'title5', 'author6']]
        )

        # Try to update a non-existent book
        with self.assertRaises(IDNotFoundError):
            self.service.update(200, '3', 'author')

class TestBookServiceT(unittest.TestCase):
    def setUp(self):
        # Set up a fresh BookService instance before each test
        self.service = BookService(BookTextRepo('books.t'))

    def test_add(self):
        # Test adding valid books
        book1 = Book(100, 'title1', 'author1')
        self.service.add(book1)
        self.assertEqual(self.service.return_list(), [[100, 'title1', 'author1']])

        book2 = Book(101, 'Modern Warfare 2: Ghost', 'Lapham/West')
        book3 = Book(102, 'title3', 'author3')
        self.service.add(book2)
        self.service.add(book3)

        # Test adding a book with invalid ID
        with self.assertRaises(ValueError):
            invalid_book = Book('dcf', 'title', 'author')
            self.service.add(invalid_book)

        # Test adding a book with duplicate ID
        with self.assertRaises(DuplicateIDError):
            duplicate_book = Book(100, 'title', 'author')
            self.service.add(duplicate_book)

    def test_remove(self):
        # Add some books first to ensure remove works
        self.service.add(Book(100, 'title1', 'author1'))
        self.service.add(Book(101, 'Modern Warfare 2: Ghost', 'Lapham/West'))
        self.service.add(Book(102, 'title3', 'author3'))

        # Remove a valid book by ID
        self.service.remove(101)
        self.assertEqual(
            self.service.return_list(), [[100, 'title1', 'author1'], [102, 'title3', 'author3']]
        )

        # Try to remove a non-existent book
        with self.assertRaises(IDNotFoundError):
            self.service.remove(200)

    def test_update(self):
        # Add some books first to ensure update works
        self.service.add(Book(100, 'title1', 'author1'))
        self.service.add(Book(104, 'title3', 'author3'))

        # Update book title
        self.service.update(104, '2', 'title5')
        self.assertEqual(
            self.service.return_list(), [[100, 'title1', 'author1'], [104, 'title5', 'author3']]
        )

        # Update book author
        self.service.update(104, '3', 'author6')
        self.assertEqual(
            self.service.return_list(), [[100, 'title1', 'author1'], [104, 'title5', 'author6']]
        )

        # Try to update a non-existent book
        with self.assertRaises(IDNotFoundError):
            self.service.update(200, '3', 'author')

class TestClientServiceM(unittest.TestCase):
    def setUp(self):
        # Set up a fresh ClientService instance before each test
        self.service = ClientService(ClientMemoryRepo())

    def test_add(self):
        # Test adding a valid client
        client1 = Client(100, 'Simon Riley')
        self.service.add(client1)
        self.assertEqual(self.service.return_list(), [[100, 'Simon Riley']])

        # Test adding a client with invalid ID
        with self.assertRaises(ValueError):
            invalid_client = Client('dcf', 'name')
            self.service.add(invalid_client)

        # Test adding a client with duplicate ID
        with self.assertRaises(DuplicateIDError):
            duplicate_client = Client(100, 'name')
            self.service.add(duplicate_client)

        # Test adding more clients
        self.service.add(Client(101, 'John MacTavish'))
        self.service.add(Client(102, 'John Price'))
        self.service.add(Client(103, 'Kyle Garrick'))

    def test_remove(self):
        # Add clients first to ensure remove works
        self.service.add(Client(100, 'Simon Riley'))
        self.service.add(Client(101, 'John MacTavish'))
        self.service.add(Client(102, 'John Price'))
        self.service.add(Client(103, 'Kyle Garrick'))

        # Remove a valid client by ID
        self.service.remove(101)
        self.assertEqual(
            self.service.return_list(), [[100, 'Simon Riley'], [102, 'John Price'], [103, 'Kyle Garrick']]
        )

        # Try to remove a non-existent client
        with self.assertRaises(IDNotFoundError):
            self.service.remove(200)

    def test_update(self):
        # Add clients first to ensure update works
        self.service.add(Client(100, 'Simon Riley'))
        self.service.add(Client(102, 'John Price'))
        self.service.add(Client(103, 'Kyle Garrick'))

        # Update client name
        self.service.update(100, '2', 'Simon "Ghost" Riley')
        self.assertEqual(
            self.service.return_list(), [[100, 'Simon "Ghost" Riley'], [102, 'John Price'], [103, 'Kyle Garrick']]
        )

        # Try to update a non-existent client
        with self.assertRaises(IDNotFoundError):
            self.service.update(200, '2', 'tgegf')

class TestClientServiceB(unittest.TestCase):
    def setUp(self):
        # Set up a fresh ClientService instance before each test
        self.service = ClientService(ClientBinaryRepo('clients.b'))

    def test_add(self):
        # Test adding a valid client
        client1 = Client(100, 'Simon Riley')
        self.service.add(client1)
        self.assertEqual(self.service.return_list(), [[100, 'Simon Riley']])

        # Test adding a client with invalid ID
        with self.assertRaises(ValueError):
            invalid_client = Client('dcf', 'name')
            self.service.add(invalid_client)

        # Test adding a client with duplicate ID
        with self.assertRaises(DuplicateIDError):
            duplicate_client = Client(100, 'name')
            self.service.add(duplicate_client)

        # Test adding more clients
        self.service.add(Client(101, 'John MacTavish'))
        self.service.add(Client(102, 'John Price'))
        self.service.add(Client(103, 'Kyle Garrick'))

    def test_remove(self):
        # Add clients first to ensure remove works
        self.service.add(Client(100, 'Simon Riley'))
        self.service.add(Client(101, 'John MacTavish'))
        self.service.add(Client(102, 'John Price'))
        self.service.add(Client(103, 'Kyle Garrick'))

        # Remove a valid client by ID
        self.service.remove(101)
        self.assertEqual(
            self.service.return_list(), [[100, 'Simon Riley'], [102, 'John Price'], [103, 'Kyle Garrick']]
        )

        # Try to remove a non-existent client
        with self.assertRaises(IDNotFoundError):
            self.service.remove(200)

    def test_update(self):
        # Add clients first to ensure update works
        self.service.add(Client(100, 'Simon Riley'))
        self.service.add(Client(102, 'John Price'))
        self.service.add(Client(103, 'Kyle Garrick'))

        # Update client name
        self.service.update(100, '2', 'Simon "Ghost" Riley')
        self.assertEqual(
            self.service.return_list(), [[100, 'Simon "Ghost" Riley'], [102, 'John Price'], [103, 'Kyle Garrick']]
        )

        # Try to update a non-existent client
        with self.assertRaises(IDNotFoundError):
            self.service.update(200, '3', 'gbrtv')

class TestClientServiceT(unittest.TestCase):
    def setUp(self):
        # Set up a fresh ClientService instance before each test
        self.service = ClientService(ClientTextRepo('clients.t'))

    def test_add(self):
        # Test adding a valid client
        client1 = Client(100, 'Simon Riley')
        self.service.add(client1)
        self.assertEqual(self.service.return_list(), [[100, 'Simon Riley']])

        # Test adding a client with invalid ID
        with self.assertRaises(ValueError):
            invalid_client = Client('dcf', 'name')
            self.service.add(invalid_client)

        # Test adding a client with duplicate ID
        with self.assertRaises(DuplicateIDError):
            duplicate_client = Client(100, 'name')
            self.service.add(duplicate_client)

        # Test adding more clients
        self.service.add(Client(101, 'John MacTavish'))
        self.service.add(Client(102, 'John Price'))
        self.service.add(Client(103, 'Kyle Garrick'))

    def test_remove(self):
        # Add clients first to ensure remove works
        self.service.add(Client(100, 'Simon Riley'))
        self.service.add(Client(101, 'John MacTavish'))
        self.service.add(Client(102, 'John Price'))
        self.service.add(Client(103, 'Kyle Garrick'))

        # Remove a valid client by ID
        self.service.remove(101)
        self.assertEqual(
            self.service.return_list(), [[100, 'Simon Riley'], [102, 'John Price'], [103, 'Kyle Garrick']]
        )

        # Try to remove a non-existent client
        with self.assertRaises(IDNotFoundError):
            self.service.remove(200)

    def test_update(self):
        # Add clients first to ensure update works
        self.service.add(Client(100, 'Simon Riley'))
        self.service.add(Client(102, 'John Price'))
        self.service.add(Client(103, 'Kyle Garrick'))

        # Update client name
        self.service.update(100, '2', 'Simon "Ghost" Riley')
        self.assertEqual(
            self.service.return_list(), [[100, 'Simon "Ghost" Riley'], [102, 'John Price'], [103, 'Kyle Garrick']]
        )

        # Try to update a non-existent client
        with self.assertRaises(IDNotFoundError):
            self.service.update(200, '3', 'geef')

# class TestBookService:
#     def __init__(self):
#         self.service = BookService(BookMemoryRepo)
#
#     def test_add(self):
#         book = Book(100, 'title1', 'author1')
#         self.service.add(book)
#         assert self.service.return_list() == [[100, 'title1', 'author1']]
#
#         self.service.add(Book(101, 'Modern Warfare 2: Ghost', 'Lapham/West'))
#         self.service.add(Book(102, 'title3', 'author3'))
#
#         try:
#             book = Book('dcf', 'title', 'author')
#             self.service.add(book)
#             assert False
#         except ValueError:
#             assert True
#
#         try:
#             book = Book(100, 'title', 'author')
#             self.service.add(book)
#             assert False
#         except DuplicateIDError:
#             assert True
#
#     def test_remove(self):
#         self.service.remove(101)
#         assert self.service.return_list() == [[100, 'title1', 'author1'], [102, 'title3', 'author3']]
#
#         try:
#             self.service.remove(200)
#             assert False
#         except IDNotFoundError:
#             assert True
#
#     def test_update(self):
#         self.service.update(102, '1', 104)
#         assert self.service.return_list() == [[100, 'title1', 'author1'], [104, 'title3', 'author3']]
#
#         self.service.update(104, '2', 'title5')
#         assert self.service.return_list() == [[100, 'title1', 'author1'], [104, 'title5', 'author3']]
#
#         self.service.update(104, '3', 'author6')
#         assert self.service.return_list() == [[100, 'title1', 'author1'], [104, 'title5', 'author6']]
#
#         try:
#             self.service.update(200, '3', 'author')
#             assert False
#         except IDNotFoundError:
#             assert True


# class TestClientService:
#     def __init__(self):
#         self.service = ClientService(ClientMemoryRepo)
#
#     def test_add(self):
#         client = Client(100, 'Simon Riley')
#         self.service.add(client)
#         assert self.service.return_list() == [[100, 'Simon Riley']]
#
#         try:
#             client = Client('dcf', 'name')
#             self.service.add(client)
#             assert False
#         except ValueError:
#             assert True
#
#         try:
#             client = Client(100, 'name')
#             self.service.add(client)
#             assert False
#         except DuplicateIDError:
#             assert True
#
#
#         self.service.add(Client(101, 'John MacTavish'))
#         self.service.add(Client(102, 'John Price'))
#         self.service.add(Client(103, 'Kyle Garrick'))
#
#     def test_remove(self):
#         self.service.remove(101)
#         assert self.service.return_list() == [[100, 'Simon Riley'], [102, 'John Price'], [103, 'Kyle Garrick']]
#
#         try:
#             self.service.remove(200)
#             assert False
#         except IDNotFoundError:
#             assert True
#
#     def test_update(self):
#         self.service.update(102, '1', 104)
#         assert self.service.return_list() == [[100, 'Simon Riley'], [104, 'John Price'], [103, 'Kyle Garrick']]
#
#         self.service.update(100, '2', 'Simon "Ghost" Riley')
#         assert self.service.return_list() == [[100, 'Simon "Ghost" Riley'], [104, 'John Price'], [103, 'Kyle Garrick']]
#
#         try:
#             self.service.update(200, '1', 104)
#             assert False
#         except IDNotFoundError:
#             assert True

if __name__ == "__main__":
    unittest.main()
#     test_book = TestBookService()
#     test_book.test_add()
#     test_book.test_remove()
#     test_book.test_update()
#
#     test_client = TestClientService()
#     test_client.test_add()
#     test_client.test_remove()
#     test_client.test_update()