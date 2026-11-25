#tuple is secured data type
#to check the boolean value of 0
"""a=0
print(bool(a))"""

#use of dictionary
"""a={"a":10,"a":20}
print(a)"""

#to add new key value pair in dictionary
"""a["c"]=15
print(a)"""

#to access the value of a key in dictionary
"""a={"a":[10,20,30],"b":[40,50,60]}
print(a['a'][1])"""

#left to right slicing
"""a="hello"
print(a[2:4])
print(a[2:3+1])    
print(a[-3:-2+1])    
print(a[2:3])     
print(a[-3:-1])"""

"""a="good morning"
print(a[-2:-6])
print(a[7:11])"""

#right to left slicing
"""a="hello"
print(a[1:2-1])
print(a[-1::-1]) """  #reversing the string

#to get mng using slicing(left to right slicing)
"""a="good morning"
print(a[5::3]) 
print(a[5:11+1:3])
print(a[-7::3])"""

#right to left slicing
"""print(a[-2:-8-1:-3]) 
print(a[10:4-1:3])"""

"""a=input("enter")
print(a)
b=int(input("enter"))
print(b)"""

"""c=eval(input("enter"))
print(c)"""

"""a=int(input("enter"))
print(a)
b=float(input("enter"))
print(b)"""
"""c=bool(input("enter"))
print(c)"""

#using if else statement
#to check if the number is even
"""a=int(input("enter"))
if a%2==0:
    print("even")"""

#to check if length of list is 5
#a=[1,2,3,4,5]
"""a=eval(input("enter a list: "))
if len(a)==5:
    print("length is 5")
else:
   print("length is not 5")"""

#to find ascii value of a character
"""print(ord('A'))
print(ord('a'))"""

#to find character of an ascii value
"""print(chr(65))
print(chr(97))"""

#using else if statement
#to check if the character is uppercase or lowercase
"""ch=input("enter a character: ")
if ch==ch.upper():
    print("uppercase")
elif ch==ch.lower():
    print("lowercase")
else:
    print("neither uppercase nor lowercase") """   

    #or
"""ch=input("enter a character: ")
if 'A'<=ch<='Z':
    print("uppercase")
elif 'a'<=ch<='z':
    print("lowercase")  
else:
    print("neither uppercase nor lowercase")"""

#using nested if statement
#to check if the username and password is correct
"""un=input("enter username: ")
if un=="kushi_v_bhat":
    print("username is correct")
    pw=input("enter password: ")
    if pw=="kushi@123":
        print("password is correct")
    else:
        print("password is incorrect")
else:
    print("username is incorrect")"""

#login program using nested if statement
"""username="kushi_v_bhat"
password="kushi@123"
un=input("enter username: ")
if un==username:
    pw=input("enter password: ")
    if pw==password:
        print("login successful")
    else:
        print("password is incorrect")
else:
    print("username is incorrect")"""

#using while loop
#printing numbers from 1 to 100
"""i=1
while i<=100:
    print(i)
    i=i+1"""

#to print even numbers from 1 to 100
"""i=1
while i<=100:
    if i%2==0:
        print(i)
    i=i+1"""

#to print odd numbers from 1 to 100
"""i=1
while i<=100:
    if i%2!=0:
        print(i)
    i=i+1"""

#reversing a number without using typecasting but by using division method
"""num=int(input("enter a number: "))
rev=0
while num>0:
    ld=num%10
    num=num//10
    rev=rev*10+ld
print("reversed number is: ",rev)"""

#using for loop(automated loop)
#to print numbers from 1 to 100
"""for i in range(1,101):
    print(i)"""

#to print even numbers from 1 to 100 using for loop
"""for i in range(1,50):
    if i%2==0:
        print(i)"""

"""l=[10,20,30]
for i in l:
    print(i)"""

#to check character is uppercase or lowercase using for loop
"""for i in range(5):
    ch=input("enter a character: ")
    if 'A'<=ch<='Z':
        print("uppercase")
    elif 'a'<=ch<='z':
        print("lowercase")  
    else:
        print("neither uppercase nor lowercase")"""

#reverse a number using for loop without slicing
"""num=input("enter a number: ")
rev=''
for i in num:
    rev=i+rev
print("reversed number is: ",rev)"""

#using nested for loop
#to print a 5*5 matrix of *
"""for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()"""

#to print a 5*5 matrix of * in diagonal
"""for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()"""

#functions
#4ways to define a function
#1.with arguments and with return
"""def convert(a):
    out=""
    for i in a:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32) 
        else:
            out+=i
    return out #returns the output address it won't display the output
print(convert(input("enter a string: ")))"""

#2.without arguments and without return
"""def convert():
    a=input("enter a string: ")
    out=""
    for i in a:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32) 
        else:
            out+=i
    print(out) #displays the output
convert()"""

#3.with arguments and without return
"""def convert(a):
    out=""
    for i in a:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32) 
        else:
            out+=i
    print(out) #displays the output
convert(input("enter a string: "))"""

#4.without arguments and with return
"""def convert():
    a=input("enter a string: ")
    out=""
    for i in a:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32) 
        else:
            out+=i
    return out #returns the output address it won't display the output
print(convert())"""

#classes and objects
#to create a class
"""class college:
    cname="gpln"
    cloc="hoodi" 
college.cloc="krpuram" 
s1=college()
print(s1.cname,s1.cloc)
#or
print(college.cname,college.cloc)"""
"""any changes made to class will affect object but if we
change object it wont affect class"""
"""s1.cloc="whitefield"
print(s1.cloc)
print (college.cloc)"""

"""class college:
    cname="gpln"
    cloc="hoodi"

s1=college()
s1.sname="arfa"
s1.phone="123456789"

s2=college()
s2.sname="kushi"
s2.phone="7795543329"

print(s1.cloc)
s1.cloc="krpuram"
print('after changing')
print(s1.cloc)

print(s2.cloc)
print (college.cloc)"""

#init constructor
"""class college:
    def __init__(self,name,phone,usn):
        self.name=name
        self.phone=phone
        self.usn=usn
s1=college('kushi',7795543329,'1GD25CS065')
s2=college('arfa',123456789,'1GD25CS067')
print(s1.name,s1.phone,s1.usn)
print(s2.name,s2.phone,s2.usn)"""
#or
"""class college:
    def __init__(self,name,phone,usn):
        self.name=name
        self.phone=phone
        self.usn=usn
    def display(self):
        print(self.name,self.phone,self.usn)
s1=college('kushi',7795543329,'1GD25CS065')
s2=college('arfa',123456789,'1GD25CS067')
s1.display()
s2.display()"""


