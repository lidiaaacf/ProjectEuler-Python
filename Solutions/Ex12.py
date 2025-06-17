
# What is the value of the first triangle number to have over five hundred divisors?

# Triangle number (1 + 2 + 3 + 4 + 5 ... )

num  = 1
tri_num = 0

while True:
    divisors = []
    previous_numbers = []
    for n in range(1,num+1):
        previous_numbers.append(n)
    tri_num = sum(previous_numbers) # correct way: tri_num = num * (num + 1) // 2 
    for n in range(1, tri_num+1):
        if tri_num % n == 0:
            divisors.append(n)
    num += 1
    if len(divisors) >= 501:
        break
        
print(tri_num)    

# OUTPUT 

# 76576500