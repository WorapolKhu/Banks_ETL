# Code for ETL operations on Country-GDP data

# Importing the required libraries
import requests
import sqlite3
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from datetime import datetime

def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''
    
    # Year-Monthname-Day-Hours:Minutes:Seconds
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    # get current timestamp
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file,"a") as f:
        f.write(timestamp + ' : ' + message + '\n')

def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''

    html_page = requests.get(url).text
    data = BeautifulSoup(html_page, 'html.parser')

    df = pd.DataFrame(columns=table_attribs)

    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr')

    for row in rows:
        col = row.find_all('td')
        if len(col) !=0:
            data_dict = {"Name": col[1].text.strip(),
                        "MC_USD_Billion": float(col[2].text.strip())}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)

    return df

def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''

    df_exchange = pd.read_csv('exchange_rate.csv', index_col=0)

    df['MC_EUR_Billion'] = np.round(df['MC_USD_Billion'] * df_exchange.loc['EUR','Rate'], 2)
    df['MC_GBP_Billion'] = np.round(df['MC_USD_Billion'] * df_exchange.loc['GBP','Rate'], 2)
    df['MC_INR_Billion'] = np.round(df['MC_USD_Billion'] * df_exchange.loc['INR','Rate'], 2)

    return df

def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''

    df.to_csv(csv_path)

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''

    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_queries(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''

    for query in query_statement:
        print(query)
        print(pd.read_sql(query, sql_connection), '\n')

''' Here, you define the required entities and call the relevant
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''

url = "https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks"
db_name = 'Banks.db'
table_name = 'Largest_banks'
csv_path = './Largest_banks_data.csv'
log_file = "code_log.txt"
table_attribs = ['Name', 'MC_USD_Billion']
query_statement = [
        'SELECT * FROM Largest_banks',
        'SELECT AVG(MC_GBP_Billion) FROM Largest_banks',
        'SELECT Name from Largest_banks LIMIT 5'
    ]

log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url, table_attribs)
log_progress('Data extraction complete. Initaiting Transormation process')

df = transform(df, csv_path)
log_progress('Data transformation complete. Initiating loading processs')

load_to_csv(df, csv_path)
log_progress('Data saved to CSV file')

sql_connection = sqlite3.connect(db_name)
log_progress('SQL Connection initiated')

load_to_db(df, sql_connection, table_name)
log_progress('Data loaded to Database as table. Running the query')

run_queries(query_statement, sql_connection)
log_progress('Process Complete')

sql_connection.close()
log_progress('Server Connection closed')