#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#
from datetime import date
from src.functions import add_transaction, modify, display, filter_func, table

def menu():
    list_of_transactions = [[10, 20, 'in', 'gift'], [12, 100, 'out', 'pizza'], [12, 10, 'in', 'salary'], [20, 30, 'in', 'gift']]
    list_of_changes = list_of_transactions[:]
    # list_of_transactions = []
    while True:
        try:
            cmd = input("> ")
            command = cmd.split()

            type_of_command = command[0]

            if type_of_command == 'add' or type_of_command == 'insert':
                list_of_transactions = add_transaction(command, list_of_transactions)
                list_of_changes.append(list_of_transactions)

            elif type_of_command == 'replace' or type_of_command =='remove':
                list_of_transactions = modify(command, list_of_transactions)
                list_of_changes.append(list_of_transactions)

            elif type_of_command == 'list':
                print(display(command, list_of_transactions))

            elif type_of_command == 'filter':
                list_of_transactions = filter_func(command, list_of_transactions)
                list_of_changes.append(list_of_transactions)


            elif type_of_command == 'undo':
                list_of_changes.pop()
                if len(list_of_changes) > 0:
                    list_of_transactions = list_of_changes
                else:
                    print("List is empty")

            elif type_of_command == 'exit':
                break
            else:
                print("Unrecognised Command")
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)
        except NameError as ne:
            print(ne)


menu()