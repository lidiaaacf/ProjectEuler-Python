# The four adjacent digits in the 1000-digit number that have the greatest product 
# are 9 x 9 x 8 x 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the 
# greatest product. What is the value of this product?

from math import prod # Imports the prod function from the Math library so I can multiply all the numbers in a sequence
# (Thanks Walter for the hint I wish I knew this sooner lmao)

number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

# Defining the start and the end of the 13 sequence interval (14 because it never counts the last one)
a = 1 
b = 14
majorProduct = 0
intervalList = [] 
numberString = str(number) # Stringfying the number so I can slice it in 13 sequence intervals
intervalString = numberString[a:b] # Defining the first 13 sequence

for i in numberString: 
    for n in intervalString: # For each char in numberString selects the following sequence of 13 characters
        intervalList.append(int(n)) # Converts the char into number again and stores in the intervalList
    multi = prod(intervalList, start=1) # Multiply all the numbers for themselves using prod function
    if multi > majorProduct or majorProduct == 0: # If its the first iteration stores the product anyway (majorPorduct == 0) to later compare with the new products and verify if the newer one is greater
        majorProduct = multi # If true replaces the lower product once saved in the majorProduct variable for the greater one
    intervalList.clear() # Clears the intervalList so it doesn't affect the next iterations
    a += 1 # Increases in one the start and the end of the interval until the entire number is analyzed
    b += 1

print(majorProduct) # Provides the answer

# OUTPUT

# 23514624000
