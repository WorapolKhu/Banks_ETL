# Acquiring and Processing Information on the World's Largest Banks
This project involves real-world data to perform Extraction, Transformation, and Loading (ETL) operations. I will create a code to compile a list of the top 10 largest banks in the world ranked by market capitalization in USD and convert the data into GBP, EUR, and INR. The data is then to be saved locally in CSV format and as a database table.

## Project Scenario
I have been hired as a data engineer by research organization. My boss has asked me to create a code that can be used to compile the list of the top 10 largest banks in the world ranked by market capitalization in billion USD. Further, the data needs to be transformed and stored in GBP, EUR and INR as well, in accordance with the exchange rate information that has been made available to you as a CSV file. The processed information table is to be saved locally in a CSV format and as a database table.

My job is to create an automated system to generate this information so that the same can be executed in every financial quarter to prepare the report.

## Requirements
- Python 3.11
- Libraries: requests, bs4, pandas, sqlite3, numpy, datetime
- Data URL: [Archived List of Largest Banks](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv)

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

## Output 
- CSV File: `./Largest_banks_data.csv`
- Database: `Banks.db`
- Table: `Largest_banks`
- Log File: `code_log.txt`