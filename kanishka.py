#WHILE LOOP
#break statement
print("break statement")
i=1
while i<6:
    print(i)
    if i==3:
       break
    i+=1


#continue statement
print("continuous statement")    
i=0
while i < 9:
    i+=1
    if i==7:
        continue
    print(i)



#while with else
print("while with else")
i=1
while i <= 6:
    print(i)
    i+=1
else:
    print("i is no longer needed")
    
#FOR LOOP
    #without argument
print("without argument")
print("For loop")
fruits=["apple","banana","cherry"]
for x in fruits:
    print(x)

#with argument
print("with argument")
x=range(6)  
for n in x:
    print(n)

#with three arguments
print("with 3 arguments")     
x=range(2,18,2)
for n in x:
    print(n)

#USING PASS
print("USING PASS")
a=33
b=200
if a>b:
    pass
else:
    print("yes")



#MATHFUNCTIONS
    #USING MIN AND MAX
print(min(5,10,25))
print(max(5,10,25))

    #usingabsolute
print(abs(-20))
    #using maths module
import math
print(math.pi)      

x=pow(11,6)
y=pow(9,8)
print("max:",max(x,y))
print("min:",min(x,y))

#FIBONACCI SERIES
a=0
b=1
n=int(input("enter till where u want series"))
print(a)
print(b)
for i in range(0,n+1):
      sum=a+b
      a=b
      b=sum
      print(b)

#MULTIPLICATION OF TABLE
n=int(input("which table you want"))
a=int(input("till where you want"))
for i in range(1,a+1):
    print(n,"X",i,"=",n*i)
    
#QUESTION1
n=int(input("which table u want"))
b=int(input("till where u want"))
if b<=20:
    for i in range(1,b+1):
        print(n,"X",i,"=",n*i)
else:
    for i in range(1,21):
        print(n,"X",i,"=",n*i)
    print("not in range now")

#QUESTION2
n=int(input("n"))
for i in range(1,n+1):
      print("* "*i)
      i+=1

#NExt method
a=int(input("n"))
for i in range(0,a):
    for j in range(0,i+1):
        print("*",end=" ")
    print()     

#FLOYDS triangle
n=int(input("n:"))
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
        

#PALINDROME
n=input("enter string")
n=n.replace(" ","").lower()
if n==n[::-1]:
    print("yes")
else:
    print("no")
    
#ARMSTRONG NUMBERS
num=int(input("enter the 3 digit"))
power=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**power
    temp//=10

if num==sum:
    print("yes,its armstrong")
else:
    print("no,its not")


    


        

















