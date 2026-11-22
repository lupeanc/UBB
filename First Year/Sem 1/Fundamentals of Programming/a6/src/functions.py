#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#
import datetime
from idlelib.pyparse import trans

from texttable import Texttable

list_of_transactions = []

def get_current_day():
    date = datetime.datetime.now()
    day = date.strftime("%d")
    return day
def get_day(command, x):
    return command[x]
def get_amount(command, x):
    return command[x]
def get_type(command, x):
    return command[x]
def get_desc(command, x):
    return command[x]

"""
FUNCTIONS FOR A
"""
# checks if the inserted day is included in [1, 30]
def check_day(day):
    if day < 1 or day > 30:
        raise ValueError("The day inserted must be a number between 1 and 30")

# checks if amount is negative
def check_amount(amount):
    if amount < 0:
        raise ValueError("The amount has to be a positive integer")

# checks if the type is different from 'in' and 'out'
def check_type(type):
    if type != 'in' and type != 'out':
        raise ValueError("Unrecognised command")

"""
FUNCTIONS FOR C
"""
def to_str(list_of_transactions):
    for transaction in list_of_transactions:
        for j in range(len(transaction)):
            transaction[j] = str(transaction[j])

def table(list_of_transactions):

    to_str(list_of_transactions)
    t = Texttable()
    t.add_row(['Nr.Crt'] + ["Day"] + ['Amount'] + ['Type'] + ['Description'])
    nr_crt = 0

    for transaction in list_of_transactions:
        nr_crt +=1
        row = [str(nr_crt)]
        for j in range(len(transaction)):
            row = row + [transaction[j]]
        t.add_row(row)
    return t.draw()

"""
MAIN FUNCTIONS
"""
def add_transaction(command, list_of_transactions):
    """
    Adds transactions according to the user's input
    :param command: the command the user inserted split into separate words
    :param list_of_transactions: the current list of all transactions
    :return: a list containing the added entry
    """

    while True:
        try:
            if command[0] == 'add':

                if len(command) != 4: #checks validity of format by the length of the command
                    raise ValueError("Unrecognised command")

                day = int(get_current_day())
                amount = int(get_amount(command, 1))
                check_amount(amount)
                type = get_type(command, 2)
                check_type(type)
                desc = get_desc(command, 3)

                list_of_transactions.append([day, amount, type, desc])
                # list_changes.append(list_of_transactions)

                return list_of_transactions

            elif command[0] == 'insert':

                if len(command) != 5: #checks validity of format by the length of the command
                    raise ValueError("Unrecognised command")

                try:
                    day = int(get_day(command, 1))
                except ValueError:
                    raise ValueError("Day has to be an int")
                check_day(day)
                amount = int(get_amount(command, 2))
                check_amount(amount)
                type = get_type(command, 3)
                check_type(type)
                desc = get_desc(command, 4)

                list_of_transactions.append([day, amount, type, desc])
                # list_changes.append(list_of_transactions)

                return list_of_transactions

        except ValueError:
            raise ValueError("Unrecognised Command")
        except TypeError:
            raise TypeError("The amount has to be a positive integer")

