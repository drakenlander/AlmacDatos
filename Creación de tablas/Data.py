import pyodbc
import Credentials as c

server = c.server
database = c.database
username = c.username
password = c.password

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
conn = pyodbc.connect(connectionString, autocommit=True)
cursor = conn.cursor()

sqlFile = open('Query.sql', 'r')
queryFile = sqlFile.read()
sqlFile.close()
splitQueries = queryFile.split(';')

for q in splitQueries:
    try:
        cursor.execute(q)
    except Exception as e:
        print("Error: ", e)

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
    