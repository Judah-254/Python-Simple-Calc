import numpy as np

# 1. Create an array with numbers from 10 to 50
arr = np.arange(10, 51)

# 2. Find the maximum and minimum values
max_val = np.max(arr)
min_val = np.min(arr)

# 3. Multiply all elements by 3
multiplied_arr = arr * 3

# Display results
print("Original array:", arr)
print("Maximum value:", max_val)
print("Minimum value:", min_val)
print("Array after multiplying by 3:", multiplied_arr)
