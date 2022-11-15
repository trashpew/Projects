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
    sys.exit()
  else:
    print("Invald input; try again:")
    
def add():
  print("What string would you like to add:")
  add = input()
  list.append(add)
  print("You successfully added {} to your list.".format(add))
  Default()
  
def sub():
  print("What index (from 0) do you want to remove:")
  sub = int(input())
  print("You successfully removed:")
  list.pop(sub)
  Default()

def swap():
  print("Which two indexes would you want to swap (from 0):")
  print("First:")
  swap1 = int(input())
  print("Second:")
  swap2 = int(input())
  list[swap1], list[swap2] = list[swap2], list[swap1]
  print("You successfully swapped index {} and {}".format(swap1, swap2))
  Default()

def clear():
  list = []
  print("You successfully cleared your list.")
  Default()
  
Default()
