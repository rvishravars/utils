# Let's calculate the covariance between two discrete variables using 
# Python. Covariance measures how much two random variables vary together. 
# If the variables tend to increase together, the covariance is positive. 
# If one tends to increase when the other decreases, the covariance is negative.

# Example: Covariance of Discrete Variables
# Let's consider two discrete variables: the number of hours studied and the 
# scores obtained by a group of students.

import numpy as np

# Data: hours studied and scores obtained
hours_studied = np.array([2, 3, 4, 5, 6])
scores = np.array([50, 60, 70, 80, 90])

# Calculate the mean of each variable
mean_hours = np.mean(hours_studied)
mean_scores = np.mean(scores)

# Calculate the covariance using the formula for discrete variables
# Cov(X, Y) = Σ [(X_i - E(X)) * (Y_i - E(Y))] / N
covariance = np.mean((hours_studied - mean_hours) * (scores - mean_scores))

# Alternatively, you can use numpy's cov function and extract the covariance value
cov_matrix = np.cov(hours_studied, scores, ddof=0)
covariance_np = cov_matrix[0, 1]

print("Covariance calculated manually:", covariance)
print("Covariance calculated using numpy:", covariance_np)