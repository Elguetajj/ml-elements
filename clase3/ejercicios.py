import numpy as np
import time

# print(np.arange(10))

# arr = np.eye(7)

# print(arr,type(arr),arr.shape)



xs = np.arange(15).reshape(3,5)

thetas = np.arange(5).reshape(5,1)


print(thetas)
print(xs)


print(xs @ thetas)



# print(calc(xs,thetas))