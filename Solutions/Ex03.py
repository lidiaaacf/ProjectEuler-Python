# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143?

num = 600851475143 

# Defining a function to identify if a number is prime or not
def prime(div):
    divisors = 0 
    previous = []
    for n in range(1, div+1): # Taking the previous numbers of the number being checked and saving them on a list
        previous.append(n)
    for n in previous: # Checking if the number is only divided by 1 and himself
        if div % n == 0:
            divisors += 1
    if divisors <= 2: # At the end, if this is true there will be only two numbers on "divisors" (1 and himself)
        return True
    else:
        return False
    
# Defining a function to factor the number
def factor(number):
    primes = []
    for n in range(1,number+1): # Detecting the prime factors of this number using the prime function
        if(prime(n)):
            primes.append(n)
    for n in primes:
        while number % n == 0: # Making the divisor to be used until it is not divisible anymore
            number /= n
    print(f'Largest prime factor of {number}: {n}') # At the end "n" is going to be the last prime factor, therefore the largest one

factor(600851475143) # Calling the function on the number of the question


# OUTPUT

# Largest prime factor of 600851475143: 6857