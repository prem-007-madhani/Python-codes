class Celsius:
    
    def __init__(self, temperature=0):

        self.temperature = temperature

    def to_fahrenheit(self):

        return (self.temperature * 1.8) + 32

    def get_temperature(self):

        return self.temperature
    
    def set_temperature(self, value):

        if value < -273:
            raise ValueError("Temperature below -273 not possible ")
        self.temperature = value
        temperature = property(self.get_temperature, self.set_temperature)

c = Celsius()
c.set_temperature(37)

print("Given temperature", c.get_temperature())
print("After converting from celsius to fahrenheit: ", c.to_fahrenheit())
