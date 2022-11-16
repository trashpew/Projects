# A (bounded) series approximation (It's awesome, I know)

import math

def bar():
    print("+=+=+=+=+=+=+=+=+=+=+")

def Start():
    global lower, upper
    print("(Note: All series are one step and integer based [duh]) \n"
          "All are formatted as: 'Series Type (Options)' \n"
          "What type of series should we approximate? \n"
          "1: Integer Series? \n"
          "2: Reciprocal Series (Odd/Even/Square)? \n"
          "3: Power Series (n'th)? \n"
          "4: 1, but Alternating? \n"
          "5: 2, but Alternating? \n"
          "6: 3, but Alternating? \n"
          "Input:")
    cmd = int(input())
    bar()
    print("What should our lower bound be? \n"
          "Input:")
    lower = int(input())
    bar()
    print("What should our upper bound be? \n"
          "Input:")
    upper = int(input())
    bar()
    if cmd == 1:
        Integer()
    elif cmd == 2:
        Recip()
    elif cmd == 3:
        Power()
    elif cmd == 4:
        IntegerAlt()
    elif cmd == 5:
        RecipAlt()
    elif cmd == 6:
        PowerAlt()

def Integer():
    global final
    global series
    nums = []
    series = 'Naturals'
    for i in range(lower, upper + 1):
        nums.append(i)
    final = sum(nums)
    Print()

def IntegerAlt():
    global final
    global series
    nums = []
    series = 'Alternating Naturals'
    for i in range(lower, upper + 1):
        x = (i * ((-1) ** (i - 1)))
        nums.append(x)
    final = sum(nums)
    Print()

def Recip():
    global final
    global series
    nums = []
    print("Do you want to sum:"
          "1: Natural Reciprocals?"
          "2: Even Reciprocals?"
          "3: Odd Reciprocals?"
          "4: Square Reciprocals?"
          "Input:")
    cmd = int(input())
    if cmd == 1:
        series = 'Natural Reciprocals'
        for i in range(lower, upper + 1):
            x = float(1 / i)
            nums.append(x)
        final = math.fsum(nums)
        Print()
    elif cmd == 2:
        series = 'Even Reciprocals'
        for i in range(lower, upper + 1):
            if (i % 2) == 0:
                x = float(1 / i)
                nums.append(x)
        final = math.fsum(nums)
        Print()
    elif cmd == 3:
        series = 'Odd Reciprocals'
        for i in range(lower, upper + 1):
            if (i % 2) == 1:
                x = float(1 / i)
                nums.append(x)
        final = math.fsum(nums)
        Print()
    elif cmd == 4:
        series = 'Square Reciprocals'
        for i in range(lower, upper + 1):
            x = float(1 / (i ** 2))
            nums.append(x)
        final = math.fsum(nums)
        Print()


def RecipAlt():
    global series
    global final
    nums = []
    print("Do you want to sum: \n"
          "1: Alternating Natural Reciprocals? \n"
          "2: Alternating Even Reciprocals? \n"
          "3: Alternating Odd Reciprocals? \n"
          "4: Alternating Square Reciprocals? \n"
          "Input:")
    cmd = int(input())
    if cmd == 1:
        series = 'Alternating Natural Reciprocals'
        for i in range(lower, upper + 1):
            x = ((1 / i) * (((-1) ** (i - 1))))
            nums.append(x)
        final = math.fsum(nums)
        Print()
    elif cmd == 2:
        series = 'Alternating Even Reciprocals'
        for i in range(lower, upper + 1):
            if (i % 2) == 0:
                iter = + 1
                x = float((1 / i) * (-1 ** (iter - 1)))
                nums.append(x)
        final = math.fsum(nums)
        Print()
    elif cmd == 3:
        series = 'Alternating Odd Reciprocals'
        for i in range(lower, upper + 1):
            if (i % 2) == 1:
                x = ((1 / i) * (((-1) ** (i - 1))))
                nums.append(x)
        final = math.fsum(nums)
        Print()
    elif cmd == 4:
        series = 'Alternating Square Reciprocals'
        for i in range(lower, upper + 1):
            x = ((1 / (i ** 2)) * (((-1) ** (i - 1))))
            nums.append(x)
        final = math.fsum(nums)
        Print()

def Power():
  global series
  global final
  print("What should k, our power, be (n ^ k)? \n"
        "Input:")
  k = int(input())
  series = 'Power ({}) Series'.format(k)
  nums = []
  for i in range(lower, upper + 1):
    x = i ** k
    nums.append(x)
  final = math.fsum(nums)
  Print()

def PowerAlt():
  global series
  global final
  print("What should k, our power, be (n ^ k)? \n"
        "Input:")
  k = int(input())
  series = 'Alternating Power ({}) Series'.format(k)
  nums = []
  for i in range(lower, upper + 1):
    x = ((i ** k) * ((-1) ** (i - 1)))
    nums.append(x)
  final = math.fsum(nums)
  Print()
  

def Print():
    for i in range(15):
      print('\n')
    print("    {} \n"
          "########### \n"
          " # \n"
          "  # \n"
          "   #       of {}  \n"
          "  # \n"
          " # \n"
          "########### \n"
          "  n = {}"
          "\n\n"
          "= {}".format(upper, series, lower, final))

      
Start()
