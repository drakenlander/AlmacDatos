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
