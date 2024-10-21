# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below two million.

# This exercise was very similar to ex 3 so I just focused on optimizing the logic of the prime function, 
# that worked previously but now was unable to do the work due to the large numbers

import math

def prime(limit):
    if limit < 2:
        return []
    primes = [True] * limit
    primes[0] = primes[1] = False  
    for i in range(2, int(math.sqrt(limit)) + 1):
        if primes[i]:
            for j in range(i * i, limit, i):
                primes[j] = False
    return primes

num = 2000000
sumPrimes = 0
prime_flags = prime(num)

for i in range(num):
    if prime_flags[i]:
        sumPrimes += i

print(f'The sum of the prime numbers below 2 million is {sumPrimes}')

# OUTPUT

# The sum of the prime numbers below 2 million is 142913828922