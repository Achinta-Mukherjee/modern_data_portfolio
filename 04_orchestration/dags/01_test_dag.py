from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# 1. Define the Python function (The actual work)
def hello_data_engineer():
    print("Hello from Airflow! Achinta's first DAG is running perfectly.")

# 2. Define the DAG (The schedule and settings)
with DAG(
    dag_id='01_achinta_test_dag',
    start_date=datetime(2024, 1, 1),
    schedule='@daily',
    catchup=False,
    tags=['testing']
) as dag:

    # 3. Define the Task (Assigning the work to the worker)
    task_1 = PythonOperator(
        task_id='print_hello_world',
        python_callable=hello_data_engineer
    )

    # Note: If we had a task_2, we would set the order here like this:
    # task_1 >> task_2