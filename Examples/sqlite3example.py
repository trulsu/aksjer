import sqlite3

# Create a database in ram
# db = sqlite3.connect(':memory:')

# Create or open a database file called mydb with a SQLite3 DB
db = sqlite3.connect('data/mydb')

# Create a table (data types: INTEGER, REAL, TEXT, BLOB)
cursor = db.cursor()
cursor.execute('''
  CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,
  					 name TEXT,
  					 phone TEXT,
  					 email TEXT unique,
  					 password TEXT)
''')

# Insert some data
name = 'Andres'
phone = '3366858'
email = 'user@example.com'
password = '12345'

cursor.execute('''INSERT INTO users(name,phone,email,password) VALUES(?,?,?,?)''',
	(name,phone,email,password))

# Fetch the data
cursor.execute('''SELECT name,email,phone FROM users''')
user = cursor.fetchone()
print user

# Close the database
db.close()
