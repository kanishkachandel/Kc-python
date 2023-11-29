#ques1

class Animal:
    def eat(self):
        print("I can eat")
class Dog(Animal):
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)

s1=Dog(input('name'))
s1.eat()
s1.display()

#ques2

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say_hello(self):
        print("hello my name is ",self.name)
        print("hello my age is",self.age)
class student(person):
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
class student(person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade
    def say_hello(self):
        super().say_hello()
        print(f"I am student in grade {self.grade}")
person=person("John",30)
person.say_hello()
student=student("radha",12,14)
student.say_hello

#ques3

class employee:
    def hello(self,name=None):
        if name is not None:
            print(f"hello {name}!")
        else:
            print("hello!")
emp=employee()
namebyuser=input("Enter the name")
emp.hello(namebyuser)
emp.hello()


#Ques5
import math
class circle:
    def parameter(self,r):
        self.r=r
        print(2*math.pi*self.r)
    def area(self,r):
        self.r=r
        print(math.pi*r*r)
r=int(input("radius: "))
radius=circle()
radius.parameter(r)
radius.area(r)

#QUES:_ WAP to create a person class includes attributes like name,country and dob implement a method to determine person's age
from datetime import date
class Person:
  def __init__(self,name,country,dob):
    self.name=name
    self.country=country
    self.dob=dob
  def cal(self):
    today=date.today()
    age=today.year - self.dob.year
    print("Age: ",age)
name=input("Enter ur name: ")
country=input("Enter ur country: ")
year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
dob = date(year, month, day)
d1=Person(name,country,dob)
d1.cal()

#QUES
class calculator:
    def add(self,a,b):
        self.a=a
        self.b=b
        print("sum: ",self.a+self.b)
    def sub(self,a,b):
        print("sub: ",self.a-self.b)
    def mul(self,a,b):
        print("mul: ",self.a*self.b)
    def div(self,a,b):
        print("div: ",self.a/self.b)
a=int(input("enter frst no: "))
b=int(input("enter second no: "))
obj=calculator()
obj.add(a,b)
obj.sub(a,b)
obj.mul(a,b)
obj.div(a,b)







































