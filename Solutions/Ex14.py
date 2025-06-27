# The following iterative sequence is defined for the set of positive integers: 
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence: 

# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

starting_num = 1
highest_sequence = 0
result = 0

while starting_num < 1000000:
    sequence = []
    num = starting_num
    sequence.append(num)
    while num > 1:
        if num % 2 == 0:
            next_num = num // 2
        else:
            next_num = 3 * num + 1
        sequence.append(next_num)
        num = next_num
    if len(sequence) > highest_sequence:
        result = starting_num
        highest_sequence = len(sequence)
    starting_num += 1
        
print(result) 

# OUTPUT 

# 837799