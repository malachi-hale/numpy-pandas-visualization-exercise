import pandas as pd
import numpy as np
from pydataset import data

np.random.seed(123)

#3
from env import host, user, password
def get_db_url(host, user, password, database):
    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    return url

#4
employees_url = get_db_url(host, user, password, "employees")
print(employees_url)

#5
sql = '''
SELECT
    emp_no,
    first_name,
    last_name
FROM employees
WHERE gender = 'F'
LIMIT 100
'''
employees_female = pd.read_sql(sql, employees_url)
print(employees_female.head())



##Intentionally making a typo in the database name
#employees_female = pd.read_sql(sql, employee_url)
#print(employees_female.head())
##Returns the error unable to recognize the employee_url

#Intentionally making a typo for the sql query 
#sql = '''
#SELECT
    #emp_no,
    #first_name,
    #last_name
#FROM employee
#WHERE gender = 'F'
#LIMIT 100
#'''
#employees_female = pd.read_sql(sql, employees_url)
#print(employees_female.head())
##Returns the error programming error

#6
sql1 = '''
SHOW TABLES 
'''
tables = pd.read_sql(sql1, employees_url)
print(tables)

sql1 = '''
SELECT * 
FROM employees
'''
employees = pd.read_sql(sql1, employees_url)
sql2 = '''
SELECT * 
FROM titles
'''
titles = pd.read_sql(sql2, employees_url)

#7
print("The employees table has", employees.shape[0], "rows and", employees.shape[1], "columns. The titles table has", titles.shape[0], "rows and", titles.shape[1], "columns.")
#Yes this is the result that I would have expected. 

#8
print("The summary statistics for the employees tables is: \n", employees.info(), employees.describe(), "\n The summary statistics for the titles table is: \n", titles.info(), titles.describe())

#9
titles_columns = '''
DESCRIBE titles
'''
employees_columns = '''
DESCRIBE employees
'''

print(pd.read_sql(titles_columns, employees_url))

print(pd.read_sql(employees_columns, employees_url))

unique_titles = '''
SELECT DISTINCT title
FROM titles
'''
unique = pd.read_sql(unique_titles, employees_url)
print(unique)
print("There are", unique.size, "unique titles in the titles table.")

#10
oldest_to_date = '''
SELECT to_date
FROM titles 
ORDER BY to_date ASC
LIMIT 1
'''
oldest = pd.read_sql(oldest_to_date, employees_url)
print("The oldest date in the to_date column is", oldest)

#11
newest_to_date = '''
SELECT to_date
FROM titles 
WHERE to_date != '9999-01-01'
ORDER BY to_date DESC
LIMIT 1
'''
all_dates = pd.read_sql(newest_to_date, employees_url)
print(all_dates)