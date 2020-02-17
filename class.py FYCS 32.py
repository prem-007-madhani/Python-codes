class demo:

    a=0
    b=0

    def __init__(self):
        self.a=5
        self.b=10

    def display (self):
        print("a=",self.a)
        print("b=",self.b)

class demo1:

    x = 0
    y = 0

    def data(self, demo):
        self.x = demo.a
        self.y = demo.b

    def display1(self):
        print("x=", self.x)
        print("y=", self.y)

d1 = demo()
d1.display()
d2 = demo1()
d2.data(d1)
d2.display1()

