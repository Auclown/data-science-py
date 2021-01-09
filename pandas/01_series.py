import numpy as np
import pandas as pd

# Pandas' series can access by label
labels = ["a", "b", "c"]
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {"a": 10, "b": 20, "c": 30}

print(pd.Series(data=my_data))
print("=====================")
print(pd.Series(data=my_data, index=labels))
# print("is equivalent to")
print(pd.Series(d))

print("=====================")
# Another way to make a seires:
series2 = pd.Series([1, 2, 5, 4], ["USA", "Germany", "Italy", "Japan"])
print(series2)

# Can grab data of a series by
print(series2["USA"])