def modify(command, list_of_transactions):
    """
    Changes the list according to the user's commands
    :param command: user's command
    :param list_of_transactions: current list
    :return: modified list
    """
    cmd = command[0]
    cmd_type = command[1]

    if cmd == 'remove': #remove can have 3 follow ups: one referring to the type (in, out), one referring to a single day (=> length = 2) and one referring to a sequence of days (=> length = 4)
        modified_list = []

        if cmd_type == 'in' or cmd_type == 'out':
            for i in range(len(list_of_transactions)):
                if list_of_transactions[i][2] != cmd_type:
                    modified_list.append(list_of_transactions[i])
            # list_of_transactions = modified_list
            # return list_of_transactions
            return modified_list

        elif len(command) == 2: #command must be of the type 'remove <day>'
            try:
                day = int(command[1])
            except ValueError:
                raise ValueError("Day has to be an int")

            for i in range(len(list_of_transactions)):
                if int(list_of_transactions[i][0]) != day:
                    modified_list.append(list_of_transactions[i])
            # list_of_transactions = modified_list
            # return list_of_transactions
            return modified_list

        elif len(command) == 4: #command must be of the type 'remove <start_day> to <end_day>'
            try:
                start_day = int(command[1])
                end_day = int(command[3])
            except ValueError:
                raise ValueError("Days have to be an int")

            for i in range(len(list_of_transactions)):
                if int(list_of_transactions[i][0]) < start_day or int(list_of_transactions[i][0]) > end_day:
                    modified_list.append(list_of_transactions[i])
            # list_of_transactions = modified_list
            # return list_of_transactions
            return modified_list

        else:
            raise ValueError("Unrecognised Command")

    else: #command must be of the type 'replace <day><type><desc> with <value>
        found = False
        try:
            day = int(get_day(command, 1))
        except ValueError:
            raise ValueError("Day has to be an int")
        type = get_type(command, 2)
        desc = get_desc(command, 3)

        try:
            value = int(get_amount(command, 5))
        except ValueError:
            raise ValueError("Value has to be an int")

        for i in range(len(list_of_transactions)):
            if int(list_of_transactions[i][0]) == day and list_of_transactions[i][2] ==  type and list_of_transactions[i][3] ==  desc:
                found = True
                list_of_transactions[i][1] = value

        if found:
            return list_of_transactions
        else:
            raise NameError("Could not find element")

def display(command, list_of_transactions):
    if command[0] == 'list':
        if len(command) == 1: #list
            return table(list_of_transactions)
        elif len(command) == 2 and (command[1] == 'in' or command[1] == 'out'): #list <type>
            type = command[1]
            list_type = []
            for transaction in list_of_transactions:
                if transaction[2] == type:
                    list_type.append(transaction)

            if len(list_type) > 0:
                return table(list_type)
            else:
                raise ValueError("There are no such transactions")

        elif command[1] == 'balance': #list balance <day>
            try:
                day = int(command[2])
            except ValueError:
                raise ValueError("Day has to be an int")
            # check_day(day)

            balance = 0 #Balance will be 0 if there are no transactions with the inputted day

            for transaction in list_of_transactions:
                if int(transaction[0]) == day:
                    if transaction[2] == 'in':
                        balance = balance + int(transaction[1])
                    else:
                        balance = balance - int(transaction[1])

            return balance

        else:
            if command[1] == '<':
                try:
                    value = int(command[2])
                except ValueError:
                    raise ValueError("Value must be an int")

                list_smaller = []
                for transaction in list_of_transactions:
                    if int(transaction[1]) < value:
                        list_smaller.append(transaction)

                if len(list_smaller) > 0:
                    return table(list_smaller)
                else:
                    raise ValueError("There are no such transactions")

            elif command[1] == '=':
                try:
                    value = int(command[2])
                except ValueError:
                    raise ValueError("Value must be an int")

                list_equal = []
                for transaction in list_of_transactions:
                    if int(transaction[1]) == value:
                        list_equal.append(transaction)

                if len(list_equal) > 0:
                    return table(list_equal)
                else:
                    raise ValueError("There are no such transactions")

            elif command[1] == '>':
                try:
                    value = int(command[2])
                except ValueError:
                    raise ValueError("Value must be an int")

                list_bigger = []
                for transaction in list_of_transactions:
                    if int(transaction[1]) > value:
                        list_bigger.append(transaction)

                if len(list_bigger) > 0:
                    return table(list_bigger)
                else:
                    raise ValueError("There are no such transactions")
            else:
                raise ValueError("Unrecognised command")
    else:
        raise ValueError("Unrecognised command")

def filter_func(command, list_of_transactions):
    if len(command) == 2: #filter <type>
        if command[1] == 'in' or command[1] == 'out':
            type = command[1]
            list_filtered = []
            for transaction in list_of_transactions:
                if transaction[2] == type:
                    list_filtered.append(transaction)
            return list_filtered
        else:
            raise ValueError("Unrecognised command")

    elif len(command) == 3:
        if command[1] == 'in' or command [1] == 'out':
            type = command[1]
            try:
                value = int(command[2])
            except ValueError:
                raise ValueError("Value has to be an int")

            list_filtered = []
            for transaction in list_of_transactions:
                if transaction[2] == type and int(transaction[1]) < value:
                    list_filtered.append(transaction)
            return list_filtered
        else:
            raise ValueError("Unrecognised command")
    else:
        raise ValueError("Unrecognised command")



