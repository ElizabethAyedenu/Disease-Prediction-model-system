import mysql.connector
db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="pharmacist",
    database="hygieia_disease_management"
)
if db.is_connected==False:
    print("not connected")
else:
    print ("connected")
mycursor=db.cursor()
mycursor.execute("SELECT * FROM disease")
for x in mycursor:
    print(x)