import pandas as pd
import requests
import pandas_gbq

# 0. Fetch
print("🚀 Fetching Data from API...")

# 1. Grab the API Data
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
raw_data = response.json()

# 2. Flatten and clean it using Pandas
df = pd.json_normalize(raw_data)
clean_df = df[['id', 'name', 'email', 'address.city']]

# Rename columns to be safe for BigQuery (no dots allowed in column names)
clean_df.columns = ['id', 'name', 'email', 'city']
print(clean_df.head(3))

# 3. The Cloud Load!
print("\n☁️ Uploading to Google BigQuery...")

# IMPORTANT: Using your true underlying GCP Project ID
gcp_project_id = 'project-f8aca53c-7f41-4c40-968' 
bq_table = 'raw_data.api_users'

# The Magic Line: Push the DataFrame directly to the cloud (Updated syntax)
pandas_gbq.to_gbq(clean_df, destination_table=bq_table, project_id=gcp_project_id, if_exists='replace')

print("✅ Success! The data is now live in BigQuery.")