def separator():
    print()
    print('--------------------------------------------------')
    print()
# Thank you DD for the separator code!!!


separator()

print('---Conditional Basics---')
print(' ')

print('---problem 1(a)---')
# DONE
"""
a. prompt the user for a day of the week, print out whether the day is Monday or not
"""
print(' ')

weekday = input('Please enter a day of the week: ')
if weekday == 'Monday':
    print('That is correct, today is Monday.')
else:
    print('That is correct, today is NOT Monday.')
print('All day')

separator()

print('---problem 1(b)---')
# DONE
"""
b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
"""
print(' ')

weekday = input('Please enter a day of the week: ')
if weekday == 'Monday':
    print('Yes, today is Monday')
elif weekday == 'Saturday' or weekday == 'Sunday':
    print('It is a weekend')
else:
    print('It is a weekday')
print('All day')

separator()

print('---problem 1(c)---')
# DONE
"""
c. create variables and make up values for
    ~ the number of hours worked in one week
    ~ the hourly rate
    ~ how much the week's paycheck will be
    ~ write the python code that calculates the weekly paycheck
    ~ you get paid time and a half if you work more than 40 hours
"""
print(' ')

hours_worked = 45
hourly_rate = 100
if hours_worked > 40:
    pay_at_regular_rate = 40 * hourly_rate
    overtime_pay = (hours_worked - 40) * hourly_rate * 1.5
    paycheck = pay_at_regular_rate + overtime_pay
else:
    paycheck = hourly_rate * hours_worked
print('$', pay_at_regular_rate, '= Regular Pay')
print('$', overtime_pay, '= Overtime Pay')
print('$', paycheck, '= Total Pay Check')
print(' ')

separator()

print('---Loop Basics---')
print()
print('---While---')

print(' ')
print('---problem 2a(1)---')
# DONE
"""
Create an integer variable i with a value of 5.
    ~ Create a while loop that runs so long as i is less than or equal to 15
    ~ Each loop iteration, output the current value of i, then increment i by one.
    ~ Your output should look like this:
"""
print()

num = 5
while num <= 15:
    print(num)
    num += 1

separator()

print('---problem 2a(2)---')
# DONE
"""
Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
"""
print()

num = 0
while num <= 100:
    print(num)
    num += 2

separator()

print('---problem 2a(3)---')
# DONE
"""
Alter your loop to count backwards by 5's from 100 to -10.
"""
print(' ')

num = 100
while num >= -10:
    print(num)
    num -= 5

separator()

print('---problem 2a(4)---')
# DONE
"""
Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
"""
print(' ')

num = 2
while num <= 1000000:
    print(num)
    num *= num

separator()

print('---problem 2a(5)---')
# DONE
"""
Write a loop that uses print to create the output shown below.
"""
print(' ')

num = 100
while num >= 5:
    print(num)
    num -= 5

separator()

print('---Loops---')
print(' ')
print('---problem 2b(i)---')
"""
Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
"""
print(' ')

user_number = int(input("Enter a number to multiplication by: "))

for num in range(1, 11):
    print(user_number, 'x', num, '=', user_number * num)

"""
Zach's
x = int(input('Please enter a number: '))

x = 7
for n in range (1,11):
    output = '{} x {} = {}'.format(x, n, x * n)
    print(output)
"""
separator()

print('---problem 2b(ii)---')
# DONE
"""
Create a for loop that uses print to create the output shown below.
"""
for num in range(1, 10):
    print(str(num) * num)

separator()

print('---Break and Continue---')
print(' ')

print('---problem 2c(i)---')
# DONE
"""
Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
"""
print(' ')

print('Number to skip is: 27')
print(' ')

for num in range(1, 50):
    if num % 2 == 0:
        continue
    elif num == 27:
        print('Yikes! Skipping number: 27')
        continue
    print('Here is an odd number: {}'.format(num))

separator()
"""
Zach's
while True:
    number_to_skip = input('Enter an odd number (1-50): ')
    if number_to_skip.isdigit() and 1 <= int(number_to_skip) in range(1, 50) and int(number_to_skip)% 2 == 1:
        break
for n in range(1, 51):
    if n % 2 == 0:
        continue
    if n == number_to_skip:
        print(f'Yikes! Skipping number {n}')
    else:
        print(f'Here is an odd number: {n}')
"""


print('---problem 2c(ii)---')
# DONE
"""
    The input function can be used to prompt for input and use that input in your python code.

    Prompt the user to enter a positive number and write a loop that counts from 0 to that number.

    (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)
"""
print(' ')

user_number = int(input('Enter a number: '))
for num in range(0, user_number + 1):
    print(num)
    num += 1

print('---problem 2c(iii)---')
# DONE
""" Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.
"""
print(' ')

user_number = int(input('Enter a number: '))
for n in range(user_number, 0, -1):
    print(n)

