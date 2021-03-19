def linear_cost(X,y,theta):
    h = X @ theta
    return ((h - y)**2).sum() / (2*len(X))


def linear_cost_gradient(X,y,theta):
    h = X @ theta
    return (X.T @ (h-y)) / len(X)

