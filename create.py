import mysql.connector as mysql

conn = mysql.connect(user="root",password="scott",host="127.0.0.1")
c=conn.cursor()
c.execute("USE python")

#c.execute("create table student(sid int ,sname varchar(30) ,slocation varchar(30))")

c.execute("insert into student values(5,'aditya','dhaisar');")
c.execute("insert into student values(5,'aditya','dhaisar');")
c.execute("insert into student values(5,'aditya','dhaisar');")
c.execute("insert into student values(5,'aditya','dhaisar');")
c.execute("insert into student values(5,'aditya','dhaisar');")
c.execute("insert into student values(5,'aditya','dhaisar');")
c.execute("insert into student values(5,'aditya','dhaisar');")
c.execute("insert into student values(5,'aditya','dhaisar');")

conn.commit()

c.execute("select * from student;")
print(c.fetchall())

conn.close()
