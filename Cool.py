import sqlite3
X=sqlite3.connect("Cool2.db")
Y=X.cursor()
Y.execute('''CREATE TABLE EMPLOYEE
          (ID INT NOT NULL,
          Name TEXT NOT NULL,
          Date_Joined TEXT,
          Place TEXT,
          Salary INT,
          Age REAL)''')
Y.execute('''INSERT INTO EMPLOYEE VALUES(1,"John","25/01/2022","Kochi",60000,25),
          (2,"James","25/01/2022","EKM",63000,27),
          (3,"Johanna","27/01/2022","Trivandrum",65000,30),
          (4,"Marian","25/01/2022","Kochi",60000,25),
          (5,"Marie","25/01/2022","Kochi",68000,22)''')
Z=Y.execute("SELECT * FROM EMPLOYEE ")
for k in Z:
    print(k[1])
    print(k[2])
    print(k[3])
X.commit()
Y.close()