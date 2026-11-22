import random


#
# Write the implementation for A5 in this file
#

# 
# Write below this comment 
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
"""
LIST VERS
"""

# def generate_random(n):
#     list_of_numbers = []
#     for i in range(n):
#         complex_number = [random.randint(0, 100),random.randint(0, 100)]
#         list_of_numbers.append(complex_number)
#
#     return list_of_numbers
#
def generate_list(n):
    list_numbers = []
    for i in range(n):
        list_numbers.append(read_number())
    return list_numbers

def get_real(number):
    return number[0]

def get_img(number):
    return number[1]

def to_str(number):
    if get_img(number) < 0 and get_real(number) != 0:
        return "z = " + str(get_real(number)) + " " + str(get_img(number)) + " * i"
    elif get_img(number) == 0:
        if get_real(number) == 0:
            return "z = 0"
        else:
            return "z = " + str(get_real(number))
    elif get_real(number) == 0:
        return "z = " + str(get_img(number)) + " * i"
    else:
        return "z = " + str(get_real(number)) + " + " + str(get_img(number)) + " * i"


#
# Write below this comment 
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

"""
DICT VERS
"""

# def generate_random(n):
#     dict_of_numbers = []
#     for i in range(n):
#         complex_number = {"real" : random.randint(1, 100), "img" : random.randint(1, 100)}
#         dict_of_numbers.append(complex_number)
#
#     return dict_of_numbers
#
# def generate_list(n):
#     list_numbers = []
#     for i in range(n):
#         list_numbers.append(read_number())
#     return list_numbers
#
# def get_real(number):
#     return number["real"]
#
# def get_img(number):
#     return number["img"]
#
# def to_str(number):
#     if get_img(number) < 0 and get_real(number) != 0:
#         return "z = " + str(get_real(number)) + " " + str(get_img(number)) + " * i"
#     elif get_img(number) == 0:
#         if get_real(number) == 0:
#             return "z = 0"
#         else:
#             return "z = " + str(get_real(number))
#     elif get_real(number) == 0:
#         return "z = " + str(get_img(number)) + " * i"
#     else:
#         return "z = " + str(get_real(number)) + " + " + str(get_img(number)) + " * i"



#
# Write below this comment 
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

def problem_a(list_of_numbers):
    """
    Longest subarray of numbers that contain at most 3 distinct values - for a and b
        Eg. For list_nb = [(1, 3) , (1, 2) , (3, 3) , (4, 3), (4, 2), (5,1)]
            max length = 3
            elements = (1, 3) , (1, 2) , (3, 3) - a and b belong to values = [ 1, 2, 3]

    :param list_of_numbers: generated list of complex numbers
    :return: max length and the elements of the subarray with the max length
    """
    values= [] #values for a and b
    elements = [] #elements of the subarray
    max_elements = []

    for i in range(len(list_of_numbers)):
        while len(values)<4 and i<len(list_of_numbers):

            if get_real(list_of_numbers[i]) not in values:
                values.append(get_real(list_of_numbers[i]))
            if len(values)==4:
                break

            if get_img(list_of_numbers[i]) not in values:
                values.append(get_img(list_of_numbers[i]))
            if len(values)==4:
                break

            elements.append(list_of_numbers[i])

            i = i + 1

        if len(elements) > len(max_elements):
            max_elements = elements

        values = []
        elements = []

    return len(max_elements), max_elements

def problem_b(list_of_numbers):
    """
    A longest alternating subsequence, when considering each number's real part
    (e.g., given sequence [1, 3, 2, 4, 10, 6, 1], [1, 3, 2, 10] is an alternating subsequence, because 1 < 3 > 2 < 10)
    :return: max length, the sequence of real parts
    """
    list_of_real = []

    for number in list_of_numbers:  # create a list of all real parts
        list_of_real.append(get_real(number))

    up = [list_of_real[0]] #list for adding a number to the sequence if it's bigger than the previous one
    down = [list_of_real[0]] #list for adding a number to the sequence if it's smaller than the previous one

    for i in range(1, len(list_of_real)):
        real_current = list_of_real[i]
        real_prev = list_of_real[i-1]

        #here we simulate both adding and omitting the current number to the sequence
        if real_current > real_prev:
            up = down + [list_of_real[i]]
        elif real_current < real_prev:
            down = up + [list_of_real[i]]

    if len(up) > len(down):
        return len(up), up
    else:
        return len(down), down

#
# Write below this comment 
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#

def read_number():
    while True:
        try:
            real_part = int(input("a = ").strip())
            img_part = int(input("b = ").strip())
            break
        except ValueError:
            raise ValueError("a and b have to be int")
    return [real_part, img_part]
    # return {"real": real_part, "img": img_part}

def display_list(list_numbers):
    for numbers in list_numbers:
        print(to_str(numbers))

def print_menu():
    print("Please choose one of the following options:")
    print("1. Generate list of complex numbers") #done
    print("2. Display the list of complex numbers") #done
    print("3. Longest subarray of numbers that contain at most 3 distinct values (for a and b)") #done
    print("4. A longest alternating subsequence, when considering each number's real part")
    print("0. Exit program")

if __name__ == "__main__":
#list_of_numbers = generate_random(10)
    while True:
        try:
            print_menu()
            command = input("Command: ").strip()

            if command == '1':
                print("How many complex numbers would you like to add?")
                try:
                    n = int(input("n = ").strip())
                except ValueError:
                    raise ValueError("n has to be an integer")

                print("z = a + b*i")
                list_of_numbers = generate_list(n)

            elif command == '2':
                try:
                    display_list(list_of_numbers)
                except NameError:
                    raise NameError("Generate a list first.")

            elif command == '3':
                list_of_numbers = [(1, 3), (1, 2), (3, 3), (4, 3), (4, 2), (5, 1)]
                try:
                    max_length = problem_a(list_of_numbers)[0]
                    subarray = problem_a(list_of_numbers)[1]
                    print("Max Length = ", max_length, " for the following subarray: ")
                    display_list(subarray)
                except NameError:
                    raise NameError("Generate a list first.")

            elif command == '4':
                list_of_numbers = [(1, 0), (3, 0), (2, 0), (4, 0), (10, 0), (6, 0), (1, 0)]
                try:
                    max_length = problem_b(list_of_numbers)[0]
                    subsequence = problem_b(list_of_numbers)[1]
                    print("Max Length = ", max_length, " for the sequence: ", subsequence)
                except NameError:
                    raise NameError("Generate a list first.")

            elif command == '0':
                break
            else:
                print("Unrecognised command.")
            print()
        except ValueError as ve:
            print(ve)
            print()
        except NameError as ne:
            print(ne)
            print()