import pandas as pd
data = {
"calories": [420, 380, 390],
"duration": [50, 40, 45]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df)

# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table
# with rows and columns.

print(df.loc[0])
print(df.loc[[0, 1]])
print(df[['calories']])

df1 = pd.read_csv('data.csv',header=0)
print(df1.head(10))

# Step 1: Copy the given CSV file ‘Test1.csv’ into the working folder and create a new python file to
# load the CSV file using Pandas DataFrame.

df2 = pd.read_csv('Test1.csv',header=0)



# Step 3: Clean the dataset by removing empty cells and duplicates. Print the first 5 rows of the
# dataset

# Remove rows that contain empty cells:
df2.dropna(inplace = True)

# Remove all duplicates:
df2.drop_duplicates(inplace = True)

# Step 2: Print the first 5 rows of the dataset.
print(df2.head(5))

# Step 4: Add a new column "Result" with the values 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
# 1100, and 1200. . Print the first 5 rows of the dataset.
df2.insert(3, "Result", [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200], True) 

# Step 5: Multiply the values in the ‘Result’ column by 2.
df2['Result']=df2['Result']*2
print(df2.head(5))