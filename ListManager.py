import sys

global list
list = []

bar = "=+=+=+=+=+=+=+=+=+=+=+=+="


def Default():
    print(bar, '\n')
    print("Your list is: {}".format(list))
    print("Would you like to:")
    print("1, Add an item?")
    print("2, Subtract an item?")
    print("3, Swap two spots?")
    print("4, Clear the list?")
    print("5, Quit?")
    print("Input:")
    cmd = int(input())
    if cmd == 1:
        add()
    elif cmd == 2:
        sub()
    elif cmd == 3:
        swap()
    elif cmd == 4:
        clear()
    elif cmd == 5:
        print("Are you sure you want to exit? (y/n)")
        cmd = input()
        if cmd == 'y' or cmd == 'Y':
            sys.exit()
        if cmd == 'n' or cmd == 'N':
            Default()
    else:
        print("Invalid input; try again:")


def add():
    print("What string would you like to add:")
    add = input()
    list.append(add)
    print("You successfully added {} to your list.".format(add))
    Default()


def sub():
    print("Would you like to swap by:")
    print("1: Index?")
    print("2: String?")
    cmd = int(input())
    if cmd == 1:
        print("What index (from 0) do you want to remove:")
        sub = int(input())
        if len(list) >= sub:
            print("You successfully removed: {}".format(list[sub]))
            list.pop(sub)
            Default()
        else:
            print("Index is not in list.")
            Default()
    elif cmd == 2:
        print("What string do you want to remove:")
        sub = input()
        if sub in list:
            sub1 = list.index(sub)
            print("You successfully removed: {}".format(list[sub1]))
            list.pop(sub1)
            Default()
        else:
            print("String is not in list.")
            Default()

def swap():
    print("Would you like to swap by:")
    print("1: Index?")
    print("2: String?")
    cmd = int(input())
    if cmd == 1:
        print("Which two indexes would you want to swap (from 0):")
        print("First:")
        swap1 = int(input())
        print("Second:")
        swap2 = int(input())
        if swap1 and swap2 in list:
            list[swap1], list[swap2] = list[swap2], list[swap1]
            print("You successfully swapped index {} and {}".format(swap1, swap2))
        else:
            print("Error: invalid input.")
    if cmd == 2:
        print("First:")
        swap1 = input()
        print("Second:")
        swap2 = input()
        if swap1 and swap2 in list:
            b = list.index(swap2)
            a = list.index(swap1)
            list[a], list[b] = list[b], list[a]
            print("You successfully swapped {} and {}".format(swap1, swap2))
        else:
            print("Error: invalid input.")
    Default()


def clear():
    global list
    print("Are you sure you want to clear your list? (y/n)")
    cmd = input()
    if cmd == 'y' or cmd == 'Y':
        list = []
        print("You successfully cleared your list.")
        Default()
    if cmd == 'n' or cmd == 'N':
        Default()


Default()

