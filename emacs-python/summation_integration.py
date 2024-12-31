import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Install following sudo apt-get install python3-tk
import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg' or 'WebAgg' based on your environment

# Summation Example: Total Sales for Each Day of the Week
sales = [150, 200, 250, 300, 350, 400, 450]  # Sales for each day from Monday to Sunday
total_sales = sum(sales)

# Integration Example: Total Distance Traveled by a Car
# Speed function: f(t) = 3t^2 (speed in km/hr, time in hours)
def speed(t):
    return 3 * t**2

# Integrate the speed function from t=0 to t=2 hours to find the total distance
distance, error = quad(speed, 0, 2)

# Plotting the Sales Data
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.bar(days, sales, color='skyblue')
plt.title('Total Sales for Each Day of the Week')
plt.xlabel('Day')
plt.ylabel('Sales')
plt.text(3, max(sales) - 50, f'Total Sales: {total_sales}', fontsize=12)

# Plotting the Speed Function and Area Under the Curve
t_values = np.linspace(0, 2, 100)
speed_values = speed(t_values)

plt.subplot(1, 2, 2)
plt.plot(t_values, speed_values, label='Speed (3t^2)')
plt.fill_between(t_values, speed_values, alpha=0.3)
plt.title('Total Distance Traveled by a Car')
plt.xlabel('Time (hours)')
plt.ylabel('Speed (km/hr)')
plt.text(1, max(speed_values) - 10, f'Total Distance: {distance:.2f} km', fontsize=12)
plt.legend()

plt.tight_layout()
plt.show()
