from src.functions import add_transaction, list_of_transactions, modify


def test_a():

    command = 'add 100 out pizza'.split()
    list_of_transactions = add_transaction(command, [])
    assert list_of_transactions == [[4, 100, 'out', 'pizza']]

    command = 'insert 10 50 in gift'.split()
    list_of_transactions = add_transaction(command , list_of_transactions)
    assert list_of_transactions == [[4, 100, 'out', 'pizza'], [10, 50, 'in', 'gift']]

    try:
        command = 'add -1 out pizza'.split()
        add_transaction(command, [])
        assert False
    except ValueError:
        assert True

    try:
        command = 'insert 0 -1 out pizza'.split()
        add_transaction(command, [])
        assert False
    except ValueError:
        assert True

    try:
        command = 'add 67'.split()
        add_transaction(command, [])
        assert False
    except ValueError:
        assert True

    try:
        command = 'add 10 blue pizza'.split()
        add_transaction(command, [])
        assert False
    except ValueError:
        assert True

def test_b():
    list_of_transactions = [[10, 20, 'in', 'gift'], [12, 100, 'out', 'pizza'], [12, 10, 'in', 'salary'], [20, 30, 'in', 'gift']]
    command = 'remove in'.split()
    assert modify(command, list_of_transactions) == [[12, 100, 'out', 'pizza']]

    list_of_transactions = [[10, 20, 'in', 'gift'], [12, 100, 'out', 'pizza'], [12, 10, 'in', 'salary'], [20, 30, 'in', 'gift']]
    command = 'remove out'.split()
    assert modify(command, list_of_transactions) == [[10, 20, 'in', 'gift'], [12, 10, 'in', 'salary'], [20, 30, 'in', 'gift']]

    list_of_transactions = [[10, 20, 'in', 'gift'], [12, 100, 'out', 'pizza'], [12, 10, 'in', 'salary'],[20, 30, 'in', 'gift']]
    command = 'remove 12'.split()
    assert modify(command, list_of_transactions) == [[10, 20, 'in', 'gift'], [20, 30, 'in', 'gift']]

    list_of_transactions = [[10, 20, 'in', 'gift'], [12, 100, 'out', 'pizza'], [12, 10, 'in', 'salary'], [20, 30, 'in', 'gift']]
    command = 'remove 10 to 13'.split()
    assert modify(command, list_of_transactions) == [[20, 30, 'in', 'gift']]

    list_of_transactions = [[10, 20, 'in', 'gift'], [12, 100, 'out', 'pizza'], [12, 10, 'in', 'salary']]
    command = 'replace 10 in gift with 100'.split()
    assert modify(command, list_of_transactions) == [[10, 100, 'in', 'gift'], [12, 100, 'out', 'pizza'], [12, 10, 'in', 'salary']]

    try:
        list_of_transactions = [[10, 20, 'in', 'gift'], [12, 100, 'out', 'pizza'], [12, 10, 'in', 'salary']]
        command = 'replace 10 in pizza with 100'.split()
        modify(command, list_of_transactions)
        assert False
    except NameError:
        assert True

    try:
        list_of_transactions = [[10, 20, 'in', 'gift'], [12, 100, 'out', 'pizza'], [12, 10, 'in', 'salary']]
        command = 'replace smthsilly in pizza with 100'.split()
        modify(command, list_of_transactions)
        assert False
    except ValueError:
        assert True

    try:
        list_of_transactions = [[10, 20, 'in', 'gift'], [12, 100, 'out', 'pizza'], [12, 10, 'in', 'salary']]
        command = 'replace 10 in pizza with yf'.split()
        modify(command, list_of_transactions)
        assert False
    except ValueError:
        assert True


test_a()

test_b()