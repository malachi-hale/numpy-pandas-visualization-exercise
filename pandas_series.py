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
#1
print(fruits_pandas.str.capitalize())
#2
print(fruits_pandas.str.replace('a', 'A'))
#3 
vowels = 'aeiou'
print(fruit.count(vowels) for fruit in fruits_pandas.values)