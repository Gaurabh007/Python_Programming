import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute('Select * from Student.Std')
for i in mycursor.fetchall():       #to see all the records
  print(i)


mycursor.execute('Select * from Student.Teachers')
for i in mycursor.fetchall():       #to see all the records
  print(i)
