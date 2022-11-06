print("What n'th prime should we find:")
prime = int(input())
p = 1
n_iter = 1
while n_iter <= (prime - 2):
    p = p + 2
    div = 1
    while div < (p / 3):
        div = div + 2
        if (p % div) == 0:
            break
        if div >= (p / 3):
            n_iter += 1

print("The {}'th prime is {}".format(prime, p))


'''
Works on my IDE at home; 
would work on trinket given an infinite amount of time.
'''