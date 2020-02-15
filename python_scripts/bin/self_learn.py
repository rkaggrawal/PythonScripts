#!/usr/bin/python

class Student:
    collegeName = 'IIT Delhi'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def student_info(self):
        print("Name : ", self.name, " Age : ",self.age)

stu1 = Student("Rahul", 25)
stu1.student_info()
print (stu1.collegeName)

stu2 = Student("Tyson", 80)
stu2.student_info()
stu2.collegeName = 'IIT Chennai'
print (stu2.collegeName)

print (stu1.collegeName) # It will still point to old data

