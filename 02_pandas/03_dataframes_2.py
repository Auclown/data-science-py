import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)
df = pd.DataFrame(data=randn(5, 4), index=[
                  'A', 'B', 'C', 'D', 'E'], columns=['W', 'X', 'Y', 'Z'])

# Conditional selection
booldf = df > 0
print(df[booldf])
print("")

# Select rows that are greater than 0 fromn column W
print(df['W'] > 0)
print("")
# the line above will only show True or False of each row depending on it satisfies the condition
# To print the values of rows that satisfy the condition:
print(df[df['W'] > 0])
print("")

# Multiple conditions:
print(df[(df['W'] > 0) | (df['Y'] > 1)])
print("")

# Reset index back to the default:
df.reset_index()

# Create a column called States, and giving it some values
newind = 'CA NY WY OR CO'.split()
df["States"] = newind
print(df)
print("")

# Can convert column to the index
print(df.set_index("States"))
print("")