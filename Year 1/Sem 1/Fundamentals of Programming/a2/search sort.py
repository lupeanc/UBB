import random

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
def exchangeSort(l : list, step : int):
    nel=len(l)
    nostep=0
    for i in range(0, nel-1):
        for j in range(i+1, nel):
            if l[i]>l[j]:
                t=l[i]
                l[i]=l[j]
                l[j]=t
                nostep=nostep+1
                if(nostep%step == 0):
                    print(l)
    print(l)
    return l

def gnomeSort(l : list, step : int):
    i=0
    nel=len(l)
    nostep=0
    while i < nel:
        if i == 0:
            i = i+1
        if l[i] >= l[i-1]:
            i = i+1
        else:
            l[i], l[i-1] = l[i-1], l[i]
            i = i-1
            nostep = 1+nostep
            if nostep % step == 0:
                print(l)
    print(l)
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
                        step = int(input("step = "))
                        slst = exchangeSort(lst, step)
                        break
                    except ValueError:
                        print("Step has to be an integer.")
                        print()
            elif typesort == '2':
                while True:
                    try:
                        step = int(input("step = "))
                        slst = gnomeSort(lst, step)
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
    elif command == '0':
        break
    else:
        print("Unrecognised command or file")
        print()