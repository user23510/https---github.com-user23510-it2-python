import pandas as pd
import re
import matplotlib

df = pd.read_csv("modified.csv")
print(df.columns)

averageHP = df["HP"].mean()  # average hp
averageHPbytype1 = df.groupby("Type 1")["HP"].mean()  # average hp by type 1




averageGenFire = df[df["Type 1"] == "Bug"]["HP"].mean()  # average generation of type 1 fire
    # .max(), .min(), sum(), count(), median(), std(),    var(),    first(),  last(), describe()
                                        # standard deviation, variance
print("average gen for type 1 fire: ", averageGenFire)

agg = df.groupby("Type 1")["Generation"].agg(["mean", "first", "last"])
print(agg)

print("-----------------")
print("-----------------")

averageSteelDefense = df.groupby("Type 1")["Defense"].mean().sort_values(ascending=False)
print(averageSteelDefense)          # Steel have highest average defense stat
