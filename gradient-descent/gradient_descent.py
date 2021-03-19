import numpy as np

def gradient_descent(
    X,
    y,
    theta_0, 
    cost_function, cost_function_gradient,
    learning_rate, threshold,
    max_iter=100000
):
    theta = theta_0
    iteration = 0
    costs = []
    thetas = []

    while np.linalg.norm(cost_function_gradient(X, y, theta)) > threshold and iteration < max_iter:
        iteration += 1
        theta -= learning_rate * cost_function_gradient(X, y, theta)
        costs.append(cost_function(X, y, theta))
        thetas.append(theta.copy())

    return theta, costs, thetas
