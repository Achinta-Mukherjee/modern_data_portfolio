import pandas as pd
import requests

print("🚀 Fetching Data for Normalization...")

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code == 200:
    raw_data = response.json()
    
    # The old way (leaves 'address' and 'company' as messy dictionaries)
    # df = pd.DataFrame(raw_data)
    
    # YOUR MISSION:
    # 1. Google how to use `pd.json_normalize()` in Pandas.
    # 2. Use it on `raw_data` to create a new DataFrame called `flat_df`.
    # 3. Print the columns of `flat_df` using `print(flat_df.columns)` to see the magic!
    # 4. Filter the DataFrame to show only: 'name', 'email', and 'address.city'
    # 5. Print the first 5 rows.

    flat_df = pd.json_normalize(raw_data)
    print(flat_df.columns)
    flat_df = flat_df[['name', 'email', 'address.city']]
    print(flat_df.head())
    
else:
    print("❌ Connection Failed.")