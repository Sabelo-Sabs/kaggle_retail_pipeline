# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.6
#   kernelspec:
#     display_name: kaggle_retail_pipeline-Ce8mgkCP
#     language: python
#     name: python3
# ---

# Data Acquisition from Kaggle
#
# In this step, we'll programmatically download the "Global Superstore Sales Forecasting" dataset from Kaggle using the Kaggle CLI. The dataset will be stored in the `data/` directory for further processing in our ETL pipeline.

# **Downloading the Dataset Using Kaggle CLI**

# +
# Ensure the data directory exists
import os

data_dir = 'data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Download the dataset using Kaggle CLI
# Dataset URL: https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting

# Replace 'rohitsahoo/sales-forecasting' with the correct dataset identifier if different
# !kaggle datasets download -d rohitsahoo/sales-forecasting -p {data_dir} --unzip
# -

# **Verifying the Download**

# List the contents of the data directory to verify the download
files = os.listdir(data_dir)
print("Files in 'data/' directory:")
for file in files:
    print(f"- {file}")

# **Handling Potential Download Issues**

# +
# Check if the main CSV file exists
csv_file = os.path.join(data_dir, 'train.csv')

if os.path.exists(csv_file):
    print(f"Dataset downloaded successfully: {csv_file}")
else:
    print("Error: Dataset not found. Please check your Kaggle API credentials and the dataset identifier.")
# -

# **Initialize the SQLite Database Connection**

# **Import Libraries and Create Engine**

# +
# Import necessary libraries
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text


# Create SQLAlchemy engine for SQLite database
engine = create_engine('sqlite:///retail_sales.db', echo=False)

# Confirm the connection
print("SQLite database 'retail_sales.db' connected successfully.")
# -

# #### **Read the CSV into DataFrame**

# +
# Path to the CSV file
csv_file = 'data/train.csv'

# Read the CSV file into a Pandas DataFrame
df_sales = pd.read_csv(csv_file)
# -

# Display the first few rows to verify
df_sales.head()

#  **Truncate the Staging Table**

# +
from sqlalchemy import text

# Connect to the database
with engine.connect() as conn:
    # Check if the staging table exists
    result = conn.execute(text("""
    SELECT name 
    FROM sqlite_master 
    WHERE type='table' AND name='stg_sales';
    """))
    table_exists = result.fetchone()
    
    if table_exists:
        # Truncate the table by deleting all records
        conn.execute(text("DELETE FROM stg_sales;"))
        print("Staging table 'stg_sales' truncated.")
    else:
        # If the table does not exist, inform the user
        print("Staging table 'stg_sales' does not exist. It will be created.")
# -

# **Load Data into Staging Table**

# +
# Write the DataFrame to the staging table
df_sales.to_sql('stg_sales', engine, if_exists='replace', index=False)

print(f"Data loaded into 'stg_sales'. Total rows: {len(df_sales)}")
# -

# **Verify the Data Load**

# +
# Query the staging table to count the number of rows
with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) FROM stg_sales;"))
    row_count = result.fetchone()[0]
    print(f"Number of rows in 'stg_sales': {row_count}")

# Compare with the DataFrame's row count
df_row_count = len(df_sales)
print(f"Number of rows in DataFrame: {df_row_count}")

# Check if the counts match
if row_count == df_row_count:
    print("Verification successful: Row counts match.")
else:
    print("Verification failed: Row counts do not match.")

# -


