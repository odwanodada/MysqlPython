import mysql.connector

mysql_day = mysql.connector.connect(user='lifechoices',password='@Lifechoices1234',host='localhost',database='Hospital',
                                   auth_plugin='mysql_native_password')
mycursor = mysql_day.cursor()
xy = mycursor.execute("Select * from Dentist")
for i in mycursor:
    print(i)
