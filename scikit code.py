import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 8, 10])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Prediction
y_pred = model.predict(X)

# Print values
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Predicted values:", y_pred)

# Plot graph
plt.scatter(X, y, label="Actual Data")
plt.plot(X, y_pred, label="Regression Line")

plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Linear Regression using Scikit-learn")
plt.legend()
plt.show()