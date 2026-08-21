import pandas as pd

print("Downloading data from the internet...")

# 1. Read the Sales Data and Store Metadata
sales_url = "https://raw.githubusercontent.com/Mounaki/Walmart-Sales-Prediction/master/train.csv"
stores_url = "https://raw.githubusercontent.com/Mounaki/Walmart-Sales-Prediction/master/stores.csv"

# Load them into DataFrames
sales_df = pd.read_csv(sales_url)
stores_df = pd.read_csv(stores_url)

print("✅ Data downloaded successfully!\n")

print("--- Sales Table (First 3 rows) ---")
print(sales_df.head(3))
print(len(sales_df.index))

print("\n--- Stores Table (First 3 rows) ---")
print(stores_df.head(3))
print(len(stores_df.index))



# YOUR MISSION:
# 1. Look at the columns in both tables. Find the column they have in common.
#ANSWER: The column they have in common is "Store".


# 2. Perform a LEFT JOIN on `sales_df` and `stores_df`.
merged_df = pd.merge(sales_df, stores_df, on="Store", how="left")

# 3. Create a new DataFrame called `merged_df` that holds the joined data.
print(merged_df.head(5))

# 4. Print the first 5 rows of `merged_df` to prove it worked.
print(merged_df.head(5))

