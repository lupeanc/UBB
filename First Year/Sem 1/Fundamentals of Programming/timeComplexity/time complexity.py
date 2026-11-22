import random
import time


#gnerating lists
def genList(nbel : int):
    l=[]
    for i in range(0, nbel):
        l.append(random.randint(1, 1000))
    return l

#search function
def interpolationSearch(l , x):
    left=0
    right=len(l)-1
    if x == l[right]:
        return right
    while left <= right and l[left] <= x <= l[right]:
        pos=left+((right-left) // (l[right] - l[left]) * (x - l[left]))
        if x == l[pos]:
            return pos
        elif x > l[pos]:
            left = pos + 1
        else:
            right = pos -1
    return -1

#sort functions
#Time complexity: O(n^2) in all cases
def exchangeSort(l : list):
    nel=len(l)
    for i in range(0, nel-1):
        for j in range(i+1, nel):
            if l[i]>l[j]:
                t=l[i]
                l[i]=l[j]
                l[j]=t
    return l

#Time complexity:
#   O(n) - Best case (already sorted)
#   O(n^2) - Average & Worst cases (Worst = sorted in a descending order)
def gnomeSort(l : list):
    i=0
    nel=len(l)
    while i < nel:
        if i == 0:
            i = i+1
        if l[i] >= l[i-1]:
            i = i+1
        else:
            l[i], l[i-1] = l[i-1], l[i]
            i = i-1
    return l

#gives user the possibility to generate a list after pressing '2'
def cmd1():
    print("Please generate a list frist.")
    cmd=input(">")
    if(cmd == '0'):
        exit()
    while(cmd!='1'):
        print("Please generate a list first.")
        cmd=input(">")
    while True:
        try:
            nbel = int(input("Number of elements: "))
            break
        except ValueError:
            print("Number of elements has to be an integer.")
    lstofel=genList(nbel)
    print(lstofel)
    return genList(nbel)

#user input
print("Please select one of the following instructions:")
print("1: Generate list")
print("2: Search for x")
print("3: Time complexity for the used sorting algorithms")
print("0: Quit")

while True:
    print("Command:")
    command=input(">").strip()

    if command == '1':
        while True:
            try:
                nbel=int(input("Number of elements: "))
                break
            except ValueError:
                print("Number of elements has to be an integer.")
        lst = genList(nbel)
        print(lst)
    elif command == '2':
        try:
            lst
        except NameError:
            lst=cmd1()
        print("In order to search for an element, the list must be sorted.")
        print("Please choose a method of sorting:")
        print("1: Exchange Sort")
        print("2: Gnome Sort")
        print("3: Exit Sort Menu")

        while True:
            print("Sort type:")
            typesort=input(">>").strip()

            while typesort != '1' and typesort != '2' and typesort != '3':
                print("Unrecognised command.")
                typesort=input(">>").strip()

            if typesort == '1':
                while True:
                    try:
                        slst = exchangeSort(lst)
                        break
                    except ValueError:
                        print("Step has to be an integer.")
                        print()
            elif typesort == '2':
                while True:
                    try:
                        slst = gnomeSort(lst)
                        break
                    except ValueError:
                        print("Step has to be an integer.")
                        print()
            else:
                break
            print("What number would you like to search for?")

            while True:
                try:
                    x=int(input("x = "))
                    break
                except ValueError:
                    print("x has to be an integer.")
                    print()
            if interpolationSearch(slst, x) == -1:
                print(x, " does not exist in the generated list.")
            else:
                print(x, " is on position number ", interpolationSearch(slst, x)+1)
            break
    elif command == '3':
        nbel = 500

        print("Which case would you like to time?")
        print("1: Best")
        print("2: Average")
        print("3: Worst")

        while True:
            try:
                case = int(input(">>>"))
                if(case <= 3):
                    break
            except ValueError:
                print("Unrecognised command")
                print()

        while nbel<=8000:
            tlist = genList(nbel)
            if case == 1:
                tlist.sort()

                timestart = time.time()
                exchangeSort(tlist)
                timeend = time.time()
                timeexchange= timeend - timestart

                timestart = time.time()
                gnomeSort(tlist)
                timeend = time.time()
                timegnome = timeend - timestart

                print(nbel, " elements:")
                print("Exchange Sort: ", timeexchange)
                print("Gnome Sort: ", timegnome)
                print()
            elif case == 2:
                timestart = time.time()
                exchangeSort(tlist)
                timeend = time.time()
                timeexchange = timeend - timestart

                timestart = time.time()
                gnomeSort(tlist)
                timeend = time.time()
                timegnome = timeend - timestart

                print(nbel, " elements:")
                print("Exchange Sort: ", timeexchange)
                print("Gnome Sort: ", timegnome)
                print()
            else:
                tlist.sort(reverse=True)

                timestart = time.time()
                exchangeSort(tlist)
                timeend = time.time()
                timeexchange = timeend - timestart

                timestart = time.time()
                gnomeSort(tlist)
                timeend = time.time()
                timegnome = timeend - timestart

                print(nbel, " elements:")
                print("Exchange Sort: ", timeexchange)
                print("Gnome Sort: ", timegnome)
                print()
            nbel = nbel * 2
    elif command == '0':
        break
    else:
        print("Unrecognised command or file")
        print()