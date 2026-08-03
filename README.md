Retail Sales Data Pipeline

Overview

This project contains a Python-based ETL pipeline that processes raw retail sales data. It performs data cleaning, standardization, and aggregation to generate two key business reports:

Top selling product categories by revenue.

Top performing months by revenue.

Technologies Used

Python: Data transformation and aggregation.

Pandas: Columnar data manipulation.

Git: Version control and pipeline management.

How to run

Ensure retail_sales_dataset.csv is in the root directory.

Run the pipeline: python3 clean_data.py

The script will automatically generate top_selling_categories.csv and top_selling_months.csv.