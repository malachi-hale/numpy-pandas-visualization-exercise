import pandas as pd
import numpy as np
from pydataset import data

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})
print(df)

#1a
df['passing_english'] = df.english >= 70
print(df)

#1b
#Duplicates are handles simply by grouping the rows together by True or False
print(df.sort_values(by='passing_english', ascending=False))

#1c
print(df.sort_values(["passing_english", "name"], ascending = (True, True)))

#1d 
print(df.sort_values(["passing_english", "english"], ascending = (True, True)))

#1e 
df['overall grade'] = (df.english + df.math + df.reading)/3
print(df)

#2a
mpg = data('mpg')
print(mpg.shape)
#There are 234 rows and 11 columns. 

#2b
print(mpg.dtypes)

#2c 
print("Info:\n", mpg.info())
print("Describe:\n", mpg.describe())

#2d 
mpg.rename(columns = {'cty':'city'}, inplace = True)
print(mpg.columns)


#2e 
mpg.rename(columns = {'hwy':'highway'}, inplace = True)
print(mpg.columns)

#2f
print(mpg[mpg['city'] > mpg['highway']].size)
#The result is 0, so no cars have better city mileage than highway mileage.

#2g
mpg['mileage difference'] = mpg['highway'] - mpg['city']
print(mpg)

#2h 
print("The cars with the maximum mileage difference are:\n", mpg[['year', 'manufacturer', 'model', 'mileage difference']][mpg['mileage difference'] == mpg['mileage difference'].max()])

#2i 
compact_cars = mpg[mpg['class'] == 'compact']
print("The compact car with the lowest highway mileage is: \n", compact_cars[['year', 'manufacturer', 'model', 'highway']][compact_cars['highway'] == compact_cars['highway'].max()])

#2j 
mpg['average mileage'] = (mpg['highway'] + mpg['city'])/2
print(mpg)

#2k 
dodge = mpg[mpg['manufacturer'] == 'dodge']
print("The dodge car with the best average mileage is:\n", dodge[['year', 'manufacturer', 'model', 'average mileage']][dodge['average mileage'] == dodge['average mileage'].max()])
print("The dodge car with the worst average mileage is:\n", dodge[['year', 'manufacturer', 'model', 'average mileage']][dodge['average mileage'] == dodge['average mileage'].min()])

#3
mammals = data('Mammals')
print(mammals)

#3a
print("The shape of the dataframe is:", mammals.shape)

#3b 
print("The data types are:\n", mammals.dtypes)

#3c
print("Info:\n", mammals.info())
print("Describe:\n", mammals.describe())

#3d
print("The weight of the fastest animal is:\n", mammals[['weight']][mammals['speed'] == mammals['speed'].max()])

#3e
specials = mammals[mammals['specials']]
percent_special = ((specials.size)/(mammals.size))*100
rounded_percent_special = str(round(percent_special, 2))
print("There are", rounded_percent_special, "percent special animals")

#3f 
fast_animals = mammals[mammals['speed'] > mammals['speed'].median()]
fast_hoppers = fast_animals[fast_animals['hoppers']]
hoppers = mammals[mammals['hoppers']]
percent_fast_hoppers_of_total = ((fast_hoppers.size)/mammals.size)*100
rounded_percent_fast_hoppers_of_total = str(round(percent_fast_hoppers_of_total, 2))
percent_fast_hoppers_of_hoppers = ((fast_hoppers.size)/hoppers.size)*100
rounded_percent_fast_hoppers_of_hoppers = str(round(percent_fast_hoppers_of_hoppers, 2))

print("There are", fast_hoppers.size, "hoppers with a speed faster than the median speed.")
print("This means", rounded_percent_fast_hoppers_of_total, "percent of the total mammals are fast hoppers, and", rounded_percent_fast_hoppers_of_hoppers, "percent of total hoppers are fast hoppers.")