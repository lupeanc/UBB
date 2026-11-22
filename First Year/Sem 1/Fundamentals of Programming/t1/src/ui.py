from src.functions import add_prod, remove_prod, display_asc_price, display_asc_quantity


def menu():
    # list_of_products = []
    list_of_products = [['napkins', 20, 10], ['games', 30, 100], ['plates', 12, 60], ['toys', 40, 5], ['phones', 65, 1300]]
    while True:
        try:
            cmd = input(">")
            command = cmd.split()
            type_of_command = command[0]

            if type_of_command == 'add':
                list_of_products = add_prod(command, list_of_products)

            elif type_of_command == 'remove':
                list_of_products = remove_prod(command, list_of_products)

            elif type_of_command == 'list':
                if command[1] == 'price':
                    print(display_asc_price(list_of_products))
                elif command[1] == 'quantity':
                    print(display_asc_quantity(list_of_products))
                else:
                    raise ValueError("Unrecognised command")
            elif type_of_command == 'exit':
                break
            else:
                raise ValueError("Unrecognised command")
        except ValueError as ve:
            print(ve)


# menu()