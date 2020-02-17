class shapes:

    def __init__(self):
        self.s = int(input("Enter side of Square: "))
        self.l = int(input("Enter length of Rectangle: "))
        self.b = int(input("Enter Breadth of Rectangle: "))

    def square(self):
        print("\nArea of Square: ",self.s*self.s)
        print("perimeter of Square: ",4*self.s)

    def rectangle(self):
        print("\nArea of Rectangle: ",self.l*self.b)
        print("perimeter of rectangle: ",2*(self.l+self.b))

s=shapes()
s.square()
s.rectangle()

