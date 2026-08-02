import pandas as pd



# Objective 1: Read the CSV

df = pd.read_csv('retail_sales_dataset.csv')



# Objective 2: Standardize Column Names: The Kaggle headers have spaces (e.g., Product Category, Total Amount). Use Pandas to rename them to lower_snake_case (e.g., product_category, total_amount) to make querying easier
df.columns = df.columns.str.replace(' ', '_').str.lower()



# Objective 3: Data Inspection: Print the first 5 rows and the data types of the columns (df.info()) to ensure it loaded correctly.
print("First 5 rows of the dataset:\n", df.head())
print("\nData types of the columns:\n", df.info())



# Objective 4: Handle Missing Values: Check for any missing values in the dataset. If there are any, decide on a strategy to handle them (e.g., fill with mean/median, drop rows, etc.)
missing_values = df.isnull().sum()
print("Missing values in each column:\n", missing_values)



# Objective 5: Convert Data Types: Ensure that each column has the appropriate data type (e.g., dates should be in datetime format, numerical values should be in float or int). Convert any columns that are not in the correct format.
# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], errors='coerce')        



# Objective 6: Remove Duplicates: Check for any duplicate rows in the dataset and remove them if necessary.
duplicates = df.duplicated().sum()
print("Number of duplicate rows:", duplicates)
df = df.drop_duplicates()       



# Objective 7: Group and Aggregate: We want to know which product category makes the most money. Create a new DataFrame called category_sales. Group the data by product_category and calculate the sum() of the total_amount
category_sales = df.groupby('product_category')['total_amount'].sum().reset_index()
print("Total sales by product category:\n", category_sales)



#Objective 8: Sort the Data: Sort category_sales from highest revenue to lowest.
category_sales = category_sales.sort_values(by='total_amount', ascending=False).reset_index(drop=True)
print("Total sales by product category (sorted):\n", category_sales)    



# Objective 9: Save your summarized category_sales DataFrame to a new file called top_selling_categories.csv
category_sales.to_csv('top_selling_categories.csv')