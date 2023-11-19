import pandas as pd

# Sample DataFrame
data = {
    'Column_Name': ['A', 'B', 'B', 'C', 'B', "B", "a", "e", "c", "c", "c", "a", 'A', 'C', 'B', 'C', 'D', 'D', 'D'],
    'installations': ['2', '3', '6', '1', '8', "4", "6", "3", "6", "2", "6", "9", '7', '8', '5', '3', '6', '5', '2'],

}

df = pd.DataFrame(data)

#converts lower case characters to upper case
df['Column_Name'] = df['Column_Name'].str.upper()

# Use value_counts to count occurrences of unique values
value_counts = df['Column_Name'].value_counts(ascending=True)

# Get the top 3 most occurring values
top_3_values = value_counts.head(3)



#show amount in column name
#average rating
# average amount of installations for each of the categories


#pandas tutorial:
#       summing columns and adding into new column
#    
#
#
#
#
print(value_counts)
print(top_3_values)


for value, count in top_3_values.items():
    #print(f"Value: {value}, Count: {count}")
    print("Value: ", value, "Count: ", count)

# touch grass, work out
# pandas tutorial
# pandas documentation
# try eksamen questions

# søknads
# look at black friday products
