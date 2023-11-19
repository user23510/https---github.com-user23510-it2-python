import pandas as pd


df = pd.read_csv("modified.csv")
df2 = df[["Name", "Type 1", "Type 2", "HP", "Attack", "Defense", "Generation", "Legendary", "Total"]]
print(df.columns)
grass_and_poison = df2.loc[  # only grass and poison. | means or
                (df["Type 1"] == "Grass") & (df["Type 2"] == "Poison")  # (df["Legendary"] == True)
    ]                                                                   # (df["HP"] > 70)
grass_and_poison = grass_and_poison.reset_index(drop=True)  # reset index  # drop=False saves old index in separate column
#print(grass_and_poison.head(40))

mega = df2.loc[df2["Name"].str.contains('Mega')]  #prints the rows containing Mega in Names
#mega = df2.loc[~df["Name"].str.contains('Mega')]  # doesnt contains Mega
print(mega)

print("--------------")
import re                               # flags.re.I ignores case
fire_and_grass = df2.loc[df2["Type 1"].str.contains("fire|grass",  flags=re.I, regex=True)]  #
#print(fire_and_grass.head(30))

                                    # ^ specifies start of word [a-z] means what characters are allowed
piAZ = df2.loc[df2["Name"].str.contains("^pi[a-z]",  flags=re.I, regex=True)]  #  can be put in front of "pi"
#print(piAZ)

df2.loc[df2["Type 1"] == "Fire", "Type 1"] = "Flamer"  # changes Fire positions to Flamer

df2.loc[df2["Type 1"] == "Bug", "Legendary"] = True  # all bug pokemon are now legendary

#if value in total column is grater than 500. Change value in generation and legendary column to test value
df2.loc[df2["Total"] > 500, ["Generation", "Legendary"]] = ["TEST ONE", "TEST TWO"]

print(df2.head(30))
