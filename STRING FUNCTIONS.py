lpu="I am a good student"

'''#printing"am a good"
print(lpu[2:11])

#printing "ood stude"
print(lpu[-11:-2])

#printing in reverse order
print(lpu[::-1])

#concatenating two strings
cse="cse is branch there in btech"
print(lpu + cse)

#using replace function
x=lpu.replace("good","great")
print(x)

#using title function(it will capitalize first letter  of each word)
y=lpu.title()
print(y)

#using count function
#note:- count is used for specific character whereas len is used for whole string
print(lpu.count("g"))
print(len(lpu))

#using centre(it will add the given character at first and last of the string in such way that length of string becomes the number given by user
print(lpu.center(26,"K"))

#using split function (it will separate each word os string as elements of the list)
z=lpu.split()
print(z)

#using join function(it will add the specific character after each and every element)
a="@".join(lpu)
print(a)

#QUES
str="how are you?"
print(str[4:7])
print(str[2:5])
print(str[8:11])
print(str[-2:-5:-1])
print(str[8:])

#QUES1
string=input("enter thr string")
print(string[0:2])
print(string[-1:-3:-1])
if len(string)<10:
    print(string)

string=input("enter the string")
n=int(input("enter the number"))
print(n*string)

#using functions to string lpu
print(lpu.capitalize()) #frst letter capitalize
print(lpu.upper()) #whole capitalize
print(lpu.lower()) #string in lower case
print(lpu.title()) #capitalise frst letter of eacch word
print(lpu.swapcase()) #reverse the case
print(lpu.split()) #converts into list
print(lpu.center(25,"$")) #create string of length = width and will add charachter at start and end.
print(lpu.count("a")) #counts no of word
print(lpu.replace("good","best")) #replace specific word
print("@".join(lpu)) #joining char to each element
a=input("enter the string")
print(a.isalpha())
print(a.islower())
print(a.isupper())
print(a.isalnum()) #should contain both alphabets and number
print(a.isdigit())
print(a.isspace()) #only spaces
print(a.istitle())
x=input("str1: ")
y=input("str2: ")
if len(x)==1 and len(y)==1:
    print("null")
else:
    print("output:",x[1:]+y)


data=input("str: ")
print("type of data",type(data))
print(data.split())'''

a=[1,2,3]
b=[1,2,3]
print(a==b)
print(a is b)


#CLONING LIST
c=a[:] 
print(c)
print(c is a)

d=list(a)
d[0]=100
print(d)
print(d is a)

list=["red","yellow","orange"]
k=list.pop()
print(k)

j=list.pop(-1)
print(j)

b.clear()
print(b)

a.append(5)
print(a)
a.insert(0,0)
print(a)

list1=[1,45,64,98,87]
list2=sorted(list1)
print(list2)






































































































