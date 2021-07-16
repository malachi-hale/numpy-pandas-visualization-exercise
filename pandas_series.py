import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pandas.core.algorithms import value_counts

fruits =     ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
fruits_pandas = pd.Series(fruits)
print(fruits_pandas)
#1
print(fruits_pandas.size)
#2
print(fruits_pandas.index.tolist())
#3
print(fruits_pandas.values)
#4
print(fruits_pandas.dtypes)
#5
print(fruits_pandas.head(5))
print(fruits_pandas.tail(3))
print(fruits_pandas.sample(2))
#6
print(fruits_pandas.describe())
#7
fruit_values = fruits_pandas.head() 
print(fruits_pandas.head().unique())
#8
print(fruits_pandas.value_counts())
#9
print("The largest values are", fruits_pandas.value_counts().nlargest(n = 1, keep = "all"))
#10
print("The smallest values are", fruits_pandas.value_counts().nsmallest(n = 1, keep = "all"))
##Part 2
print("\n")
#1
print("Capitalize everything ")
print(fruits_pandas.str.capitalize())
print("\n")

#2
print("count A:")
print(fruits_pandas.str.count('a'))
print("\n")

#3 
print("vowel counts:")
print(fruits_pandas.str.count('[aeiou]'))
print("\n")


#4 
print("highest length:")
max_length = fruits_pandas.str.len().max()
print("The longest string is: ", fruits_pandas.values[fruits_pandas.str.len() == max_length], "The length is: ", max_length)
print("\n")


#5
print("length greater than 5:")
length_of_fruits = fruits_pandas.str.len()
print(fruits_pandas[length_of_fruits >= 5])
print("\n")

#6
print("two or more o's:")
print(fruits_pandas[fruits_pandas.apply(lambda x: x.count('o') >= 2)])
print("\n")


#7
print("contains berry:")
print(fruits_pandas[fruits_pandas.apply(lambda x: "berry" in x)])
print("\n")


#8
print("contains apple:")
print(fruits_pandas[fruits_pandas.apply(lambda x: "apple" in x)])
print("\n")


#9
print("greatest number of vowels:")
print(fruits_pandas[fruits_pandas.str.count('[aeiou]').max()])
print("\n")

#Part 3
#1
letters_string = 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
letters_list = list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')
letters = pd.Series(letters_list)
print("The most frequent letter is:", letters.value_counts().nlargest(n = 1, keep = "all"))

#2
print("The least frequent letter is:", letters.value_counts().nsmallest(n = 1, keep = "all"))

#3
print("There are", sum(letters.str.count('[aeiou]')), "total vowels")

#4 
print("There are", sum(letters.str.count('[bcdfghjklmnpqrstvwxyz]')), "total consonants")

#5
print(letters.str.upper())

#6
pd.Series(letters).value_counts().nlargest(n =5, keep = "all").plot.bar(color='firebrick', width=.9)
plt.title('Letter Frequency')
plt.xticks(rotation=0)
plt.xlabel('Letter')
plt.ylabel('Frequency')

plt.show()

#1
numbers = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])
print(numbers.dtype)

#2
print("There are", len(numbers), "elements in this data series.")

#3
no_dollar_sign = numbers.str.replace("$", "")
clean_numbers = no_dollar_sign.str.replace(",", "")
numbers_numeric = pd.to_numeric(clean_numbers)

#4
print("The maximum value of numbers is", max(numbers_numeric))

#5
print("The minimum value of numbers is", min(numbers_numeric))

#6
print("The range of values in the series is:", max(numbers_numeric)-min(numbers_numeric))

#7
cut_numbers = pd.cut(numbers_numeric, 4)
print(cut_numbers)

#8
pd.Series(cut_numbers).value_counts().plot.bar(color='firebrick', width=.9)
plt.title('Values in each Range')
plt.xticks(rotation=0)
plt.xlabel('Range')
plt.ylabel('Values in range')

plt.show()


exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

#1
print("There are", len(exam_scores), "elements in exam scores.")

#2
print("Mean:", exam_scores.mean(), "\n Median:", exam_scores.median(), "\n Minimum:", exam_scores.min(), "\n Maximum:", exam_scores.max())

#3
grades = pd.cut(exam_scores, [60, 70, 80, 90, 100])

pd.Series(grades).value_counts().plot.bar(color='firebrick', width=.9)
plt.title('Grade Ranges')
plt.xticks(rotation=0)
plt.xlabel('Grade Range')
plt.ylabel('Number of Students in that Grade Range')

plt.show()

#4
curved_grades = exam_scores + 4
print("Curved exam scores:", curved_grades)

#5
def convert_to_letter_grade(n):
    if n <= 100 and n >= 90: 
        return 'A'
    elif n <= 89 and n >= 80: 
        return 'B' 
    elif n <= 79 and n >= 70: 
        return 'C' 
    elif  n <= 69 and n >= 60: 
        return 'D' 
    else:
         return 'F'
letter_grades = curved_grades.apply(convert_to_letter_grade)
print(letter_grades)

#6
pd.Series(letter_grades).value_counts().loc[['A', 'B', 'C', 'D']].plot.bar(color='firebrick', width=.9)
plt.title('Student Grades')
plt.xticks(rotation=0)
plt.xlabel('Grade')
plt.ylabel('Number of Students')

plt.show()