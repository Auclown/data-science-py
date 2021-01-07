import numpy as np

my_list = [1, 2, 3]
arr = np.array(my_list)

# print(arr)

my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(np.array(my_mat))

# print(np.arange(0, 11))
# print(np.arange(0, 11, 2))

# print(np.linspace(0, 5, 100))

ranarr = np.random.randint(0, 50, 10)

print(ranarr)
print(ranarr.max())
print(ranarr.argmax())
print(ranarr.min())
print(ranarr.argmin())
