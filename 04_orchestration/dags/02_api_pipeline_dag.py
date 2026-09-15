from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import requests

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/opt/airflow/config/gcp_key.json"

import pandas_gbq 
import google.auth

# 1. Python function to extract and load API data to BigQuery
def extract_and_load_api_data():
    print("Starting API extraction...")    
    
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

    # Grab the credentials from the VIP badge we set at the top of the file
    credentials, project = google.auth.default()

    pandas_gbq.to_gbq(clean_df, destination_table=bq_table, project_id=gcp_project_id, if_exists='replace', credentials=credentials)

    print("✅ Success! The data is now live in BigQuery.")
    
    print("Data successfully extracted! (BigQuery upload pending GCP connection)")

# 2. Define the DAG
with DAG(
    dag_id='02_retail_data_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule='@daily',
    catchup=False,
    tags=['production', 'ingestion']
) as dag:

    # 3. Define the Task
    extract_task = PythonOperator(
        task_id='fetch_api_and_load_to_bq',
        python_callable=extract_and_load_api_data
    )

    # When we add dbt later, the flow will look like this:
    # extract_task >> run_dbt_models_task