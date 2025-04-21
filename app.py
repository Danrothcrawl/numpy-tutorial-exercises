import numpy as np

print(np.__version__)
print(np.show_config())
print(np.zeros(10))
zeros = np.zeros(10)
mem_size = zeros.itemsize * zeros.size
print(mem_size)
np.info(np.add)
arr = np.zeros(10)
arr[4] = 1
print(arr)
arr = np.arange(10,50)
print(arr)
arr = np.arange(0,10)
print(arr[::-1])