class student:

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = rollno

    def display(self):
        print("name: ",self.name)
        print("roll_no: ",self.roll_no)

name = str(input("please enter your name: "))
rollno = int(input("please enter your roll no: "))
s1 = student(name,rollno)
s1.display()
