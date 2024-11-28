# ETL Batch Processing - FTDE - Mini Project 1 

This project demonstrates a simple implementation of ETL Batch Processing using Python. It is implements the Extract, Transform, Load (ETL) process to automate data workflows and load transformed data into a Data Warehouse (DWH). The project automates the ETL process in batches, supports PostgreSQL databases, and leverages powerful Python libraries like Pandas, SQLAlchemy, and psycopg2 to handle data processing efficiently. 


## 🚀 Key Features
- **Database Connectivity**: Supports secure connections to both source databases and the DWH.
- **Data Extraction**: Data is extracted from the source database using custom SQL queries provided in the query/query.sql file.
- **Data Transformation**: Data is manipulated and transformed using Pandas, allowing for efficient cleaning and preparation of data before ingestion into the DWH (Flexible design to support additional transformation steps as required).
- **Data Ingestion**: Transformed data is ingested into the DWH using SQLAlchemy for seamless integration with PostgreSQL.


## 🛠️ Technologies Used
- Python 3.12
- Pandas
- SQLAlchemy
- SQLParse
  

## 📂 Project Structure
- query/ 
    - query.sql  ->  SQL queries for extracting data from the source database
    - dwh_design.sql   ->  SQL script for defining the schema and tables in the Data Warehouse
- main.py   ->  The main Python script for running the ETL process
- connection.py   ->  Module for managing secure database connections
- requirements.txt   ->  List of Python dependencies required for the project


### Jalankan script berikut untuk menginstall dependencies
```
pip install -r requirements.txt
```


## ⚙️ Configuration
### 1.Create a `config.json` File
This file contains credentials for connecting to the source database and DWH. It is excluded from version control to maintain security.
Example format:
```
{
    "marketplace_prod": {
        "host": "",
        "db": "",
        "user": "",
        "password": "",
        "port": ""
    },
    "dwh": {
        "host": "",
        "db": "",
        "user": "",
        "password": "",
        "port": ""
    }
}
```

### 2. Prepare SQL Files
- `query/query.sql`: Contains SQL queries to extract data from the source database.
- `query/dwh_design.sql`: Contains SQL scripts for creating the schema and tables in the Data Warehouse.
 

## How To Run
### 1. Clone the repository
```
git clone https://github.com/Mafarasya/Mini-project-batch-processing.git
cd Mini-project-batch-processing
```
### 2.  Install Dependencies
```
pip install -r requirements.txt
```
### 3. Execute the ETL Script
```
python main.py
```


## 💡 Learning Outcomes
This project is more than just building an ETL pipeline—it’s about understanding the core concepts of data engineering. Through this project, you will:
- Learn how to connect to databases securely and manage credentials effectively.
- Gain experience in extracting, transforming, and loading data using industry-standard tools like Pandas and SQLAlchemy.
- Understand the importance of data quality and how to clean and validate data before ingestion.
- Develop modular Python scripts that are easy to scale and maintain.
- Explore the fundamentals of designing a data warehouse schema and implementing it in SQL.
This mini-project is a stepping stone to mastering ETL workflows and preparing for real-world data engineering tasks!

