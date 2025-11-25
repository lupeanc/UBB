"""
GETTERS & SETTERS
"""
def get_product_name(command, x):
    return command[x]

def get_quantity(command, x):
    if int(command[x]) > 0:
        return int(command[x])
    else:
        raise ValueError("Quantity must be a positive integer")

def get_item_price(command, x):
    if int(command[x]) > 0:
        return int(command[x])
    else:
        raise ValueError("Price must be a positive integer")

def create_product(command):
    product = []

    product_name = get_product_name(command, 1)
    product.append(product_name)

    quantity = get_quantity(command, 2)
    product.append(quantity)

    item_price = get_item_price(command, 3)
    product.append(item_price)

    return product

def to_str(list_of_products):
    for product in list_of_products:
        for i in range(3):
            product[i] = str(product[i])
    return list_of_products

"""
FUNCTIONS
"""
def add_prod(command, list_of_products):
    if len(command) != 4:
        raise ValueError("Invalid command")
    else:
        product = create_product(command)
        list_of_products.append(product)

        return list_of_products

def remove_prod(command, list_of_products):
    """
    Removes products with prices smaller/bigger than the one specified
    :param command: the command split up
    :param list_of_products: current list of products
    :return: new list of products with according prices
    """
    changed_list =[]
    if command[1] == '<':
        for product in list_of_products:
            command_price = int(command[2])
            item_price = get_item_price(product, 2)

            if item_price >= command_price:
                changed_list.append(product)
        return changed_list
    elif command[1] == '>':
        for product in list_of_products:
            command_price = int(command[2])
            item_price = get_item_price(product, 2)

            if item_price <= command_price:
                changed_list.append(product)
        return changed_list
    else:
        raise ValueError("Unrecognised command")

def test_remove():
    cmd = 'remove < 30'
    command = cmd.split()
    list_of_products = [['napkins', 20, 10], ['games', 30, 100], ['plates', 12, 60]]
    assert remove_prod(command, list_of_products) == [['games', 30, 100], ['plates', 12, 60]]

    cmd = 'remove > 30'
    command = cmd.split()
    list_of_products = [['napkins', 20, 10], ['games', 30, 100], ['plates', 12, 60]]
    assert remove_prod(command, list_of_products) == [['napkins', 20, 10]]

    try:
        cmd = 'remove ads'
        command = cmd.split()
        list_of_products = [['napkins', 20, 10], ['games', 30, 100], ['plates', 12, 60]]
        remove_prod(command, list_of_products)
        assert False
    except ValueError:
        assert True

test_remove()

def display_asc_price(list_of_products):
    list_of_products = to_str(list_of_products)
    asc_price = sorted(list_of_products, key = lambda product: int(product[2]))
    return asc_price

def display_asc_quantity(list_of_products):
    list_of_products = to_str(list_of_products)
    asc_quantity = sorted(list_of_products, key=lambda product: int(product[1]))
    return asc_quantity

