# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from math import gcd # Importing the Greatest Common Divisor function from the Math Library
from functools import reduce 
 
def lcm(x, y): # Lower Common Multiple function that receives two parameters and returns the product of them divided by their gcd
    return (x * y) // gcd(x, y)

LCM = reduce(lcm, range(1, 21)) # Using reduce to apply the function on all 20 numbers
print(LCM) # Providing final answer

# OUTPUT

# 232792560