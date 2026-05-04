import sqlite3

conn= sqlite3.connect("vehicle.vh")
cursor =conn.cursor()

cursor.execute("SELECT * FROM cars  ")
rows =cursor.fetchall() 

for row in rows:
    print(row)
