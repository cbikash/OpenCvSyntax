import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root", password="")



if mydb:
    print("connection is successful")
else:
    print("Error")

mycursor= mydb.cursor()
mycursor.execute("Show databases")

for db in mycursor:
    print(db)