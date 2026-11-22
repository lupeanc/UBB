import random

from src.domain.complex import ComplexNumber
from src.repository.repo_binary import ComplexNumberBinaryRepo
from src.repository.repo_memory import ComplexNumberMemoryRepo
from src.repository.repo_text import ComplexNumberTextRepo


class Functions():
    def __init__(self):
        # self.repo = ComplexNumberMemoryRepo()
        # self.repo = ComplexNumberBinaryRepo()
        self.repo = ComplexNumberTextRepo()

        self.list_of_changes = []  # saves the changes for the undo function

        self.list_of_numbers = []

    def add(self, complex_number):
        """
        Adds complex number to the list
        :param complex_number: complex number that has a real and an imaginary part
        """
        self.list_of_numbers.append(complex_number)
        self.list_of_changes.append(self.list_of_numbers[:])
        self.repo.add(self.list_of_numbers)

    def display(self):
        """
        Displays the list of numbers
        """
        for number in self.list_of_numbers:
            print(number.__str__())

        # for i in range(len(self.list_of_numbers)):
        #     number = self.list_of_numbers[i]
        #     print(number.__str__())

    def filter(self, start, end):
        """
        Keeps the numbers between the stated indices
        :param start: starting index
        :param end: end index
        :return: new list
        """
        self.list_of_numbers = self.list_of_numbers[start - 1 : end]
        self.list_of_changes.append(self.list_of_numbers[:])
        self.repo.add(self.list_of_numbers)

        # new_list = []
        # for i in range(start, end+1):
        #     new_list.append(list_of_numbers[i])
        #
        # list_of_numbers[:] = new_list

    def undo(self):
        """
        undoes the last change
        :return: previous version of the list
        """
        if len(self.list_of_changes) > 0:
            self.list_of_changes.pop()
        if len(self.list_of_changes) > 0:
            self.list_of_numbers = self.list_of_changes[len(self.list_of_changes) - 1]
            self.repo.add(self.list_of_numbers)
        else:
            print("List is empty")

    def initialize(self):
        """
        initializes 10 random numbers in case the list is empty
        :return: list of 10 random complex numbers
        """
        self.list_of_numbers = self.repo.load_data() #checks if there is data to load
        self.list_of_changes.append(self.list_of_numbers[:])

        if len(self.list_of_numbers) == 0:
            for i in range(10):
                number = ComplexNumber(random.randint(1, 10), random.randint(1, 10))
                self.list_of_numbers.append(number)
            self.repo.add(self.list_of_numbers)
            self.list_of_changes.append(self.list_of_numbers[:])

    def return_list(self):
        list_of_numbers = self.list_of_numbers[:]
        return list_of_numbers
