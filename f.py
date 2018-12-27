import pyodbc

conn = pyodbc.connect(
r'DRIVER={ZappySys JSON Driver};'
)
cursor = conn.cursor() 

#execute query to fetch data from API service
cursor.execute("SELECT CustomerID,CompanyName FROM value WHERE COUNTRY='Germany' WITH (SRC='http://3.16.192.70:50102/logs?msg=pull')") 
row = cursor.fetchone() 
while row: 
    print (row[0],row[0]) 
    row = cursor.fetchone()