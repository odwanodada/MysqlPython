import mysql.connector

mydb = mysql.connector.connect(user='lifechoices', passwd='@Lifechoices1234', host='127.0.0.1', database='Hospital', auth_plugin='mysql_native_password')

mycursor = mydb.cursor()

sql = "INSERT INTO login VALUES (%s, %s)" #insert
value = ("Siphe","Siphe2021")
mycursor.execute(sql, value)

mydb.commit()



#mycursor.execute('CREATE TABLE login (Username VARCHAR(15) not null, Password VARCHAR(10) not null, primary key(Password))')

#mycursor.execute("Show tables")
#for x in mycursor:
 #   print(x)



import mysql.connector

Username = input("Enter Username:")
Password = input("Enter Password")
mydb = mysql.connector.connect(user='lifechoices', passwd='@Lifechoices1234', host='127.0.0.1', database='Hospital', auth_plugin='mysql_native_password')

mycursor = mydb.cursor()

sql = "insert into login(Username, Password) values(%s, %s)"
val = (Username, Password)


try:
    mycursor.execute(sql, val)

    mydb.commit()

except:

    mydb.rollback()
print(mycursor.rowcount, "record inserted!")
mydb.close()


