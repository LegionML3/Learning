import numpy as np
n = int(input("num: "))
array = np.arange(n**2).reshape(n, n)
print(array)
mean_colums = np.array(array.sum(axis=0))
mean_colums.reshape(int(n / 2), int(n * 2))

print(array)
print(mean_colums)
