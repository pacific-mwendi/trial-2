import sqlite3

#creates and opens file if it does not exist
conn = sqlite3.connect("document.doc")

#used to execute SQL commands
command=conn.cursor()

#creating a table
#IF NOT EXISTS prevents errors if the table already exists.
#Creates a table called users with:
#name → text
#age → integer

command.execute("CREATE TABLE IF NOT EXISTS users (name TEXT ,age INTERGER)")

#Inserting Data

command.execute("INSERT INTO users VALUES(?,?)",("pacific",18))

#. Saving Changes
conn.commit()

#closing the connection
conn.close()