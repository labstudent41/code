import numpy as np
def sigmoid(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

x = np.array([
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 1, 0, 0]
    ])

y = np.array([[0, 0, 1, 0, 1, 0, 1, 0]]).T

np.random.seed(1)
w0 = 2 * np.random.random((4, 4)) - 1
w1 = 2 * np.random.random((4, 1)) - 1

for i in range(1000):
    l_input = x
    l1 = sigmoid(l_input.dot(w0))
    l_output = sigmoid(l1.dot(w1))

    l_output_error = y - l_output
    l_output_delta = l_output_error * sigmoid(l_output, True)
    l1_error = l_output_delta.dot(w1.T)
    l1_delta = l1_error * sigmoid(l1, True)

    w1 = w1 + 2 * l1.T.dot(l_output_delta)
    w0 = w0 + 2 * l_input.T.dot(l1_delta)

print("Final weights :-\n", w0)
print("Output after training :-\n", l_output)
print("Loss: \n", np.mean(np.square(y - l_output)))
