import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
# mycursor.execute('Insert into Student.Std values(1001,"Gaurabh","Data Science");')
# mycursor.execute('Insert into Student.Std values(1002,"Harsh","Java with DSA");')
# mycursor.execute('Insert into Student.Std values(1003,"Chirag","Python with DSA");')
mydb.commit()       #to make the changes Permanent inside my database

mycursor.execute('Insert into Student.Teachers values(01,"Hitesh","Web Development");')
mycursor.execute('Insert into Student.Teachers values(02,"Krish","Data Science");')
mydb.commit()

# mycursor.execute('Select * from Student.Std')
# for i in mycursor.fetchall():       #to see all the records
#   print(i)
# mydb.close()