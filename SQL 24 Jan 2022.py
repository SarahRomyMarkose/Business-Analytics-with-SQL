import sqlite3
conn=sqlite3.connect("24Jan2022DataBase.db")
conn.execute('''CREATE TABLE SQL24Jan2022 
             (ID INT, Name TEXT)''')
print("I have made an SQL connection")
