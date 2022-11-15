# A program to summate all even numbers in a list, 
# and then summate all the odd numbers in the same list.

import os, sys

global sum_list, sumeven, sumodd
sum_list, sumeven, sumodd = [], [], []

def Start():
  global length
  print("How long should our list be?")
  length = int(input())
  for i in range(1, length + 1):
    print("What should number {} be?".format(i))
    sum_list.append(input())
  Sum_Check()

def Repeat():
  print()
  print("Would you like to use the program again (y/n):")
  cmd = input()
  if cmd[0] == 'y' or 'Y':
    os.system('clear')
    Start()
  elif cmd[0] == 'n' or 'N':
    print("Thank you for using the program.")
    quit()
    

def Print():
  sume = sum(sumeven)
  sumo = sum(sumodd)
  print("\n"
        "Given the list, {}, \n\n"
        "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= \n"
        "The sum of all even numbers is {}. \n"
        "The sum of all odd numbers is {}.".format(sum_list, sume, sumo))
  Repeat()

def Sum_Check():
  for i in range(length):
    if int(sum_list[i]) % 2 == 0:
      x = int(sum_list[i])
      sumeven.append(x)
    if int(sum_list[i]) % 2 == 1:
      x = int(sum_list[i])
      sumodd.append(x)
  Print()
  
Start()

