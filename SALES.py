import sqlite3

 
X = sqlite3.connect('SalesDB.db')
 
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales ")


new_list=[]



for k in Y.fetchall():
  new_list.append(k[8])
  
  
print(max(new_list))  
   
 
X.commit()

Y.close()