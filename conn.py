import mysql.connector as mysql

conn = mysql.connect(user="root",password = "scott" , host = "127.0.0.1")

c=conn.cursor()
c.execute("use python")
c.execute("select * from student")

print ("data before updating")
print =( c.fetchall())

c.execute("update student set sname = 'johnwhick' where sid = 1" )
c.execute("update student set sname = 'prem' where sid =2")
c.execute("select * from student")

print("data after updating")
print(c.fetchall())

row = c.fetchall()

print(row[0][1])

conn.close()
