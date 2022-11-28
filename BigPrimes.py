# To prove a number is prime, we must verify that it cannot be divided
# by any prime number lower than it's square root.

import sys
primes = []
for i in range(1, 1000000, 2):
    for div in range(3, int(i ** (1/2)) + 1):
        if i % div == 0:
            break
        elif div == int(i ** (1/2)):
            primes.append(i)
num = primes[-1] ** 2
for i in range(num, num + 1000000000, 2):
    for prime in primes:
        if i % prime == 0:
            break
        elif prime == primes[-1]:
            print("{} is a really big prime.".format(i))
            sys.exit()
