import numpy as np
import pandas as pd

# Can create dataframe as dictionary as well
# keys will be the columns in the dataframe
# values are the datapoints of each column
d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}

df = pd.DataFrame(d)
print(df)
print("")

# dropna() method will drop any rows that have null value in it
print(df.dropna())
print("")

# Passing axis=1 will make dropna() method drops columns instead of rows
print(df.dropna(axis=1))
print("")

# Can set the number of NaN values to drop by using thresh parameter
print(df.dropna(thresh=2))
# This will drop rows that have 2 or more NaN values only
print("") 

# Can replace all NaN (missing values) with fillna() method
print(df.fillna(value="FILL VALUE"))
print("")

# Can pick one specific NaN in the dataframe and replace it by
print(df['A'].fillna(value=df['A'].mean()))
print("")