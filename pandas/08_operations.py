import numpy as np
import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [
                  444, 555, 666, 444], 'col3': ['abc', 'def', 'ghi', 'xyz']})

df.head()

# To find unique value in a column, use unique() method
print(df['col2'].unique())
print("")

# Number of unique values, use nunique()
print(df['col2'].nunique())
print("")

# value_counts() method is used to get how many times each unique value is shown
print(df['col2'].value_counts())
print("")


def times2(x):
    return x * 2


# apply() method allows you to use custom functions on Dataframes
print(df['col1'].apply(times2))
print("")

# and also built-in functions.
print(df['col3'].apply(len))
print("")

# lambda expression
print(df['col2'].apply(lambda x: x * 2))
print("")

# Can remove column by using drop() method
# print(df.drop('col1', axis=1))

# sort_values() method allows you to sort the DataFrame
print(df.sort_values(by='col2'))
print("")

# isnull() method allows you to see which value of the DataFrame is null
# returns False if the value is not null
print(df.isnull())
print("")

# pivot_table() method creates a pivot table which is a multi-index table
data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'two', 'two', 'one', 'one'],
        'C': ['x', 'y', 'x', 'y', 'x', 'y'],
        'D': [1, 3, 2, 5, 4, 1]}

df = pd.DataFrame(data)
# print(df)
# values parameter: indicates values of a specific column
# index parameter: makes specific columns into multi-level index
# columns parameter:
print(df.pivot_table(values='D', index=['A', 'B'], columns='C'))
