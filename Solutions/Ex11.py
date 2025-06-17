# In the 20x20 grid below, four numbers along a diagonal line have been marked in red.

a = [8,   2, 22, 97, 38, 15,  0, 40,  0, 75,  4,  5,  7, 78, 52, 12, 50, 77, 91,  8]
b = [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48,  4, 56, 62,  0]
c = [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30,  3, 49, 13, 36, 65]
d = [52, 70, 95, 23,  4, 60, 11, 42, 69, 24, 68, 56,  1, 32, 56, 71, 37,  2, 36, 91]
e = [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80]
f = [24, 47, 32, 60, 99,  3, 45,  2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50]
g = [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70]
h = [67, 26, 20, 68,  2, 62, 12, 20, 95, 63, 94, 39, 63,  8, 40, 91, 66, 49, 94, 21]
i = [24, 55, 58,  5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72]
j = [21, 36, 23,  9, 75,  0, 76, 44, 20, 45, 35, 14,  0, 61, 33, 97, 34, 31, 33, 95]
k = [78, 17, 53, 28, 22, 75, 31, 67, 15, 94,  3, 80,  4, 62, 16, 14,  9, 53, 56, 92]
l = [16, 39,  5, 42, 96, 35, 31, 47, 55, 58, 88, 24,  0, 17, 54, 24, 36, 29, 85, 57]
m = [86, 56,  0, 48, 35, 71, 89,  7,  5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58]
n = [19, 80, 81, 68,  5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77,  4, 89, 55, 40]
o = [ 4, 52,  8, 83, 97, 35, 99, 16,  7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66]
p = [88, 36, 68, 87, 57, 62, 20, 72,  3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69]
q = [ 4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18,  8, 46, 29, 32, 40, 62, 76, 36]
r = [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74,  4, 36, 16]
s = [20, 73, 35, 29, 78, 31, 90,  1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57,  5, 54]
t = [ 1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52,  1, 89, 19, 67, 48] 

# The product of these numbers is 23 x 63 x 78 x 14 = 1788696.
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally)
# in the grid?

# for each number of the grid, i need to check for all the product possibilities  of 4 adjacent numbers, 
# which will varie according to the index and row of the grid

grid = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t]  

# There is no need to look for numbers in opposites, its redundant 

highest_product = 0
current_index   = 0
current_row     = 0        
        
def find_diagonal_right_up_product(row, number, index): # curr_row, number, curr_index
    """ Findind the next 3 numbers on the right upward diagonal side of the current number """
    if row in [a, b, c] or index in [17, 18, 19]:
        return None
    
    up_right = []
    up_right.append(number)
    for i in range(1,4):
        next_row   = row   - i
        next_index = index + i
        num = grid[next_row[next_index]]
        up_right.append(num)
    product = up_right[0] * up_right[1] * up_right[2] * up_right[3]
    return product
    
def find_horizontal_right_product(row, number, index): # row, number, curr_index
    """ Finding the next 3 numbers on the right side of the current number """
    if index in [17, 18, 19]:
        return None
    
    next_right = []
    next_right.append(number)
    for i in range(1,4):
        next_index = index + i
        num = row[next_index]
        next_right.append(num)
    product = next_right[0] * next_right[1] * next_right[2] * next_right[3]
    return product

def find_diagonal_down_right_product(row, number, index): # curr_row, number, curr_index
    """ Findind the next 3 numbers on the right downward diagonal side of the current number """
    if row in [r, s, t] or index in [17, 18, 19]:
        return None
    
    down_right = []
    down_right.append(number)
    for i in range(1,4):
        next_row   = row   + i
        next_index = index + i
        num = grid[next_row[next_index]]
        down_right.append(num)
    product = down_right[0] * down_right[1] * down_right[2] * down_right[3]
    return product


def find_vertical_down_product(row, number, index): # row, number, curr_index
    """ Finding the next 3 numbers vertically under the current number """
    if row in [r, s, t]:
        return None
    
    next_down = []
    next_down.append(number)
    for i in range(1,4):
        next_row   = row  + i
        num = grid[next_row[index]]
        next_down.append(num)
    product = next_down[0] * next_down[1] * next_down[2] * next_down[3]
    return product

for row in grid:
    for number in row:
        p_a = find_diagonal_right_up_product(current_row, number, current_index)
        p_b = find_horizontal_right_product(row, number, current_index)
        p_c = find_diagonal_down_right_product(current_row, number, current_index)
        p_d = find_vertical_down_product(row, number, current_index)
        
        product = [p_a, p_b, p_c, p_d]
        
        if product > highest_product:
            highest_product = product 
            
        current_index += 1
    current_row += 1
    
         