import pandas as pd
import requests

print("🚀 Initiating API Connection...")

# 1. The API URL (This is a free public API that generates fake user data)
url = "https://jsonplaceholder.typicode.com/users"

# 2. We 'request' the data from the website
response = requests.get(url)

# 3. We check if the connection was successful (Status Code 200 means OK!)
if response.status_code == 200:
    print("✅ Connection Successful!")
    
    # 4. Extract the raw JSON data
    raw_data = response.json()

    #5. Exporting the json data to a csv file
    pd.DataFrame(raw_data).to_csv('api_data.csv', index=False)
    
    # Let's print the first record just to see how messy JSON looks
    # print("\n--- Raw JSON Data (First Record) ---")
    # print(raw_data[0])
    
    # YOUR MISSION:
    # 1. Use what you know about Pandas to turn 'raw_data' into a DataFrame called 'df'.
    df = pd.DataFrame(raw_data)



    # 2. Just like a SQL SELECT statement, filter the DataFrame to only show these columns:
    #    'id', 'name', 'email', and 'phone'.
    df = df[['id', 'name', 'email', 'phone']]



    # 3. Print the first 5 rows of your new, clean DataFrame!
    print(df.head())

else:
    print(f"❌ Connection Failed. Status Code: {response.status_code}")