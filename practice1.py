import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("modified.csv")
df2 = pd.read_csv("googleplaystore1.csv")
# Convert "HP" column to numeric, coercing errors to NaN
# Convert "HP" column to numeric, coercing errors to NaN
df2["Rating"] = pd.to_numeric(df2["Rating"], errors="coerce")
# Drop rows with NaN values in the "HP" column
df2 = df2.dropna(subset=["Rating"])

df2['Installs'] = df2['Installs'].str.replace('+', '')
df2['Installs'] = df2['Installs'].str.replace(',', '')  # removes comma from numbers thus able to read number
df2["Installs"] = pd.to_numeric(df2["Installs"], errors="coerce")
df2 = df2.dropna(subset=["Installs"])

print(df2.columns)


# finds number of instances of each category is in categories column
val = df2["Category"].value_counts()
val = val.head(3)

for c, v in val.items():
    average_rating = df2[df2["Category"] == c]["Rating"].mean()
    average_installs = df2[df2["Category"] == c]["Installs"].mean()

    print("Category: ", c, "| Number of apps: ", v, "| Average Rating: ", average_rating, "| Average Installs: ", average_installs)


for c, v in val.items():

    # b) Utvid programmet slik at det også presenterer de tre mest populære appene, målt i antall installasjoner, i hver av disse tre kategoriene.
    most_installs = df2[df2["Category"] == c]["Installs"].sort_values(ascending=False)
    most_installs = most_installs.head(3)
    # Print the "App" sorted after number of Installs column
    most_pop_apps = df2.loc[most_installs.index, "App"].head(3)  # .index important!!

    for app, installs in zip(most_pop_apps, most_installs):
        print("Most popular apps in ", c, "category: ", app, "| installs: ", installs)






for c, v in val.items():
    bars = plt.bar(c, v)
    for bar in bars:
        bar.set_hatch("O")

#plt.show()


# finds number of Fire Category type 1s that are over gen 4


