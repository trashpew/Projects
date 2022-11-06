import sys

print("What should our dividend be:")
p = int(input())

i = 0
while True:
    i = i + 1
    for div in range(2, p + 1): # end range parameters need to be one higher, hence p + 1
        if i % div == 0:
            if div == p:
                print(i)
                sys.exit()
            continue
        else:
            break

'''
This code is sprung from the question:
"What is the lowest number divisible by all numbers 1-10?"
Our dividend can be 10, and it will output the answer, for instance.
''' 
