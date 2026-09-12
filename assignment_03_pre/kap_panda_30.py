import subprocess
# Clear screen on Windows
subprocess.run("cls", shell=True)
import pandas as pd
print("########################################")
'''
df = pd.DataFrame({
    "Cities": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
    "Population": [8419600, 3980400, 2716000, 2328000, 1690000],
    "State": ["NY", "CA", "IL", "TX", "AZ"]
})
print(df)
df.loc[len(df)] = ["Philadelphia", 1584200, "PA"]
print(df)
print(round(df['Population'].mean(),2))
df['PP'] = df['Population'] / (df['Population'].mean())
print(df)
'''

#'''
df1 = pd.read_csv("sales.csv", sep="\t")
print("\n#          INFO          #" )
print(df1.info())
print("\n#         DESCRIBE         #" )
print(df1.describe())
print("\n#          HEAD          #" )
print(df1.head())
print("\n#          SHAPE          #" )
print("shape:", df1.shape)
#'''
'''
print('One Column:\n', df1["City"].head(), '\n')
df = pd.read_csv("sales.csv", sep="\t")
print(repr(df.columns))
print(df)
print("one column :\n", df["City"].head(), "\n")
print("two cols   :\n", df[["City", "Revenue"]].head(), "\n")
print("loc by label:\n", df.loc[0:2, ["City", "Revenue"]], "\n")
print("iloc by pos :\n", df.iloc[0:2, 0:3])

big = df[df["Revenue"] > 2000]
print(big)
df["Price_per_Unit"] = df["Revenue"] / df["Units_Sold"]
print(df.head())

df2 = df.drop(columns=["Month"])
print("\nafter drop:\n", df2.head())
import pandas as pd
import numpy as np

df = pd.DataFrame({"x": [1, 2, np.nan, 4], "y": [np.nan, 5, 6, 7]})
print("Original:\n", df)
print("isnull:\n", df.isnull())
print("\nfillna(0):\n", df.fillna(0))
print("\ndropna:\n", df.dropna())

df = pd.read_csv("sales.csv", sep="\t")
gby_city = df.groupby("City")["Revenue"].sum().sort_values(ascending=True)
print("Group by City:\n", gby_city)

print("\nUnits sold by product:\n", df.groupby("Product")["Units_Sold"].sum())
data = {
    'Title': ['Inception', 'Dunkirk', 'Interstellar', 'The Prestige', 'Memento'],
    'Director': ['Christopher Nolan', 'Christopher Nolan', 'Christopher Nolan', 'Christopher Nolan', 'Christopher Nolan'],
    'Rating': [8.8, 7.9, 8.6, 8.5, 8.4]
}
dfd = pd.DataFrame(data)
print("Original DataFrame:\n", dfd)
print("Average Rating by Director:\n", dfd.groupby('Director')['Rating'].mean()[['Christopher Nolan']])
#
data = {
    'Product': ['Laptop', 'Desktop', 'Tablet', 'Phone', 'Smartwatch'],
    'Price': [25000, 12000, 8000, 22000, 5000]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
# Filter products with price greater than 10000
price_filter = df[df['Price'] >= 20000]
print("\nProducts with Price greater or equal to 20000:\n", price_filter)
#
data = {
    'Store': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Item': ['Apple', 'Banana', 'Orange', 'Grape', 'Apple', 'Banana', 'Orange', 'Grape'],
    'Price': [50, 20, 30, 60, 55, 22, 33, 65],
    'Quantity': [10, 12, 15, 16, 20, 25, 30, 35]
}

df = pd.DataFrame(data)
# add a new column 'Revenue' by multiplying 'Price' and 'Quantity'
df['Revenue'] = df['Price'] * df['Quantity']
# Group by 'Store' and calculate the total revenue for each store
revenue_by_store = df.groupby('Store')['Revenue'].sum()
print("\nTotal Revenue by Store:\n", revenue_by_store)
#Average price of items sold by each store
average_price_by_store = df.groupby('Store')['Price'].mean()
print("\nAverage Price by Store:\n", average_price_by_store)
#
data = {
    'Customer': ['Alice', 'Bob', 'Alice', 'Alice', 'Bob', 'Bob', 'Alice', 'Bob'],
    'Item': ['Pen', 'Pencil', 'Notebook', 'Eraser', 'Pen', 'Pencil', 'Notebook', 'Eraser'],
    'Price': [10, 5, 50, 20, 10, 5, 50, 20],
    'Quantity': [3, 4, 2, 5, 10, 6, 1, 2]
}
df = pd.DataFrame(data)
df['Amount'] = df['Price'] * df['Quantity']
print("Original DataFrame:\n", df)
comm = df.groupby('Customer')['Amount'].sum()
print(comm)
#
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Temperature': [20, 22, 25, 27, 30, 32, 35, 34, 30, 28, 24, 21]
}
df = pd.DataFrame(data)
# sort the DataFrame by Temperature in descending order
sorted_df = df.sort_values(by='Temperature', ascending=False)
print("Sorted DataFrame by Temperature:\n", sorted_df)
sorted_df_highest = sorted_df['Month'].iloc[0]
print("Month with the highest temperature:", sorted_df_highest)
#
data = {
    'Category': ['Fruit', 'Vegetable', 'Fruit', 'Vegetable', 'Fruit', 'Vegetable'],
    'Name': ['Apple', 'Carrot', 'Banana', 'Potato', 'Grape', 'Onion'],
    'Price': [2, 1, 1.5, 0.5, 3, 1],
    'Quantity': [10, 20, 15, 30, 5, 40]
}

df = pd.DataFrame(data)
fruits = df[df['Category'] == 'Fruit']
total_fruit_value = fruits['Price'].sum() * fruits['Quantity'].sum()
print(total_fruit_value)
#
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
result = df[df['Age'] >= 30].sort_values(by='Age', ascending=False).iloc[0]['City']
print(result)
#
data = {
    'Product': ['A', 'B', 'C', 'A', 'B', 'C'],
    'Price': [100, 200, 300, 150, 250, 350],
    'Quantity': [10, 5, 7, 12, 8, 5]
}
df = pd.DataFrame(data)
total_revenue = (df['Price'] * df['Quantity']).sum()
average_price = df['Price'].mean()
print(total_revenue, average_price)
#
data = {
    'Customer': ['Alice', 'Bob', 'Alice', 'Alice', 'Bob', 'Bob', 'Alice', 'Bob'],
    'Item': ['Pen', 'Pencil', 'Notebook', 'Eraser', 'Pen', 'Pencil', 'Notebook', 'Eraser'],
    'Price': [10, 5, 50, 20, 10, 5, 50, 20],
    'Quantity': [3, 4, 2, 5, 10, 6, 1, 2]
}

df = pd.DataFrame(data)
# Calculate the total amount spent per item
df['Amount'] = df['Price'] * df['Quantity']
dfitem = df.groupby('Item')['Amount'].sum().sort_values(ascending=False)
print("Total Amount Spent per Item:\n", dfitem)
# Calculate the total amount spent by all customers
total_spent = df['Amount'].sum()
print("Total Amount Spent by All Customers:", total_spent)
#import pandas as pd
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'City_A_Temp': [20, 22, 25, 27, 30, 32, 35, 34, 30, 28, 24, 21],
    'City_B_Temp': [10, 12, 15, 17, 20, 22, 25, 24, 20, 18, 14, 11]
}
df = pd.DataFrame(data)
df['Diff'] = df['City_A_Temp'] - df['City_B_Temp']
print("Average Temperature Difference by Month:\n", df.groupby('Month')['Diff'].mean())
'''
