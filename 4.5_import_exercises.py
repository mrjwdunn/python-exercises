from itertools import permutations
from itertools import product
import itertools
import json


def separator():
    print()
    print('--------------------------------------------------')
    print()
# Thank you DD for the separator code!!!


separator()

# DONE
"""
import the module and refer to the function with the . syntax
"""
# import functions_exercises.is_vowel('a)
# print('This is the first one!')

separator()

# DONE
"""
use from to import the function directly
"""
# from functions_exercises import is_vowel
# print('This is the second one!')

separator()

# DONE
"""
use from and give the function a different name
"""
# from functions_exercises import is_vowel as vowel
# print('This is the third one!')

separator()


# DONE
"""
How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
"""
# import itertools
# from itertools import product

result = itertools.product('abc', '123')

for item in result:
    print(list(item))

separator()

# DONE
"""
How many different ways can you combine two of the letters from "abcd"?
"""
# import itertools
# from itertools import permutations

result = itertools.permutations('abcd', 2)

for item in result:
    print(list(item))

separator()

# DONE
"""
Total number of users == 19
"""
# from json

data = json.load(open('profiles.json'))

number_of_users = []

for user in data:
    number_of_users.append(user['isActive'])

print('Total number of users:', (len(number_of_users)))

separator()

# DONE
"""
Number of active users == 9
"""
active_users = []

for user in data:
    if user['isActive'] == True:
        active_users.append(user['isActive'])

print('Number of active users:', (len(active_users)))

separator()

# DONE
"""
Number of inactive users == 10
"""
inactive_users = []

for user in data:
    if user['isActive'] == False:
        inactive_users.append(user['isActive'])

print('Number of inactive users:', (len(inactive_users)))

separator()

# DONE
"""
Grand total of balances for all users == $52,667.02
"""
total_balances = sum([float(profile['balance'].replace(
    '$', '').replace(',', '')) for profile in data])
print('Grand total of balance for all users: ${}'.format(total_balances))

separator()

# DONE
"""
Average balance per user == $2,771.95
"""
average_balances = [profile['balance'] for profile in data]
print("Average balace per user: ${}".format(
    round(total_balances/len(average_balances), 2)))

separator()

# DONE
"""
User with the lowest balance == Avery Flynn
"""
lowest_balance = []

for user in data:
    lowest_balance.append(user['balance'])

for user in data:
    if user['balance'] == min(lowest_balance):
        print('User with highest balance:', (user['name']))

separator()

# DONE
"""
User with the highest balance == Fay Hammond
"""
highest_balance = []

for user in data:
    highest_balance.append(user['balance'])

for user in data:
    if user['balance'] == max(highest_balance):
        print('User with highest balance:', (user['name']))

separator()

# DONE
"""
Most common favorite fruit == strawberry
"""
favorite_fruit = []

for user in data:
    favorite_fruit.append(user['favoriteFruit'])

print('Most common favorite fruit:', (max(favorite_fruit)))

separator()

# DONE
"""
Least most common favorite fruit == apple
"""
least_favorite_fruit = []

for user in data:
    least_favorite_fruit.append(user['favoriteFruit'])

print('Least most common favorite fruit:',
      (min(least_favorite_fruit)))

separator()

# WRONG
"""
Total number of unread messages for all users == 210
"""
unread_messages = []

for user in data:
    unread_messages.append(user['greeting'])

print('Total number of unread messages for all users:',
      (min(unread_messages)))

separator()
