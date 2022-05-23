import sqlite3
X=sqlite3.connect("FetchData1.db")
Y=X.cursor()
Y.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEE
          (ID INT NOT NULL,
          Name TEXT NOT NULL,
          Date_Joined TEXT,
          Place TEXT,
          Salary INT,
          Age REAL)''')
Y.execute("SELECT * FROM EMPLOYEE WHERE Name='John'")
print(Y.fetchall())
X.commit()
Y.close()
