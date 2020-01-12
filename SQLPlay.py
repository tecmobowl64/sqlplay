# Import OS and sqlite for the program to use
 import sqlite3
 import os

 # Database connection
 def create_connection(db_file):
     try:
         conn = sqlite3.connect(db_file)
         return conn
     except Exception as e:
         print(e)
     return None
