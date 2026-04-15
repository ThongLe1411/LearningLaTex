import matplotlib.pyplot as plt

# Given values
i_enter = 0.060178  # A
i_leave = 0.058305  # A

labels = ['Current Entering', 'Current Leaving']
values = [i_enter, i_leave]

# Custom colors
colors = ['tab:blue', 'tab:orange']

# Plot
plt.figure()
plt.barh(labels, values, color=colors)

plt.xlabel("Current (A)")
plt.title("KCL Verification: Current Entering vs Leaving")

# Annotate values
# for i, v in enumerate(values):
#     plt.text(v, i, f"{v:.6f}", va='center')
plt.grid(axis='x')
plt.show()