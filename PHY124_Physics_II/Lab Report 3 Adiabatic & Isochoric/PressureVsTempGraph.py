import numpy as np
import matplotlib.pyplot as plt

# Data from table
temperature = np.array([325.82, 303.29, 289.16, 285.78])  # K
pressure = np.array([202754, 137752, 106892, 95986])      # Pa

# Linear regression
coefficients = np.polyfit(temperature, pressure, 1)
slope = coefficients[0]
intercept = coefficients[1]

# Generate best fit line
x_fit = np.linspace(min(temperature), max(temperature), 100)
y_fit = slope * x_fit + intercept

# Plot
plt.figure()

plt.scatter(temperature, pressure, label="Experimental Data")
plt.plot(x_fit, y_fit, label=f"Best Fit Line: y = {slope:.2f}x + {intercept:.2f}")

plt.xlabel("Temperature (K)")
plt.ylabel("Pressure (Pa)")
plt.title("Pressure vs Temperature (Isochoric Process)")
plt.legend()
plt.grid(True)

plt.show()

print("Slope =", slope)
print("Intercept =", intercept)
