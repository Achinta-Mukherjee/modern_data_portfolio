import pandas as pd
import numpy as np

# A messy dataset with missing values (np.nan is the Python equivalent of NULL)
messy_data = {
    'Transaction_ID': [1001, 1002, 1003, np.nan, 1005],
    'Store_Location': ['Mumbai', 'Delhi', np.nan, 'Pune', 'Mumbai'],
    'Revenue': [1500, np.nan, 2000, 1200, np.nan]
}

df = pd.DataFrame(messy_data)

print("--- Original Messy Data ---")
print(df)
print("\n--- Data Information ---")
# df.info() tells you how many non-null values exist in each column
df.info()

# YOUR MISSION:
# 1. Google how to fill missing (NaN) values in a specific Pandas column.
#    - Fill the missing values in the 'Revenue' column with 0 (Like SQL: ISNULL(Revenue, 0))

df['Revenue'] = df['Revenue'].fillna(0)



# 2. Google how to drop rows that have missing values in a specific column.
#    - Drop the row where 'Transaction_ID' is missing (Like SQL: WHERE Transaction_ID IS NOT NULL)

df.dropna(subset=['Transaction_ID'], inplace=True)

# 3. Print your final, cleaned DataFrame!
print("--- Final Cleaned Data ---")
print(df)
print("\n--- Data Information ---")
df.info()