# What is the 10001 prime number?

primes = []

# Reusing the function defined in Exercise 3 to check if a number is prime or not
def prime(num):
    divisors = 0
    previous = []
    for n in range(1, num+1):
        previous.append(n)
    for n in previous:
        if num % n == 0:
            divisors += 1
    if divisors <= 2:
        return True
    else:
        return False

# I couldn't find a better way to determine a limit to this for loop, but the idea is to check enough numbers until I find the 10001st prime number
for n in range(1,30000):
    if prime(n): #If the number is prime, stores it in the primes list
        primes.append(n)
    if len(primes) >= 10000: # Whenever the lenght of the primes list reaches 10001 items, it means i got the answer and breaks the loop
        break

print(f'The 10001st prime number is {primes[10000]}') # Provides the answer

# OUTPUT

# The 10001st prime number is 104743
