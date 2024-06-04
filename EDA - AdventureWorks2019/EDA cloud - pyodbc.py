import pyodbc
server = '.'
database = 'AdventureWorks2019'
username = 'sa'
password = '123'

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
conn = pyodbc.connect(connectionString)
cursor = conn.cursor()

q = "SELECT TABLE_NAME FROM AWLanding.INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'"
cursor.execute(q)
tables = cursor.fetchall()

for table in tables:
    print(table)

    cols = "SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = ?"
    cursor.execute(cols, table)
    columns = cursor.fetchall()

    for column in columns:
        print('\t', column)
    
    print()