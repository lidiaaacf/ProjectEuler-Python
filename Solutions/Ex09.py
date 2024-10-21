# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a**2 + b**2 = c**2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

# c = root of (a**2 + b**2)
# b = root of (c**2 - a**2)
# a = root of (c**2 - b**2)

# 3 + 4 + 5 = 12
# a + b + c = 1000

def findProduct(sum):
    for a in range(1, sum//3): # a has to be lower than a third of 1000
        for b in range(1, sum//2): # b has to be lower than half of 1000
            c = sum - a - b # c is equal 1000 minus a and b
            if a**2 + b**2 == c**2: # verifying if its a triplet
                return a,b,c,a*b*c # if true returns a, b, c and the product abc

triplet = findProduct(1000)
a, b, c, abc = triplet # Catching the values returned in findProduct function
print(f'Triplet: {a}, {b} and {c}.\nProduct: {abc}') # Providing the answer

# OUTPUT

# Triplet: 200, 375 and 425.
# Product: 31875000