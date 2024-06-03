# Acquiring and Processing Information on the World's Largest Banks
This project involves real-world data to perform Extraction, Transformation, and Loading (ETL) operations. I will create a code to compile a list of the top 10 largest banks in the world ranked by market capitalization in USD and convert the data into GBP, EUR, and INR. The data is then to be saved locally in CSV format and as a database table.

## Project Scenario
I have been hired as a data engineer by research organization. My boss has asked me to create a code that can be used to compile the list of the top 10 largest banks in the world ranked by market capitalization in billion USD. Further, the data needs to be transformed and stored in GBP, EUR and INR as well, in accordance with the exchange rate information that has been made available to you as a CSV file. The processed information table is to be saved locally in a CSV format and as a database table.

My job is to create an automated system to generate this information so that the same can be executed in every financial quarter to prepare the report.

## Objectives
- Use Webscraping techniques to extract information from any website as per requirement.
- Use Pandas data frames and dictionaries to transform data as per requirement.
- Load the processed information to CSV files and as Database tables
- Query the database tables using SQLite3 and pandas libraries
- Log the progress of the code properly

## Requirements
- Python 3.11
- Libraries: requests, bs4, pandas, sqlite3, numpy, datetime
- Data Source: [Archived List of Largest Banks](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv)
  ![Task_2a_extract](https://github.com/WorapolKhu/Banks_ETL/assets/93505768/9043cbee-0123-4c79-bb15-b0a937cc7eac)

## Installation
- Required libraries: `requests`, `bs4`, `pandas`, `sqlite3`, `numpy`, `datetime`.
- Install the required libraries using:
```
python3.11 -m pip install <library_name>
```
- Download the required exchange rate file using the terminal command:
```bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv
```
## Usage
Run the script `banks_project.py` to perform the ETL operations and generate the report.

## Project tasks
1. Log progress at different stages.
2. Extract tabular information from the provided URL.
3. Transform the data based on exchange rates.
4. Load the transformed data to a CSV file and SQL database.
5. Run queries on the database table.
6. Verify log entries.

## Process Steps
### Extraction of data
![Task_2c_extract](https://github.com/WorapolKhu/Banks_ETL/assets/93505768/2bd62848-abef-4746-98a1-fff56c6613b9)

### Transformation of data
![Task_3b_tranform](https://github.com/WorapolKhu/Banks_ETL/assets/93505768/9060c97e-dc43-41ce-8df9-936f220c6089)

### Loading to CSV
![Task_4_CSV](https://github.com/WorapolKhu/Banks_ETL/assets/93505768/3574dadc-3578-4a21-b10a-0ad8d784ba32)

## Results 
- CSV File: `./Largest_banks_data.csv`
- Run queries on Database
  1. Print the contents of the entire table
  Query statement:
  ```
  SELECT * FROM Largest_banks
  ```
  2. Print the average market capitalization of all the banks in Billion USD.
  Query statement:
  ```
  SELECT AVG(MC_GBP_Billion) FROM Largest_banks
  ```
  3. Print only the names of the top 5 banks
  Query statement:
  ```
  SELECT Name from Largest_banks LIMIT 5
  ```
  ![Task_6_SQL](https://github.com/WorapolKhu/Banks_ETL/assets/93505768/ae8be97a-cf88-4764-aa93-4febd4ec6eb1)
- Log Logged ETL Process: `code_log.txt`
  ![Task_7_log_content](https://github.com/WorapolKhu/Banks_ETL/assets/93505768/d88a680c-1857-482a-915b-271ef5ff32e2)
