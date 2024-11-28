
# What is the value of the first triangle number to have over five hundred divisors?

# Triangle number (1 + 2 + 3 + 4 + 5 ... )

tri = 1
divisors = []

divisorsChecked = []
for n in range(1,1000):
    divisors.append(n)
    if n > 1:
        tri = n + (n - 1)
    for i in divisors:
        if tri % i == 0:
            if i in divisorsChecked:
                pass
            else:
                divisorsChecked.append(i)
    if len(divisorsChecked) >= 500:
        print(f'Divisores: {divisorsChecked}')
        print(f'Número: {tri}')
        break
