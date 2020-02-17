import mysql.connector as mysql

conn = mysql.connect(user = "root" ,password="scott" ,host="127.0.0.1")
c=conn.cursor()
c.execute("use python")
c.execute("show tables from python")

print(c.fetchall())

c.execute("drop table  student")
c.execute("show table from python")

print(c.fetchall())

conn.close()
