# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
def upper_case(fruits):
    for i in range(len(fruits)):
         fruits[i] = fruits[i].upper()
    return fruits
print(upper_case(fruits))
# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
def capitalized_fruits(fruits):
    for i in range(len(fruits)):
         fruits[i] = fruits[i].title()
    return fruits
print(capitalized_fruits(fruits))
# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
def fruits_with_more_than_two_vowels(fruits):
    two_vowels_or_more = []
    for i in range(len(fruits)):
        if fruits[i].count('a') + fruits[i].count('e') + fruits[i].count('i') + fruits[i].count('o') + fruits[i].count('u') > 2:
            two_vowels_or_more.append(fruits[i])
    return two_vowels_or_more
print(fruits_with_more_than_two_vowels(fruits))
# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
def fruits_with_only_two_vowels(fruits):
    only_two_vowels = []
    for i in range(len(fruits)):
        if fruits[i].count('a') + fruits[i].count('e') + fruits[i].count('i') + fruits[i].count('o') + fruits[i].count('u') == 2:
            only_two_vowels.append(fruits[i])
    return only_two_vowels
print(fruits_with_only_two_vowels(fruits))

# Exercise 5 - make a list that contains each fruit with more than 5 characters
def fruits_with_more_than_five_characters(fruits):
    more_than_five_characters = []
    for i in range(len(fruits)):
        if len(fruits[i]) > 5:
            more_than_five_characters.append(fruits[i])
    return more_than_five_characters
print(fruits_with_more_than_five_characters(fruits))

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
def fruits_with_exactly_five_characters(fruits):
    exactly_five_characters = []
    for i in range(len(fruits)):
        if len(fruits[i]) == 5:
            exactly_five_characters.append(fruits[i])
    return exactly_five_characters
print(fruits_with_exactly_five_characters(fruits))
# Exercise 7 - Make a list that contains fruits that have less than 5 characters
def fruits_with_less_than_five_characters(fruits):
    less_than_five_characters = []
    for i in range(len(fruits)):
        if len(fruits[i]) < 5:
            less_than_five_characters.append(fruits[i])
    return less_than_five_characters
print(fruits_with_less_than_five_characters(fruits))

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
def number_of_characters_in_each_fruits(fruits):
    number_of_characters = []
    for i in range(len(fruits)):
        number_of_characters.append(len(fruits[i]))
    return number_of_characters
print(number_of_characters_in_each_fruits(fruits))
# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
def fruits_with_letter_a(fruits):
    fruits_with_a = []
    for i in range(len(fruits)):
        if 'a' in fruits[i].lower():
            fruits_with_a.append(fruits[i])
    return fruits_with_a
print(fruits_with_letter_a(fruits))

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
def even_numbers(numbers):
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens
print(even_numbers(numbers))

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
def odd_numbers(numbers):
    odds = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens
print(even_numbers(numbers))

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
def positive_numbers(numbers):
    positives = []
    for number in numbers:
        if number > 0:
            positives.append(number)
    return positives
print(positive_numbers(numbers))
# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
def negative_numbers(numbers):
    negatives = []
    for number in numbers:
        if number < 0:
            negatives.append(number)
    return negatives
print(negative_numbers(numbers))
# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
def two_or_more_numerals(numbers):
    two_or_more = []
    for number in numbers:
        if len(abs(number)) >= 2:
            two_or_more.append(number)
    return two_or_more
print(two_or_more_numerals(numbers))
# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
def numbers_squared(numbers):
    squared = []
    for number in numbers:
        number_squared = number ** 2
        squared.append(number_squared)
    return squared
print(numbers_squared(numbers))
# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
