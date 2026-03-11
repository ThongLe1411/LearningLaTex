import matplotlib.pyplot as plt
import numpy as np

# Component labels
components = ['Rx', 'R2', 'R3', 'R4']
x = np.arange(len(components))
width = 0.25

# Simulated values
sim_resistance = [2500, 1000, 10000, 4000]      # Ohms
sim_voltage = [1, 1, 4, 4]                      # Volts
sim_current = [4e-4, 0.001, 4e-4, 0.001]        # Amps

# Measured values
meas_resistance = [2512, 931, 10042, 4023]      # Ohms
meas_voltage = [1.021, 1.014, 4.002, 4.031]     # Volts
meas_current = [3.981e-4, 0.0011, 3.983e-4, 9.943e-4]  # Amps

fig, axes = plt.subplots(3, 1, figsize=(6, 10))

axes[0].bar(x - width/2, sim_resistance, width, label='Simulated', color='mediumblue')
axes[0].bar(x + width/2, meas_resistance, width, label='Measured', color='darkorange')
axes[0].set_title('Resistance Comparison')
axes[0].set_xticks(x)
axes[0].set_xticklabels(components)
axes[0].set_ylabel('Resistance (Ω)')
axes[0].legend()


axes[1].bar(x - width/2, sim_voltage, width, label='Simulated', color='mediumblue')
axes[1].bar(x + width/2, meas_voltage, width, label='Measured', color='darkorange')
axes[1].set_title('Voltage Comparison')
axes[1].set_xticks(x)
axes[1].set_xticklabels(components)
axes[1].set_ylabel('Voltage (V)')
axes[1].legend()

# --- Current ---
axes[2].bar(x - width/2, sim_current, width, label='Simulated', color='mediumblue')
axes[2].bar(x + width/2, meas_current, width, label='Measured', color='darkorange')
axes[2].set_title('Current Comparison')
axes[2].set_xticks(x)
axes[2].set_xticklabels(components)
axes[2].set_ylabel('Current (A)')
axes[2].legend()

plt.tight_layout()
plt.show()
