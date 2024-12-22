# Project 1: Kaggle Retail Sales ETL Pipeline

## Overview
This project demonstrates an end-to-end data engineering workflow using data from Kaggle. We acquire a retail sales dataset, model it in a star schema using SQLite and SQLAlchemy, and transform the data via SQL queries. Finally, we produce analytical insights (e.g., monthly revenue and category performance).

**Key Highlights:**
- **External Data Integration:** Fetch a real-world dataset from Kaggle.
- **Schema Design (SQLAlchemy + SQLite):** Define dim/fact tables using ORM models.
- **SQL Transformations:** Leverage SQL queries for data cleaning and structuring.
- **Data Quality Checks:** Validate that dimensions align with fact table keys.
- **Analytics & Insights:** Extract meaningful metrics (monthly sales, top categories).

**Author:** [Sabelo-Sabs](https://github.com/Sabelo-Sabs)

## Prerequisites
- **Kaggle Account & API Key:**  
  Obtain your `kaggle.json` from your Kaggle account and place it in `~/.kaggle/kaggle.json`:
  ```bash
  mkdir -p ~/.kaggle
  mv kaggle.json ~/.kaggle/
  chmod 600 ~/.kaggle/kaggle.json
  ```
  
- **pyenv:**  
  Install pyenv following instructions here: [pyenv installation](https://github.com/pyenv/pyenv#installation).  
  Use pyenv to install a specific Python version (e.g., 3.9.16):
  ```bash
  pyenv install 3.9.16
  pyenv local 3.9.16
  ```
  
- **pipenv:**  
  Install pipenv if you don’t already have it:
  ```bash
  pip install --user pipenv
  ```

With pyenv, we ensure a consistent Python version. With pipenv, we manage dependencies in an isolated environment.

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Sabelo-Sabs/project1_kaggle_retail_pipeline.git
   cd project1_kaggle_retail_pipeline
   ```

2. **Set Python Version via pyenv:**
   Within the project directory:
   ```bash
   pyenv local 3.9.16
   ```
   This ensures that any Python commands here use the specified version.

3. **Initialize Pipenv Environment:**
   Use pipenv to create and manage a virtual environment for dependencies:
   ```bash
   pipenv --python 3.9
   pipenv install pandas sqlalchemy kaggle jupyter
   ```
   
   *Note:* `--python 3.9` ensures pipenv uses the Python version set by pyenv. If `pyenv local 3.9.16` is already set, pipenv will pick up that version automatically.

4. **Activate the Pipenv Shell:**
   ```bash
   pipenv shell
   ```
   Now you are inside the project’s virtual environment.

5. **Run the Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```
   Open `project1_pipeline.ipynb` in your browser and run all cells in order.

## Data Source
- **Dataset:** [Global Superstore Sales Forecasting (Kaggle)](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting)

This dataset provides detailed sales information, enabling rich analytics on product performance, geographical markets, and time-based trends.

## Pipeline Steps
1. **Data Acquisition:**  
   Uses the Kaggle API to download the dataset into the `data/` directory.

2. **Staging:**  
   Loads raw CSV data into `stg_sales` within `retail_sales.db`.

3. **Schema Definition:**  
   Uses SQLAlchemy ORM to define `dim_customers`, `dim_products`, `dim_dates`, and `fact_sales` tables.

4. **Transformations & Loading:**  
   - Populate dimension tables from staging data.
   - Create indexes for performance.
   - Load the fact table by joining staging with dimension tables.

5. **Data Quality Checks:**  
   Validate record counts and ensure no orphaned dimension keys.

6. **Analytics & Insights:**  
   - Monthly revenue and profit trends.
   - Top categories by revenue and profit.

## Jupytext Commands

To convert a Jupyter notebook to a script using Jupytext:
```bash
jupytext --to py pipeline.ipynb
```

To convert a script back to a Jupyter notebook:
```bash
jupytext --to notebook pipeline.py
```

## Directory Structure
```bash
project1_kaggle_retail_pipeline/
├─ data/               
├─ project1_pipeline.ipynb
├─ README.md
├─ Pipfile
└─ Pipfile.lock
```

## Next Steps
- **Extended Validations:** Add more robust data quality checks.
- **CI/CD Integration:** Use GitHub Actions to run tests on each commit.
- **Visualization:** Incorporate charts or dashboards for clearer insight communication.
- **Parameterization:** Pass dataset paths or credentials via environment variables.
