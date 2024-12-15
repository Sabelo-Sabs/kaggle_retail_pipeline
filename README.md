# Project 1: Kaggle Retail Sales ETL Pipeline

## Overview
This project demonstrates an end-to-end data engineering workflow for integrating, modeling, and analyzing retail sales data sourced from Kaggle. It implements a star schema in SQLite, using SQLAlchemy ORM models for schema definition and SQL queries for transformations. Finally, it provides analytical queries to derive insights (e.g., monthly revenue trends and top-performing product categories).

**Key Highlights:**
- **External Data Integration:** Uses the Kaggle API to download real-world retail sales data.
- **Schema Design & Modeling:** Implements a star schema (fact and dimension tables) with `sqlalchemy` ORM.
- **SQL Transformations:** Performs data cleaning and transformations using raw SQL queries.
- **Data Quality Checks:** Includes referential integrity checks and ensures no missing foreign keys.
- **Analytics & Insights:** Produces monthly sales trends and category performance metrics.

## Prerequisites
- **Kaggle Account & API Key:**  
  Set up your Kaggle credentials by placing `kaggle.json` in `~/.kaggle/` and ensuring it has the correct permissions:
  ```bash
  chmod 600 ~/.kaggle/kaggle.json
  ```
- **Pipenv (Python environment):**  
  Install `pipenv` if you haven’t already:
  ```bash
  pip install --user pipenv
  ```

## Setup Instructions
1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/yourusername/project1_kaggle_retail_pipeline.git
   cd project1_kaggle_retail_pipeline
   ```

2. **Set Up the Virtual Environment with Pipenv:**  
   ```bash
   pipenv --python 3.9
   pipenv install pandas sqlalchemy kaggle jupyter
   pipenv shell
   ```
   
3. **Run the Jupyter Notebook:**  
   Launch Jupyter Notebook or JupyterLab:
   ```bash
   jupyter notebook
   ```
   Open `project1_pipeline.ipynb` in your browser and run all cells in order.

## Data Source
- **Dataset:** [Global Super Store Dataset (Kaggle)](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting)
  
  The dataset includes historical sales data across various product categories, regions, and time periods, allowing for rich analytical insights.

## Pipeline Steps
1. **Data Acquisition:**  
   Uses the Kaggle API to download the dataset into the `data/` directory.

2. **Staging:**  
   Loads the raw CSV file into a `stg_sales` table within an SQLite database (`retail_sales.db`).

3. **Schema Definition:**  
   Defines dimension and fact tables using `sqlalchemy` ORM models for clarity, maintainability, and structure.

4. **Transformations & Loading:**
   - Inserts cleaned, deduplicated dimension data into `dim_customers`, `dim_products`, and `dim_dates`.
   - Creates indexes on dimension tables for performance.
   - Populates the `fact_sales` table by joining `stg_sales` with the dimension tables via natural keys.

5. **Data Quality Checks:**
   - Verifies record counts.
   - Checks for any orphaned product IDs in the fact table.

6. **Analytics & Insights:**
   - Provides SQL queries to summarize monthly sales and profits.
   - Identifies top categories by revenue and profit.

## Outputs
- **Database:** `retail_sales.db` containing populated fact and dimension tables.
- **Summaries:** Printed DataFrames in the notebook showing monthly trends and top categories.

## Directory Structure
```bash
project1_kaggle_retail_pipeline/
├─ data/                 # Downloaded datasets
├─ project1_pipeline.ipynb
├─ README.md
├─ Pipfile
└─ Pipfile.lock
```

## Next Steps
- **Extend Validations:** Add more sophisticated data quality checks or integrate Great Expectations.
- **CI/CD:** Incorporate GitHub Actions to automatically test the ETL pipeline on each commit.
- **Visualization:** Create charts or dashboards (e.g., in a separate notebook or a BI tool) to present insights visually.
- **Parameterization:** Allow dataset paths or database connections to be set via environment variables.
