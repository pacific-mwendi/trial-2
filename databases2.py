import sqlite3

conn = sqlite3.connect("vehicle.vh")

cursor =conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS cars (name TEXT , year INTEGER) ")

cursor.execute("INSERT INTO cars VALUES(?,?)",("toyota",2024))

conn.commit()
conn.close()


