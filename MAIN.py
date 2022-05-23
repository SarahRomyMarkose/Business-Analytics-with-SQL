import sqlite3
conn=sqlite3.connect("NEWTEST2.db")
conn.execute('''CREATE TABLE SQL1 
             (ID INT, 
              Name TEXT, 
              Date_Joined TEXT, 
              Age INT, 
              Salary REAL)''')
conn.execute('''INSERT INTO SQL1 VALUES
             (1,"John","24/01/2022",21, 60000.88),
             (2,"James","24/01/2022",22,60000.99),
             (3,"Thomas","24/01/2022",23,65000.99),
             (4,"Mary","25/01/2022",21,65000.99),
             (5,"Martha","25/01/2022",23,80000.00)''')
conn.commit()
print("I have made an SQL connection")
