### Multi-index and hierarchy ###
import numpy as np
import pandas as pd
from numpy.random import randn

# Construct multi-index frame
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])

print(df)
print("")

# Call data
print(df.loc['G1'])
print("")
print(df.loc['G1'].loc[1])
print("")