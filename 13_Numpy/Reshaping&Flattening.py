import numpy as np
arr = np.arange(0, 9)
reshaped = arr.reshape(3 , 3)
flattened = reshaped.flatten()

print(arr)
print()
print(reshaped)
print()
print(flattened)