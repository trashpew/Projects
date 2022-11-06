'''
This code will output all pythagorean triples, from n1 to n2,
which satisfy the condition that (a + b + c) equals some value, n.
This also just prints all pythagorean triples, and sorts by (a + b + c), in actuality.

I'll leave it as an exercise for you to do the derivations necessary for the code in the Math() function.

An interesting note is that all '(a + b + c) = n' require n to be some even number.

Another interesting note comes from within the distribution of these numbers.
Sometimes, gaps of ~20 numbers can go by without a case of '(a + b + c) = n' being true.
(as with 'n = 1302' to 'n = 1320', no numbers satisfy the requirements)
However, numbers such as 'n = 1260' have six different combinations satisfying the case.

Edit: Fixed the code not outputting certain 'n' values; the problem originated
from my anti-duplication (not printing 'a, b' and 'b, a') being overkill.
A set is now used and a value checked against that set.
'''


#

def Math():
    for n in range(n1, n2):
        for a in range(1, int(n / 2)):  # [6]
            for b in range(1, int(n / 2)):
                if ((n * b) + (n * a) - (a * b)) == ((n ** 2) / 2):  # [1]
                    c = int((((a * a) + (b * b)) ** (1 / 2)))  # [2]
                    s = set(a_list)  # [5]
                    if b not in s:
                        a_list.append(a)
                        b_list.append(b)
                        c_list.append(c)
                        n_list.append(n)
    Print()


#

def Intro():
    global n1, n2
    print("Insert a lower bound for our calculator:")
    n1 = int(input())
    print("Insert an upper bound for our calculator:")
    n2 = int(input())
    print('\n'
          "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n"
          "Please give the program sometime to do it's calculations.\n"
          "It will print the results when it is done."
          '\n'
          "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+"
          '\n')
    Math()


#

def Init():
    global c_list, b_list, a_list, n_list
    c_list, b_list, a_list, n_list = [], [], [], []
    Intro()  # [4]


#

def Print():
    result = zip(a_list, b_list, c_list, n_list)
    print("All 'a, b' values are interchangeable ('a, b' can swap places).\n")
    print(*('a = {}, b = {}, c = {} | n = {}'.format(a, b, c, d) for (a, b, c, d) in result), sep="\n")
    # [3]


#

#################

Init()  # [7]

'''
1: The code actually only checks 'a, b' values and checks if they match some product of n.
Using substitution, you can rearrange some theorems to realize all 'a, b' in triples must be
some product value of n to satisfy '(a + b + c) = n'.

2: Because of the previous statement, this line actually creates a 'c' value based off
of the 'a, b' values; I'm finding triples without actually using triples, hence why
this code is so optimized compared to brute force.

3: This took a really long time, I'll never forget to unpack the zip() again.

4: Basically just defining a bunch of empty lists; this function serves no other purpose.

5: Set() is a really cool feature.

6: You only ever need to check until ''a, b' >= (n/2)'. Algebraic inequalities (might) prove this,
but I'm honestly not 100% certain on the math I used to justify it. It's weird, but it works.

7: Init() runs the entire program, since all the functions are intertwined.
'''
