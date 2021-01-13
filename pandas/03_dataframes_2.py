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
