'''FUNCTIONS
def demo(name,age):
    print(name,age)
demo("Raj",25)

#SUM
def sum_function(a,b):
    print(a+b)
sum_function(10,15)
sum_function(20,23)

#FOUR FUNCTIONS
def sum_function(x,y):
    return(a+b)
def sub_function(x,y):
    return(a-b)
a=int(input("a: "))
b=int(input("b: "))
addition=sum_function(a,b)
subtraction=sub_function(a,b)
print("addition",addition)
print("subtraction",subtraction)

#QUES1
def add(num1,num2):
    num3=num1+num2
    return num3
num1,num2=5,15
ans=add(num1,num2)
print(f'addition of {num1} and {num2} reults {ans}')

#QUES2
def sayhello(username):
    greet="hello"
    print(greet + " " + username)

users=["ram","sham","geeta"]
for name in users:
    sayhello(name)


def greet(name,dept):
    print(f"hi {name}")
    print(f"are you from {dept}")

greet(dept="cse",name="ram")

def my_country(country="India"):
    print("I am from",country)
my_country()
my_country("England")


def sum(a,b=100):
    c=a+b
    print(c)
sum(50)

greet(name="ashima",dept="cse")


#ARBITRARY ARGUMENTS
def my_function(*kids):
    print("The youngest child is " +kids[0])

my_function("ram","sham","radha")'''

def mysum(*args):
    return sum(args)
print(mysum(1,2,3,4,5))

def mymax(*args):
    print (max(args))
    print(min(args))

mymax(10,20,30,40)

function= lambda x,y:x+y
a=int(input(" enter first number"))
b=int(input(" enter second number"))
print(function(a,b))


#MAP FUNCTION
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
def addinglist(a,b):
    return a+b
print(list(map(addinglist,list1,list2)))


print(list(map(lambda x: x**2,list1)))

#FILTER FUNCTION
a=[1,4,6,10]
b=[1,10,20,30,40]
z=list(filter(lambda x:x in a,b))
print(z)

#GLOBAL AND LOCAL VARIABLE
msg="Hello"
def greet():
    greet="good mrng"
    print("local",greet)
    print("local",msg)
greet()
print("global",msg)

x=4
print(x)

def hello():
    x=5
    print("local x is",x)
    print("hello there")
print("global x is",x)
hello()
print("global functn is",x)


#COMPOSITION OF FUNCTIONS
def add(x):
    return x+2
def multiply(x):
    return x*5
print(multiply(add(5)))









