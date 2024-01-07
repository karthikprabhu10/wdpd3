import mysql.connector
# Establishing a connection to MySQL server
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456"  # Corrected the syntax error here
)
# Creating a cursor object to interact with the database
cursor_object = database.cursor()
# Executing the SQL query to create a database named 'students'
cursor_object.execute("CREATE DATABASE students7")

