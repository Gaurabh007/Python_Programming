import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()

# mycursor.execute("Create Database if not exists Student")    

# mycursor.execute('Create table if not exists Std (Roll_no int, S_Name varchar(30), S_Course varchar(30));')
mycursor.execute('use Student')
mycursor.execute('Create table if not exists Teachers (Id int, T_Name varchar(30), T_Course varchar(30));')
mydb.close()
