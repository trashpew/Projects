
def bar():
    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")

def Start():
    global list
    list = []
    print("How long should our list be? \n"
          "Input:")
    leng = int(input())
    for i in range(leng ):
        print("What should number {} be? \n"
              "Input:".format(i+1))
        list.append(int(input()))
    print("Given the list: {}".format(list))
    bar()
    Length()
    bar()
    OddLength()
    bar()
    EvenLength()
    bar()
    PrimeLength()
    bar()
    Max()
    bar()
    Min()
    bar()
    Range()
    bar()
    Sum()
    bar()
    Mean()
    bar()
    Repeat()
    bar()
def Length():
    num = len(list)
    print("Our list has a length of {}".format(num))
  
def OddLength():
    m = 0
    for n in range(len(list)):
        c = list[n]
        if c % 2 == 1:
            m = m + 1
    print("There are {} odd numbers.".format(m))
    
def EvenLength():
    m = 0
    for n in range(len(list)):
        c = list[n]
        if c % 2 == 0:
            m = m + 1
    print("There are {} even numbers.".format(m))

def PrimeLength():
    m = 0
    for i in range(len(list)):
        c = list[i]
        if c % 2 == 1:
            div = 1
            for div in range(int(c/3)):
                div = div + 2
                if c % div == 0:
                    break
                else:
                    if div == (int(c/3)):
                        m = m + 1
                    else:
                        continue
        else:
            continue
    print("There are {} prime numbers.".format(m))

def Max():
    print("The maximum value is {}.".format(max(list)))
    
def Min():
    print("The minimum value is {}.".format(min(list)))

def Range():
    rg = int(max(list)) - int(min(list))
    print("The range (max - min) is {}.".format(rg))

def Sum():
    s = sum(list)
    print("The sum of the values is {}.".format(s))
  
def Mean():
    s = int(sum(list))
    length = int(len(list))
    mean = s / length
    print("The mean is {}.".format(int(mean)))

def Repeat():
    print("Would you like to use the program again? (y/n)")
    print("Input:")
    cmd = input()

Start()
