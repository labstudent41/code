import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

x = np.array([1, 5, 1.5, 8, 1, 9, 7, 8.7, 2.3, 5.5, 7.7, 6.1])
y = np.array([2, 8, 1.8, 8, 0.6, 11, 10, 9.4, 4, 3, 8.8, 7.5])

# show unclassified data
plt.scatter(x, y)
plt.show()

# shaping data for training model
training_X = np.vstack((x, y)).T
training_Y = [0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1]

# define the model
f = svm.SVC(kernel='linear', C=1.0)

# train model
f.fit(training_X, training_Y)

# get the values for linear equation from trained SVM model
f.fit(training_X, training_Y)

# get the values for linear equation from trained SVM model
w = f.coef_[0]

# get Y-intercept
a = -w[0] / w[1]

# maing X-axis space from data
x_axis = np.linspace(0, 12)

# get the Y-value to plot decision boundary
y_axis = a * x_axis - f.intercept_[0] / w[1]

# plot the decision boundary
plt.plot(x_axis, y_axis, 'k-')

# show the plot
plt.scatter(training_X[:, 0], training_X[:, 1], c=training_Y)
# plt.legend()
plt.show()
