import mysql.connector

# Establishing connection to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pharmacy_db"
)

# Creating a cursor object
mycursor = mydb.cursor()
