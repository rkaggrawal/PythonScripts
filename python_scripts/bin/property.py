#/usr/bin/python


#Method 1
'''
class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

man = Celsius()
print man.temperature
man.temperature = 37
print man.temperature
print man.to_fahrenheit()
'''

'''
#Method 2
class Celsius:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)
    
    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32
    
    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


man = Celsius()
print man.get_temperature()
man.set_temperature(37)
print man.get_temperature()
print man.to_fahrenheit()
'''

'''
# Method 3
class Celsius:
    def __init__(self, temperature = 0):
  	self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
   
    def get_temperature(self):
        print("Getting Value")
	return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting Value")
        self._temperature = value

    temperature = property(get_temperature,set_temperature)


man = Celsius()
print man.temperature
man.temperature = 37
print man.temperature
print man.to_fahrenheit()
'''
#Method 4
class Celsius(object):
    def __init__(self, temperature=0):
        self.temperature = temperature
    
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value


man = Celsius()
print man.temperature
man.temperature = 37
print man.temperature
print man.to_fahrenheit()





#man.temperature = 37
#print man.temperature
#print man.to_fahrenheit  #By using @property we call class method as a variable. No need to mention  man.to_fahrehheit().
#print man.__dict__
#print Celsius.__dict__
#print "Class name is: ",Celsius.__name__
