# The sum of the squares of all the numbers between 1 and 10 is 385 (1 + 4 + 9 + ... + 100) 
# The square of the sum of all the numbers between 1 and 10 is 3025 (1 + 2 + 3 + ... + 10)^2
# The difference between them is 2640. Find the difference between the first 100 
# natural numbers (1 to 100)

sumSquares = 0
sumThenSquare = 0

# Coursing through all the numbers between 1 and 100 and elevating them by two
for n in range(1,101):
    square = n * n # Catching the square of each number
    sumThenSquare += n # Saving the numbers without elevating to square the sum afterwards
    sumSquares += square # Addind the squared numbers to the sum

result = (sumThenSquare **2) - sumSquares # Elevating the sum of all the numbers and subtracting the other sum
print(result) # Providing the answer

# OUTPUT

# 25164150