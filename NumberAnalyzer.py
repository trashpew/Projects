#not done
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
    Length()
    OddLength()
    EvenLength()
    PrimeLength()
    Max()
    Min()
    Range()
    Sum()
    Mean()

def Length():
    num = len(list)
    print("Our list has a length of {}".format(num))
  
def OddLength():
    m = 0
    for n in range(len(list)):
        c = list.index(n)
        if c % 2 == 1:
            m = m + 1
    print("There are {} odd numbers.".format(m))
    
def EvenLength():
    m = 0
    for n in range(len(list)):
        c = list.index(n)
        if c % 2 == 0:
            m = m + 1
    print("There are {} even numbers.".format(m))

def PrimeLength():
    m = 0
    for n in range(len(list)):
        c = list.index(n)
        for p in range(2, int(c ** (1/2))):
            if c % p == 0:
                break
            elif p == int(c ** (1/2)):
                m = m + 1
                break
    print("There are {} prime numbers.".format(m))
        
Start()
