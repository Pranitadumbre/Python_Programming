import numpy as np
import matplotlib.pyplot as plt

from sklearn.svm import SVC
from sklearn.datasets import make_circles


# Create nonlinear dataset
X, y = make_circles(n_samples=200, noise=0.08, factor=0.5, random_state=42)


# Train Linear SVM
linear_model = SVC(kernel='linear')
linear_model.fit(X, y)


# Train RBF SVM
rbf_model = SVC(kernel='rbf', gamma=2)
rbf_model.fit(X, y)


# Function to plot boundary
def plot_decision_boundary(model, X, y, title):

    plt.figure(figsize=(7, 6))

    # plot points
    plt.scatter(X[:, 0], X[:, 1], c=y, s=60, cmap='bwr', edgecolors='k')

    # grid
    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    xx = np.linspace(xlim[0], xlim[1], 400)
    yy = np.linspace(ylim[0], ylim[1], 400)
    YY, XX = np.meshgrid(yy, xx)

    xy = np.vstack([XX.ravel(), YY.ravel()]).T
    Z = model.decision_function(xy).reshape(XX.shape)

    # decision boundary
    ax.contour(XX, YY, Z, levels=[0])

    plt.title(title)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()


# Plot Linear Kernel Result
plot_decision_boundary(linear_model, X, y,
                       "SVM with Linear Kernel")

# Plot RBF Kernel Result
plot_decision_boundary(rbf_model, X, y,
                       "SVM with RBF Kernel")