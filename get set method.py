class celsius:

     def __init__(self,temperature=0):

         self.set_temperature=temperature
         print("given Temperature=",self.set_temperature)
        
     def to_fahrenheit(self):
        
         return (self.temperature * 1.8)+32
    
     def get_temperature(self):
        
         return self.temperature
    
     def set_temperature(self,value):
        
       if value< -273:
           raise ValueError("Temperature below -273 not possible")
       self.temperature=value
       temperature=property(get_temperature,self.set_temperature)
         
c=celsius()
c.temperature=37

print(c.get_temperature())
print("after converting from celsius to fahrenheit:",c.to_fahrenheit())
