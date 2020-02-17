import mysql.connector as mysql

conn = mysql.connect(user="root",password = "scott" , host = "127.0.0.1")

c.conn.cursor()
e.execute("use python")
c.execute("show databases")

print(c.fetchall())

c.execute("drop database python")
c.execute("show databases")

print(c.fetchall())

c.conn.close()
