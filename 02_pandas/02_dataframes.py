import numpy as np
import pandas as pd

from numpy.random import randn

# declaring a random seed number
np.random.seed(101)

df = pd.DataFrame(data=randn(5, 4), index=[
                  'A', 'B', 'C', 'D', 'E'], columns=['W', 'X', 'Y', 'Z'])

print(df)
print("")

# DataFrame is a bunch of series

# Can access to data with column name, for example:
print(df['W'])
print("")

# Multiple column names is also available:
print(df[['W', 'Z']])
print("")

# Create a new column named 'new' by adding two existing columns:
df['new'] = df['W'] + df['Y']
print(df['new'])
print("")

# Can drop a column
df.drop('new', axis=1, inplace=True)
print(df)
print("")

# and also a row
df.drop('E')
print(df)
print("")

# Selecting rows by
print(df.loc['A'])
# or
print(df.iloc[2])
print("")

# Return a subset of the dataframe by
print(df.loc[['A', 'B'], ['W', 'Y']])
print("")
