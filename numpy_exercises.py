import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

#1
print("There are", len(a[a < 0]), "negative numbers.")

#2
print("There are", len(a[a > 0]), "positive numbers.")

#3
b = a[a>0]
print("There are", len(b[b%2 ==0]), "positive even numbers.")

#4
c = a + 3
print("Adding 3 to each data point give the positive numbers would be:", c[c>0])

#5
a_squared = a ** 2
print("If we square every value in a, the number mean would be:", a_squared.mean(), "THe new standard deviation would be:", a_squared.std())

#6
a_centered = a - (a.mean())
print("The centered data is:", a_centered, "The mean of the centered data is:", a_centered.mean())

#7 
a_z_score = (a - (a.mean()))/(a.std())
print("The z-scores of each point are:", a_z_score)

# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
a_array = np.array(a)
print("The sum of a is:", a_array.sum())
# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
print("The minimum of a is:", a_array.min())

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
print("The maximum of a is:", a_array.max())

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum(a)/len(a)
print("The mean of a is:", a_array.mean())
# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
def product(list):
    result = 1
    for item in list:
        result = result * item 
    return result 
product_of_a = product(a)
print("The product of a is", a_array.prod())
# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
def squared(list):
    new_list = []
    for item in list:
        item = item ** 2
        new_list.append(item)
    return new_list 
squares_of_a = squared(a)
print("The square of all the values in a is:", np.square(a_array))
# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
def find_odd(list):
    list_of_odds = []
    for item in list:
        if item % 2 != 0:
            list_of_odds.append(item)
    return list_of_odds
odds_in_a = find_odd(a)
print("The odd numbers in a are:", a_array[a_array% 2 != 0])
# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
def find_even(list):
    list_of_even = []
    for item in list:
        if item % 2 == 0:
            list_of_even.append(item)
    return list_of_even
evens_in_a = find_even(a)
print("The even numbers in a are:", a_array[a_array% 2 == 0])

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
b_matrix = np.array(b)
print("The sum of b", np.sum(b_matrix))

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1]) 
print("The min of b is", np.min(b_matrix)) 

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
print("The max of b is", np.max(b_matrix))

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
print("The sum of b is", np.sum(b_matrix))
# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
print("The product of b is", np.prod(b_matrix))
# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
print("The square of every value in b is:", np.square(b_matrix))

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
print("The odd values in b are:", b_matrix[b_matrix % 2 != 0])
# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
print("The even values in b are:", b_matrix[b_matrix % 2 == 0])

# Exercise 9 - print out the shape of the array b.
print("The shape of b is:", np.shape(b_matrix))
# Exercise 10 - transpose the array b.
transposed_matrix = [[0,0],
    [0 ,0],
    [0 ,0]]
for i in range(len(b)):
    for j in range(len(b[0])):
        transposed_matrix[j][i] = b[i][j]

print("The transpoed b matrix is:", b_matrix.transpose())
    
# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
list_of_b = []
for i in range(len(b)):
    for j in range(len(b[0])):
        list_of_b.append(b[i][j])
print("The single list is:", b_matrix.tolist()[0])
# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
six_lists = []
for i in range(len(b)):
    for j in range(len(b[0])):
         six_lists.append(b[i][j])
def list_of_lists(list):
    return [[item] for item in list]
list_of_six_lists = list_of_lists(six_lists)
print("The list of lists is:", b_matrix.reshape(6, 1).tolist())



## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
c_array = np.array(c).flatten()
print("Min:", c_array.min(), "\n Max:", c_array.max(), "\n Sum:", c_array.max(), "\n Product:", c_array.prod())
# Exercise 2 - Determine the standard deviation of c.
print("\n Standard Deviation:", c_array.std())
# Exercise 3 - Determine the variance of c.
print("\n Variance:", c_array.var())
# Exercise 4 - Print out the shape of the array c
c_matrix = np.array(c)
print("C matrix", c_matrix)
print(c_matrix.shape)

# Exercise 5 - Transpose c and print out transposed result.
print(c_matrix.transpose())

# Exercise 6 - Get the dot product of the array c with c. 
print(np.dot(c_matrix, c_matrix))

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
c_transpose = np.transpose(c_matrix)
product_of_c = c_matrix * c_transpose
print(np.sum(c_matrix*c_transpose))
# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
print(product_of_c.prod())

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d
d_matrix = np.array(d)
print(np.sin(d_matrix))

# Exercise 2 - Find the cosine of all the numbers in d
print(np.cos(d_matrix))
# Exercise 3 - Find the tangent of all the numbers in d
print(np.tan(d_matrix))
# Exercise 4 - Find all the negative numbers in d
print(d_matrix[d_matrix <0])
# Exercise 5 - Find all the positive numbers in d
print(d_matrix[d_matrix > 0])
# Exercise 6 - Return an array of only the unique numbers in d.
print(np.unique(d_matrix))
# Exercise 7 - Determine how many unique numbers there are in d.
print("There are", len(np.unique(d_matrix)), "unique values in d.")
# Exercise 8 - Print out the shape of d.
print("The shape of d is:", np.shape(d_matrix))
# Exercise 9 - Transpose and then print out the shape of d.
d_tranpose = d_matrix.transpose()
print("The shape of d transposed is:", np.shape(d_tranpose))
# Exercise 10 - Reshape d into an array of 9 x 2
print(d_matrix.reshape(9,2))