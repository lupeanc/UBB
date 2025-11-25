from src.domain.complex import ComplexNumber
from src.repository.repo_binary import ComplexNumberBinaryRepo
from src.repository.repo_memory import ComplexNumberMemoryRepo
from src.repository.repo_text import ComplexNumberTextRepo
from src.services.functions import Functions


class UI:
    def __init__(self):
        self.service = Functions()

    def menu(self):
        print("Select one of the following:")
        print("1. Add a number")
        print("2. Display the list of numbers")
        print("3. Filter the list")
        print("4. Undo")
        print("0. Exit")

    def start(self):
        self.service.initialize()
        while True:
            try:
                self.menu()
                command = input(">")

                if command == '1':
                    try:
                        a = int(input("a = "))
                        b = int(input("b = "))
                    except ValueError:
                        raise ValueError("a and b have to be integers")

                    number = ComplexNumber(a, b)
                    self.service.add(number)

                elif command == '2':
                    self.service.display()

                elif command == '3':
                    try:
                        start = int(input("start = "))
                        end = int(input("end = "))
                    except ValueError:
                        raise ValueError("start/end have to be integers")

                    self.service.filter(start, end)

                elif command == '4':
                    self.service.undo()

                elif command == '0':
                    break
                else:
                    raise ValueError("Unrecognised command")
            except ValueError as ve:
                print(ve)

if __name__ == "__main__":
    ui = UI()
    ui.start()