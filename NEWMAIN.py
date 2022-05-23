import sqlite3
X=sqlite3.connect("HELLO7.db")
X.execute('''CREATE TABLE SQL2
          (RollNumber INT, 
           Name TEXT, 
           EMAIL TEXT, 
           PhoneNumber INT, 
           Place TEXT)''')
X.execute('''INSERT INTO SQL2 VALUES
          (1,"John","john@gmail.com",123456789,"Alappuzha"),
          (2,"James","james@gmail.com",246813579,"Idukki"),
          (3,"Thomas","thomas@gmail.com",135792468,"Trivandrum"),
          (4,"Mary","mary@gmail.com",2143658790,"Kottayam"),
          (5,"Martha","martha@gmail.com",765432109,"EKM")''')
X.commit()
print("I have made an SQL Connection")