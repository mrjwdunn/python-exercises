import math
import numpy as np


def separator():
    print()
    print('--------------------------------------------------')
    print()


separator()


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# a[a<0].shape[0]
print('How many negative numbers are there:', a[a < 0].shape[0])

# 2. How many positive numbers are there?

# a[a>0].shape[0]
print('How many positive numbers are there:', a[a > 0].shape[0])

# 3. How many even positive numbers are there?

# a[(a>0) & (a%2 == 0)].shape[0]
print('How many even positive numbers are there:',
      a[(a > 0) & (a % 2 == 0)].shape[0])

# 4. If you were to add 3 to each data point, how many positive numbers would there be?

# a[(a+3)>0 & (a%2 == 0)].shape[0]
print('If you were to add 3 to each data point, how many positive numbers would there be:',
      a[(a+3) > 0 & (a % 2 == 0)].shape[0])

# 5. If you squared each number, what would the new mean and standard deviation be?

print('mean:', (a ** 2).mean(), '\n'
      'standard deviation:', (a ** 2).std())

# 6.  A common statistical operation on a dataset is centering. This means to adjust the data such that the center of the data is at 0. This is done by subtracting the mean from each data point. Center the data set.

a = a - np.mean(a)
print(a)

# 7. Calculate the z-score for each data point. Recall that the z-score is given by:
#
# Z = x − μ / σ

print((a - a.mean(axis=0))/a.std(axis=0))

separator()

# *Use python's built in functionality/operators to determine the following:

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

sum_of_a = 0
for i in a:
    sum_of_a += i

print('python:', sum_of_a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = a[0]
for i in a:
    if i < min_of_a:
        min_of_a = i

print('python:', min_of_a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max_of_a = a[0]
for i in a:
    if i > max_of_a:
        max_of_a = i

print('python:', max_of_a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = 0
for i in a:
    mean_of_a += i
mean_of_a = mean_of_a / len(a)

print('python:', mean_of_a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

product_of_a = 1
for n in a:
    product_of_a *= n

print('python:', product_of_a)

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

squares_of_a = []
for n in a:
    squares_of_a.append(n ** 2)

print('python:', squares_of_a)

squares_of_a = [n ** 2 for n in a]

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

odds_in_a = []
for n in a:
    if n % 2 != 0:
        odds_in_a.append(n)

print('python:', odds_in_a)

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = []
for n in a:
    if n % 2 == 0:
        evens_in_a.append(n)

print('python:', evens_in_a)

separator()

# What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...

# Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
# b = [
#     [3, 4, 5],
#     [6, 7, 8]
# ]

b = [[3, 4, 5], [6, 7, 8]]
b = np.array(b)

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable.
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**
#
# sum_of_b = 0
# 3for row in b:
#     sum_of_b += sum(row)

print('numpy:', np.sum(b))

# Exercise 2 - refactor the following to use numpy.
# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])

print('numpy:', np.min(b))

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

print('numpy:', np.max(b))

# Exercise 4 - refactor the following using numpy to find the mean of b
# mean_of_b = (sum(b[0]) + sum(b[1])) / (len([b[0]]) + len(b[1]))

print('numpy:', np.mean(b))

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
# product_of_b = 1
# for row in b:
#     for number in row:
#         product_of_b *= number

print('numpy:', np.prod(b))

# Exercise 6 - refactor the following to use numpy to find the list of squares
# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2)

print('numpy:', np.square(b))

# Exercise 7 - refactor using numpy to determine the odds_in_b
# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)

print('numpy:', b[b % 2 != 0])

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
# evens_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 == 0):
#             evens_in_b.append(number)

print('numpy:', b[b % 2 == 0])

# Exercise 9 - print out the shape of the array b.

print('numpy:', np.shape(b))

# Exercise 10 - transpose the array b.

print('numpy:', np.transpose(b))

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

print('numpy:', b.reshape(1, 6))

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

print('numpy:', b.reshape(6, 1))

separator()

# Setup 3
# c = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

c = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c = np.array(c)

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
#
# Exercise 1 - Find the min, max, sum, and product of c.

print('numpy:', c.min(), 'min')
print('numpy:', c.max(), 'max')
print('numpy:', c.sum(), 'sum')
print('numpy:', c.prod(), 'product')

# Exercise 2 - Determine the standard deviation of c.

print('numpy:', np.std(c))

# Exercise 3 - Determine the variance of c.

print('numpy:', np.var(c))

# Exercise 4 - Print out the shape of the array c

print('numpy:', np.shape(c))

# Exercise 5 - Transpose c and print out transposed result.

print('numpy:', np.transpose(c))

# Exercise 6 - Multiply c by the c-Transposed and print the result.

print('numpy:', c * np.transpose(c))

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed.
# Answer should be 261

print('numpy:', (c * np.transpose(c)).sum())

# Exercise 8 - Write the code necessary to determine the product of c times c transposed.
# Answer should be 131681894400.

print('numpy:', (c * np.transpose(c)).prod())

separator()

# Setup 4
# d = [
#     [90, 30, 45, 0, 120, 180],
#     [45, -90, -30, 270, 90, 0],
#     [60, 45, -45, 90, -45, 180]
# ]

d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d = np.array(d)

# Exercise 1 - Find the sine of all the numbers in d

print('numpy:', np.sin(d))

# Exercise 2 - Find the cosine of all the numbers in d

print('numpy:', np.cos(d))

# Exercise 3 - Find the tangent of all the numbers in d

print('numpy:', np.tan(d))

# Exercise 4 - Find all the negative numbers in d

print('numpy:', d[d < 0])

# Exercise 5 - Find all the positive numbers in d

print('numpy:', d[d > 0])

# Exercise 6 - Return an array of only the unique numbers in d.

print('numpy:', np.unique(d))

# Exercise 7 - Determine how many unique numbers there are in d.

print('numpy:', np.unique(d).sum())

# Exercise 8 - Print out the shape of d.

print('numpy:', np.shape(d))

# Exercise 9 - Transpose and then print out the shape of d.

print('numpy:', (np.transpose(d)).shape)

# Exercise 10 - Reshape d into an array of 9 x 2

print('numpy:', d.reshape(9, 2))
