import matplotlib.pyplot as plt

# Values
voc_resistance = 82.36   # Ohm
half_voc_resistance = 41.2  # Ohm
load_resistance = 50     # Ohm

labels = ['Rth for Voc', 'Rth for half Voc', 'closest Load Resistance']
values = [voc_resistance, half_voc_resistance, load_resistance]

# Colors: same for Voc & Half Voc, different for load
colors = ['tab:blue', 'tab:blue', 'tab:orange']

# Plot
plt.figure()
plt.bar(labels, values, color=colors)

plt.ylabel("Resistance (Ohm)")
plt.title("Comparison of Open Circuit and Load Resistance")

# Annotate values
# for i, v in enumerate(values):
#     plt.text(i, v, f"{v:.2f} Ω", ha='center', va='bottom')

plt.grid(axis='y')
plt.show()