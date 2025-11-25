import random

from faker import Faker

from src.domain.client import Client
from src.repository.repo_binary import ClientBinaryRepo
from src.repository.repo_memory import DuplicateIDError, IDNotFoundError, UnrecognisedCommand, ClientMemoryRepo


class ClientService:
    def __init__(self, repo):
        self.list_of_clients = repo.load_data()
        self.repo = repo

    def add(self, client):
        """
                Adds a valid client to the list of books
                :raises DuplicateIDError: if the inputted id is a duplicate
                :param client: client created using the domain Client
                """
        for entity in self.list_of_clients:
            if client.id == entity.id:
                raise DuplicateIDError()

        self.list_of_clients.append(client)
        self.repo.add(self.list_of_clients)

    def remove(self, id):
        """
                Removes a client from the list based on its id
                :raises IDNotFoundError: if the inputted id is not one of the existing ones
                :param id: id is the unique id of a client
                """
        new_list = []
        for client in self.list_of_clients:
            if int(client.id) != int(id):
                new_list.append(client)

        if new_list == self.list_of_clients:
            pass
            # raise IDNotFoundError(f"ID {id} not found. List not modified.")
        else:
            self.list_of_clients = new_list[:]
            self.repo.add(self.list_of_clients)

    def update(self, id, command, update):
        """
                Updates an existing client based in its id
                :raises IDNotFoundError: if the inputted id is not one of the existing ones
                :param id: the id of the book the user wishes to update
                :param command: the field the user wishes to update
                :param update: the new value of the updated field
                """
        found = 0
        for client in self.list_of_clients:
            if client.id == id:
                found = 1
                client.name = update
        if found == 0:

            raise IDNotFoundError(f"ID {id} not found")
        self.repo.add(self.list_of_clients)

    def return_list(self):
        list_of_clients = []
        for client in self.list_of_clients:
            list_of_clients.append([client.id, client.name])
        return list_of_clients

    def search(self, field, search):
        if field == 1:
            try:
                test_search = int(search)
            except ValueError:
                raise ValueError("The inputted id is supposed to be an integer")

        search_list = []
        for client in self.list_of_clients:
            if field == 1:
                if search in str(client.id):
                    search_list.append(client)
            elif field == 2:
                if search.lower() in client.name.lower():
                    search_list.append(client)
            else:
                raise UnrecognisedCommand("Field has to be 1, or 2")

        return search_list

    def initialize(self):
        fake = Faker()
        self.list_of_clients = self.repo.load_data()  # checks if there is data to load

        if len(self.list_of_clients) == 0:
            for id in range(200, 220):
                name = fake.name()
                client = Client(id, name)
                self.list_of_clients.append(client)
            self.repo.add(self.list_of_clients)