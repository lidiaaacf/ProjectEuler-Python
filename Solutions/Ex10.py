#The sum of the primes below 10 is  2 + 3 + 5 + 7. 
# Find the sum of all the primes below two million.

def sum_primes_below(limit):
    # Create a list of prime numbers
    sieve = [True] * limit
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    
    # Sieve of Eratosthenes algorithm to find all primes up to 'limit'
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False
    
    # Sum up all the primes
    return sum(i for i in range(limit) if sieve[i])

limit = 2000000

result = sum_primes_below(limit)
print(result)

# OUTPUT

# Result: 142913828922