separator()

print('---Fizzbuzz---')
print(' ')
print('---problem 2c(i)---')
# DONE
"""
One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

Write a program that prints the numbers from 1 to 100.

For multiples of three print "Fizz" instead of the number

For the multiples of five print "Buzz".

For numbers which are multiples of both three and five print "FizzBuzz".
"""
for num in range(1, 101):
    if num % 3 == 0:
        print('Fizz')
    if num % 5 == 0:
        print('Buzz')
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    if num % 3 != 0 and num % 5 != 0:
        print(num)

separator()

print('---Display a table of powers---')
print(' ')

# Zach's
upper_bound = int(input('Enter a number: '))
n = 1

print('number | squared | cubed')
print('------ | ------- | -----')
for n in range(1, upper_bound + 1):
    # right-aligned(default)
    print('{:6} | {:7} | {:5}'.format(n, n ** 2, n ** 3))
    # left-aligned
    # print('{:<6} | {:<7} | {:<5}'.format(n, n ** 2, n ** 3))
    # center-aligned
    # print('{:^6} | {:^7} | {:^5}'.format(n, n ** 2, n ** 3))

separator()

print('---BONUS---')
print(' ')
# DONE
"""
Convert given number grades into letter grades.

Prompt the user for a numerical grade from 0 to 100.

Display the corresponding letter grade.

Prompt the user to continue.

Assume that the user will enter valid integers for the grades.

The application should only continue if the user agrees to.

Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).
"""

user_wants_to_continue = 'yes'

while user_wants_to_continue == 'yes':
    grade = int(input('Enter your number grade: '))

    if grade >= 99:
        letter_grade = 'A+'
    elif grade >= 90 and grade <= 98:
        letter_grade = 'A'
    elif grade >= 80 and grade <= 89:
        letter_grade = 'B'
    elif grade >= 70 and grade <= 79:
        letter_grade = 'C'
    elif grade >= 60 and grade <= 69:
        letter_grade = 'D'
    elif grade < 60:
        letter_grade = 'F'
    print('Your letter grade is: ' + letter_grade)
    print()

    user_wants_to_continue = input('Do you want to continue? ')
    user_continues = 'yes'

separator()

print('---BONUS---')
print(' ')
# DONE
"""
Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
"""

books = [
    {
        'title': 'The Path Between the Seas',
        'author': 'David McCullough',
        'genre': 'Travel'
    },
    {
        'title': 'Erased: The Untold Story of the Panama Canal',
        'author': 'Marixa Lasso',
        'genre': 'Travel'
    },
    {
        'title': 'Keto Diet: Your 30-Day Plan to Lose Weight, Balance Hormones, Boost Brain Health, and Reverse Disease',
        'author': 'Josh Axe',
        'genre': 'Diet'
    },
    {
        'title': 'Mindful Eating',
        'author': 'Jan Chozen Bays, MD',
        'genre': 'Diet'
    },
    {
        'title': 'Beginner Html 5 & CSS 3',
        'author': 'Swapnil Raja',
        'genre': 'Coding'
    },
    {
        'title': 'HTML & CSS, design and bulid websites',
        'author': 'Jon Duckett',
        'genre': 'Coding'
    },
    {
        'title': 'JAVASCRIPT & JQUERY, interactive front-end web development',
        'author': 'Josh Axe',
        'genre': 'Coding'
    },
]

for book in books:
    print('---------------')
    print(book['title'])
    print(book['author'])
    print(book['genre'])

separator()
# DONE
"""
Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre
"""
books = [
    {
        'title': 'The Path Between the Seas',
        'author': 'David McCullough',
        'genre': 'Travel'
    },
    {
        'title': 'Erased: The Untold Story of the Panama Canal',
        'author': 'Marixa Lasso',
        'genre': 'Travel'
    },
    {
        'title': 'Keto Diet: Your 30-Day Plan to Lose Weight, Balance Hormones, Boost Brain Health, and Reverse Disease',
        'author': 'Josh Axe',
        'genre': 'Diet'
    },
    {
        'title': 'Mindful Eating',
        'author': 'Jan Chozen Bays, MD',
        'genre': 'Diet'
    },
    {
        'title': 'Beginner Html 5 & CSS 3',
        'author': 'Swapnil Raja',
        'genre': 'Coding'
    },
    {
        'title': 'HTML & CSS, design and bulid websites',
        'author': 'Jon Duckett',
        'genre': 'Coding'
    },
    {
        'title': 'JAVASCRIPT & JQUERY, interactive front-end web development',
        'author': 'Josh Axe',
        'genre': 'Coding'
    },
]

genre_picked = input('Genre the user picked: ')

for book in books:
    if book['genre'] == genre_picked:
        print(book['title'])
        print(book['author'])
        print(book['genre'])

separator()
