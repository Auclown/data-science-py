# Can use pandas to read CSV, SQL, HTML and Excel files.
from sqlalchemy import create_engine
import pandas as pd


############### CSV Files ################
# read_csv() reads a csv file
print(pd.read_csv('example.csv'))
print("")

# Can assign csv to a variable with read_csv() method:
df = pd.read_csv('example.csv')
print(df)
print("")

# Can create a csv file out of a dataframe by using to_csv() method:
df.to_csv('my_output.csv', index=False)
# This will create "my_output.csv" file in current directory


################ Excel Files ############
# read_excel() reads an excel file
# Can use sheetname parameter to read a specific sheet from the excel file
print(pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet1'))
print("")

# to_excel() creates an excel file out of a dataframe
# Can also specify the sheet name if want
df.to_excel('Excel_Sample2.xlsx', sheet_name='NewSheet')


################ HTML input ################
# Can read html
data = pd.read_html(
    'https://www.fdic.gov/bank/individual/failed/banklist.html')
print(data[0].head)
print("")
