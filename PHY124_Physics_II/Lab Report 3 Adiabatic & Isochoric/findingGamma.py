import numpy as np
import matplotlib.pyplot as plt

# Data from the table
lnP = np.array([11.468, 11.828, 12.108, 12.262])
neg_lnV = np.array([8.3309, 8.6200, 8.88, 9.1333])

# Linear regression (best fit line)
coefficients = np.polyfit(neg_lnV, lnP, 1)
slope = coefficients[0]
intercept = coefficients[1]

# Create smooth line
x_fit = np.linspace(min(neg_lnV), max(neg_lnV), 100)
y_fit = slope * x_fit + intercept

# Plot
plt.figure()

plt.scatter(neg_lnV, lnP, label="Experimental Data")
plt.plot(x_fit, y_fit, label=f"Best Fit Line: y = {slope:.3f}x + {intercept:.3f}")

plt.xlabel("-ln(V) [m³]", fontsize = 12)
plt.ylabel("ln(P) [Pa]", fontsize = 12)
plt.legend()
plt.grid(True)

plt.show()

print("Slope =", slope)
print("Intercept =", intercept)
