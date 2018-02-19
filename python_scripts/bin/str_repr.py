#!/usr/bin/python

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        # return '__repr__ for car'
        return '{self.__class__.__name__}({self.color}, {self.mileage})'.format(self=self)
    # def __str__(self):
    #     return '__str__ for car'

my_car = Car('Red', 50)
print my_car
print repr(my_car)


#To see real difference between repr & str run it on CLI. Below is sample run from CLI.
# >>> from str_repr import Car
# __repr__ for car
# >>> my_car = Car('Red', 50)
# >>> print my_car
# __str__ for car
# >>> my_car
# __repr__ for car
# >>>
