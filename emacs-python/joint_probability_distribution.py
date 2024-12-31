#Let's consider a real-time example involving the joint distribution of the height and weight of individuals.

#Scenario: Suppose we have data on the height (in cm) and weight (in kg) of a group of people. We want to understand the relationship between height and weight.
#Python Example
#Here's how you might visualize a joint distribution using a scatter plot and a 2D histogram (heatmap) in Python:

import numpy as np
import matplotlib.pyplot as plt

# Generate random data for height and weight
np.random.seed(0)
height = np.random.normal(170, 10, 1000)  # Mean height 170 cm, std dev 10 cm
weight = np.random.normal(70, 15, 1000)   # Mean weight 70 kg, std dev 15 kg

# Scatter plot of height vs. weight
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(height, weight, alpha=0.5)
plt.title('Scatter Plot of Height vs. Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')

# 2D histogram (heatmap) of height vs. weight
plt.subplot(1, 2, 2)
plt.hist2d(height, weight, bins=30, cmap='Blues')
plt.colorbar(label='Count')
plt.title('2D Histogram of Height vs. Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')

plt.tight_layout()
plt.show()
