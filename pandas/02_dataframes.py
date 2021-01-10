import numpy as np
import pandas as pd

from numpy.random import randn

# declaring a random seed number
np.random.seed(101)

df = pd.DataFrame(data=randn(5, 4), index=[
                  'A', 'B', 'C', 'D', 'E'], columns=['W', 'X', 'Y', 'Z'])

print(df)