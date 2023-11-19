import pandas as pd

df = pd.read_csv("pokemon_data.csv")

#print(df.head(3))  # top 3 rows
#print(df.tail(3))  # bottom 3 rows

#df_xlsx = pd.read_excel("pokemon_data.xlsx")

#print((df_xlsx.head(3)))  # pip install pyexcel

df_txt = pd.read_csv("pokemon_data.txt", delimiter = "\t")  # tab separated specify delimiter

print(df_txt.columns)  # prints header to all columns
print("----------")

#print(df["Name"][0:30])  # prints top 30 in names column

#print(df[["Name", "Type 2", "HP"]])  # prints these 3 columns

#print(df.iloc[0])  # prints spesific row

#print(df.iloc[2, 1])  # gives spesific position

#print(df.loc[df["Type 1"] == "Fire"][0:4])  # Only gives Type 1 that's equal to fire

print("-----")
#for index, row in df.iterrows():
#    print(index, row["Name"])

print(df.sort_values("Name", ascending=False).head(10))  # opposite of alphabetical because ascending=false

#print(df.sort_values(["Name", "Speed"], ascending=[1, 0])) dont understand

print("-----")  # make total column

d1 = df.iloc[:, 4:6].sum(axis=1)  # sums between 4th and 9th column together
d2 = df.iloc[:, 6:10].sum(axis=1)
df["Total"] = d1 + d2
#print(df["Total"].head(6))
#df = df.drop(columns=["Total"])  ## specify df = df when dropping a column

print("--------------------------")

#df = df[["Name", "HP", "Legendary"]]  # removes all other columns
#print(df.head(2))

df.to_csv("modified.csv", index=False)  # save to new csv # index=False removes old indexes
#df.to_excel("modified.xlsx")
#df.to_csv("modified.txt", sep="\t")  # separated by tabs

