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

