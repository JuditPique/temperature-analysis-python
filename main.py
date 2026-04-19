import pandas as pd
from matplotlib import pyplot as plt

# Load data
data = pd.read_csv("temperature_data.csv")

# Show first rows
print(data.head())

# Extract columns
days = data["day"]
temperatures = data["temperature"]

# Basic analysis
average_temp = temperatures.mean()
max_temp = temperatures.max()

print("Average temperature:", average_temp)
print("Max temperature:", max_temp)
print("Min temperature:", temperatures.min())
max_day = data.loc[temperatures.idxmax(), "day"]
print("Max temperature day:", max_day)

# Plot
plt.plot(days, temperatures, marker='o')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.title("Temperature over time")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.scatter(days, temperatures)
plt.savefig("temperature_plot.png")
plt.show()