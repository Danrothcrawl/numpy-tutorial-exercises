import numpy as np

print(np.__version__)
print(np.show_config())
print(np.zeros(10))
zeros = np.zeros(10)
mem_size = zeros.itemsize * zeros.size
print(mem_size)