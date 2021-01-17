# groupby allows you to group together rows based off of a column and perform
# an aggregate function on them.
import numpy as np
import pandas as pd

data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]
        }

df = pd.DataFrame(data)

by_comp = df.groupby('Company')
# Can call aggregate functions
print(by_comp.mean())
print("")

print(by_comp.sum())
print("")

print(by_comp.sum().loc['FB'])
print("")

# Can call all the lines above in one single line
print(df.groupby('Company').sum().loc['FB'])
print("")

# describe() method gives a bunch of useful information
print(by_comp.describe())
