# 1. Import NumPy as np
import numpy as np

# 2. Create an array of 10 zeros
zeros = np.zeros(10)
print("2:", zeros)

# 3. Create an array of 10 ones
ones = np.ones(10)
print("3:", ones)

# 4. Create an array of 10 fives
fives = np.ones(10) * 5
print("4:", fives)

# 5. Create an array of the integers from 10 to 50
ten_to_fifty = np.arange(10, 50)
print("5:", ten_to_fifty)

# 6. Create an array of all the even integers from 10 to 50
ttf_even = np.arange(10, 50, 2)
print("6:", ttf_even)

# 7. Create a 3x3 matrix with values ranging from 0 to 8
tbt = np.arange(9).reshape(3, 3)
print("7:", tbt)

# 8. Create a 3x3 identity matrix
identity_mat = np.eye(3)
print("8:", identity_mat)

# 9. Use NumPy to generate a random number between 0 and 1
rand_num = np.random.rand(1)
print("9:", rand_num)

# 10. Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
rand_samp = np.random.randn(25)
print("10:", rand_samp)
