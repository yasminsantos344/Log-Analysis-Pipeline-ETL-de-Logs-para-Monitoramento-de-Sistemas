# About
This is a simple project created to study how an ETL pipeline works using log data.

The pipeline reads raw logs, processes the data, and prepares it for analysis.

---

## Pipeline
The project is divided into three main steps:

- Extract (`extract.py`)

Reads the log data from a file

- Transform (`transform.py`)
  
Cleans and structures the data (date, status code, URL, etc.)

- Load / Analysis (`analytics.py`)
  
Runs queries and aggregations on the processed data

---

## Files

```
analytics.py     # queries and aggregations
config.py        # configuration (database, etc.)
database.py      # database connection
extract.py       # data extraction
transform.py     # data transformation
log.txt          # sample log data
main.py          # pipeline execution
README.md

```

---
## Technologies

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-00758F?style=for-the-badge&logo=mysql&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-000000?style=for-the-badge&logo=postgresql&logoColor=white)

---

## Purpose
This project was built to practice:

- ETL concepts
- log processing
- basic data analysis with SQL
