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
print(mpg.info)
print(mpg.describe)

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
mpg['mileage difference']