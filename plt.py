import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
df2 = pd.read_csv("modified.csv")
# Convert "HP" column to numeric, coercing errors to NaN
df2["HP"] = pd.to_numeric(df2["HP"], errors="coerce")
# Drop rows with NaN values in the "HP" column
df2 = df2.dropna(subset=["HP"])

df = pd.read_csv("gas_prices.csv")
average = df2.groupby("Type 1")["HP"].mean().reset_index()  # reset index needed for plotting
print(average)

bars = plt.bar(average["Type 1"].head(10), average["HP"].head(10))
for bar in bars:
    bar.set_hatch("O")
plt.show()



x = [1, 2, 3]
y = [1, 4, 9]
z = [10, 5, 0]

#plt.plot(x, y, label='2x', color='red', linewidth=2, marker=".", markersize=10, linestyle="-")

x3 = np.arange(0,4.5,0.5)
print(x3)
#plt.plot(x3, x3**2, label='x3', color='orange', linewidth=2, marker=".", markersize=10, linestyle="-")

plt.title("test plot")
plt.xlabel("x")
plt.ylabel("y and z")
plt.legend()
#plt.show()

#plt.savefig("mygraph.png")
print("---------------")

labels = ["a", "b", "c"]
values = [1, 3, 9]

