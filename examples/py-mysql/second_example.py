from database import db


mysql = db.Db()
c = mysql.query("SELECT firstName, lastName FROM employees")

for row in c:
    print(row[0], row[1])

mysql.close()