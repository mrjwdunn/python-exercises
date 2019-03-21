def separator():
    print()
    print('--------------------------------------------------')
    print()
# Thank you DD for the separator code!!!


separator()

# DONE
"""
1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
"""


def is_two(i):
    if i == 2 or i == '2':
        return True
    else:
        return False


print("is_two(2) == %s" % is_two(2))
print("is_two('2') == %s" % is_two('2'))
print("is_two(3) == %s" % is_two(3))
print("is_two('Ada') == %s" % is_two('Ada'))

separator()

# DONE
"""
2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
"""


def is_vowel(is_string):
    if is_string in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False


print("is_vowel('c') == %s" % is_vowel('c'))
print("is_vowel('o') == %s" % is_vowel('o'))
print("is_vowel('d') == %s" % is_vowel('d'))
print("is_vowel('e') == %s" % is_vowel('e'))
print("is_vowel('u') == %s" % is_vowel('u'))
print("is_vowel('p') == %s" % is_vowel('p'))

separator()

# DONE
"""
3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
"""


def is_consonant(is_string):
    if is_string in ['a', 'e', 'i', 'o', 'u']:
        return False
    else:
        return True


print("is_consonant('c') == %s" % is_consonant('c'))
print("is_consonant('o') == %s" % is_consonant('o'))
print("is_consonant('d') == %s" % is_consonant('d'))
print("is_consonant('e') == %s" % is_consonant('e'))
print("is_consonant('u') == %s" % is_consonant('u'))
print("is_consonant('p') == %s" % is_consonant('p'))

separator()

# DONE
"""
4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
"""


def capitalize(word):
    if is_consonant(word[0]):
        return word.capitalize()


print("capitalize('panama') == %s" % capitalize('panama'))
print("capitalize('codeup') == %s" % capitalize('codeup'))
print("capitalize('ada') == %s" % capitalize('ada'))
print("capitalize('jason') == %s" % capitalize('jason'))

separator()

# DONE
"""
5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
"""


def calculate_tip(bill, tip):
    return bill * tip


print('The bill was: $150')
print('I gave a 15% tip: ', (calculate_tip(150, .15)))
print('My total bill including tip was: $ ', 150 + calculate_tip(150, .15))
separator()

# DONE
"""
6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
"""


def apply_discount(price, discount):
    return price - (price * discount)


print('The price was: $ 150')
print('Store discount was 10%: ', 150 - apply_discount(150, .10))
print('My final bill including discount was: $', (apply_discount(150, .10)))

separator()

# DONE
"""
7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
"""


def handle_commas(string):
    string_without_commas = string.replace(',', '')
    return int(string_without_commas)


print("handle_commas('1,000,000') == %s" % handle_commas('1,000,000'))

separator()

# DONE
"""
8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
"""


def get_letter_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80 and grade <= 89:
        return 'B'
    elif grade >= 70 and grade <= 79:
        return 'C'
    elif grade >= 60 and grade <= 69:
        return 'D'
    elif grade <= 59:
        return 'F'


print("get_letter_grade(95) == %s" % get_letter_grade(95))
print("get_letter_grade(84) == %s" % get_letter_grade(84))
print("get_letter_grade(77) == %s" % get_letter_grade(77))
print("get_letter_grade(67) == %s" % get_letter_grade(67))
print("get_letter_grade(15) == %s" % get_letter_grade(15))

separator()

# DONE
"""
9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
"""


def remove_vowels(a_string):
    for vowel in 'aeiou':
        a_string = a_string.replace(vowel, '')
    return a_string


print("remove_vowels('panama') == %s" % remove_vowels('panama'))
print("remove_vowels('codeup') == %s" % remove_vowels('codeup'))
print("remove_vowels('ada') == %s" % remove_vowels('ada'))
print("remove_vowels('jason') == %s" % remove_vowels('jason'))

separator()

# GOT HELP
"""
10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
    ~ anything that is not a valid python identifier should be removed
    ~ leading and trailing whitespace should be removed
    ~ everything should be lowercase
    ~ spaces should be replaced with underscores
    ~ for example:
        ~ Name will become name
        ~ First Name will become first_name
        ~ % Completed will become completed
"""

LETTERS = ' _abcdefghijklmnopqrstuvwxyz0123456789'


def normalize_name(a_string):
    a_string = a_string.lower()
    valid_characters = []
    for character in a_string:
        if character in LETTERS:
            valid_characters.append(character)
    return ''.join(valid_characters).strip().replace(' ', '_')


print("normalize_name('Name') == {}".format(normalize_name('Name')))
print("normalize_name('First Name') == {}".format(normalize_name('First Name')))
print("normalize_name('% Completed') == {}".format(normalize_name('% Completed')))

separator()

# GOT HELP
"""
11. Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
    ~ cumsum([1, 1, 1]) returns [1, 2, 3]
    ~ cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]
"""


def cumsum(numbers):
    sums = [numbers[0]]
    for current_number in numbers[1:]:
        last_number = sums[-1]
        next_number = last_number + current_number
        sums.append(next_number)
    return sums


print("cumsum([1, 1, 1,]) == %s" % cumsum([1, 1, 1, ]))
print("cumsum([1, 2, 3,]) == %s" % cumsum([1, 2, 3, ]))
print("cumsum([1, 2, 3, 4]) == %s" % cumsum([1, 2, 3, 4]))
print("cumsum([1, -2, 1,]) == %s" % cumsum([1, -2, 1, ]))

separator()
