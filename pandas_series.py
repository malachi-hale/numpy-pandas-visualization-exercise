import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

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
print("capitalize A:")
print(fruits_pandas.str.replace('a', 'A'))
print("\n")

#3 
print("vowel counts:")
print(fruits_pandas[fruits_pandas.str.count(r'[aeiou]')])
print("\n")


#4 
print("highest length:")
max_length = fruits_pandas.str.len().max()
print(fruits_pandas[fruits_pandas.str.len() == max_length])
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
print(fruits_pandas[fruits_pandas.str.count(r'[aeiou]').max()])
print("\n")
