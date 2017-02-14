# pip install mysql-connector
# documentation: http://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
import mysql.connector

con = mysql.connector.connect(user='<USERNAME', password='<PASSWORD>', host='<HOST>', database='classicmodels')
cursor = con.cursor()

cursor.execute("SELECT firstName, lastName FROM employees")

print("Firstname\t Lastname")
print("-"*30)
for (firstName, lastName) in cursor:
    ws = 9 - len(firstName)
    if ws > 0:
        print(firstName, " " * ws, "\t", lastName)
    else:
        print(firstName, " ", "\t", lastName)


cursor.close()
con.close()