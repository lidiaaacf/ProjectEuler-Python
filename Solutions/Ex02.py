# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

numberSum = []

def fibonacciSum(limit):
    a, b = 0, 1  # Initialize the first two Fibonacci numbers.
    
    # Continue generating Fibonacci numbers until 'a' exceeds the limit.
    while a <= limit:
        if a % 2 == 0:  # Check if the number is even.
            
            numberSum.append(a)  # Add even numbers to the list.
            
        print(a, end=' ')  # Print the current Fibonacci number.
        a, b = b, a + b  # Update 'a' and 'b' to the next Fibonacci numbers.
        
    # Calculate and print the sum of all even numbers in the list.
    total = sum(numberSum)
    print(f'\nThe total sum of the even numbers of this Fibonacci sequence was: {total}')

# Call the function with a limit of 4 million.
fibonacciSum(4000000)

# OUTPUT

# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 
# 196418 317811 514229 832040 1346269 2178309 3524578
 
# The total sum of the even numbers of this Fibonacci sequence was: 4613732