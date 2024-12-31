import numpy as np
import matplotlib.pyplot as plt

# Generate random heights following a normal distribution
mean_height = 175  # mean height in cm
std_dev = 7        # standard deviation in cm
sample_size = 1000

heights = np.random.normal(mean_height, std_dev, sample_size)

# Plot the distribution of heights
plt.hist(heights, bins=30, edgecolor='black', density=True)
plt.title('Distribution of Heights')
plt.xlabel('Height (cm)')
plt.ylabel('Frequency')
plt.show()
