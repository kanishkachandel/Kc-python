lpu="I am a good student"

#printing"am a good"
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

#using title function(
y=lpu.title()

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
