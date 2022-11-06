# Primes (and Special Primes) in a Range

def bar():
    bar = "=-=-=-=-=-=-=-=-=-=-="
    print()
    print(bar)
    print()

def PrimeChecker():
    global p
    global p1
    if (p <= 1):
        p = 3
    if ((p % 2) == 0):
        p = p - 1
    num = p - 2
    rnge = int(((p1 - p) / 2))
    for i in range(rnge):
        num = num + 2
        div = 1
        while (div < (num / 3)):
            div = div + 2
            if ((num % div) == 0):
                break
        if (div >= (num / 3)):
            print(str(num) + " is prime.")

def Intro():
    print("######################################")
    print("# Welcome to Prime Number Calculator #")
    print("#           (Version 3!)             #")
    print("######################################")
    bar()

def Ranger():
    global p
    global p1
    print("(A large range will be slow!)")
    print("Insert Starting Number (lower bound):")
    p = int(input())
    print("Insert an End Number (upper bound):")
    p1 = int(input())
    print("Your range starts at:")
    print(p)
    print("and ends at:")
    print(p1)
    bar()

def Program():
    print("Which primes would you like to print?")
    print("1 = All, 2 = Doubles, 3 = Triples")
    method = int(input())
    bar()
    if method == 1:
        PrimeChecker()
    if method == 2:
        DoublePrimeChecker()
    if method == 3:
        TriplePrimeChecker()

def DoublePrimeChecker():
    LastPrime = -1
    global p
    global p1
    if (p <= 1):
        p = 3
    if ((p % 2) == 0):
        p = p - 1
    num = p - 2
    rnge = int(((p1 - p) / 2))
    for i in range(rnge):
        num = num + 2
        div = 1
        while (div < (num / 3)):
            div = div + 2
            if ((num % div) == 0):
                break
        if (div >= (num / 3)):
            if (LastPrime == (num - 2)):
                print(str(LastPrime) + " and " + str(num) + " are double prime.")
            LastPrime = num

def TriplePrimeChecker():
    LastPrime = 0
    LasterPrime = 0
    global p
    global p1
    if (p <= 1):
        p = 3
    if ((p % 2) == 0):
        p = p - 1
    num = p - 2
    rnge = int(((p1 - p) / 2))
    for i in range(rnge):
        num = num + 2
        div = 1
        while (div < (num / 3)):
            div = div + 2
            if ((num % div) == 0):
                break
        if (div >= (num / 3)):
            if (LasterPrime == (num - 6)):
                print(str(LasterPrime) + " and " + str(LastPrime) + " and " + str(num) + " are triple prime.")
            LasterPrime = LastPrime
            LastPrime = num

############################

Intro()
Ranger()
Program()