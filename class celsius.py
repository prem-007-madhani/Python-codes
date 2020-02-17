class celsius:

    def __init__(self,temperature=0):
        self.temperature=temperature

    def to_fahrenheit(self):
        return (self.temperature*1.8)+32

man=celsius(25)

print(man.to_fahrenheit())
