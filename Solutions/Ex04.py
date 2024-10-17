# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99. 
# Find the largest palindrome made from the product of two-digit numbers.

numbers = range(100,1000) # Defining the range of 100-999 to analyze all the 3-digit numbers
largestPalin = 0 

# I had tried to analyse the numbers starting from the highest (reversed) in attempt of reducing the iterations, but at the end this didn't work and everything had to be executed
for n in reversed(numbers): 
    for m in reversed(numbers): # Doing a for inside the for so I can multiply all the 3-digit numbers between themselves
        product = n * m 
        stringProduct = str(product) # Tranforming the product in a string so I can verify if it's a palindrome

        if stringProduct == stringProduct[::-1]: # Checking if its a palindrome
            if product > largestPalin: # Replacing always the lower palindrome for the higher one
                largestPalin = product # Stores the number in a variable

# Provides the final answer
print(f'Largest palindrome generated as a product of 2 numbers of 3 digits: {largestPalin}')

# OUTPUT

# Largest palindrome generated as a product of 2 numbers of 3 digits: 906609
