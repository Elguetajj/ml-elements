import numpy as np 
from matplotlib import pyplot as plt
from gradient_descent import gradient_descent
from linear_cost import *

TRAINING_SET_SIZE = 200

x = 2 * np.random.rand(TRAINING_SET_SIZE,1)
y = 4 +3 * x+np.random.randn(TRAINING_SET_SIZE,1)

X = np.hstack(
    (
        np.ones(TRAINING_SET_SIZE).reshape(TRAINING_SET_SIZE,1),
        x
    )
)
# print(x.shape)
# print(y.shape)
# print(X)

# plt.plot(x, y, 'o', color='black');


m, n = X.shape
theta_0 = np.random.rand(n,1)

r_theta, costs, thetas = gradient_descent(
    X,
    y,
    theta_0,
    linear_cost,
    linear_cost_gradient,
    learning_rate=0.2,
    threshold=1
)

plt.plot(costs[:])

plt.show()