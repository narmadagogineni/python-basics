print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.''')

---------------------------------------------
# playsound
from playsound import playsound
playsound('C:\\Users\\Narmada G\\OneDrive\\Desktop\\python codes 2\\tiktok.mp3')
--------------------------------------------------------------------------------

#list directory
import os
print(os.listdir())

--------------------------------------------------------------------
# single line comment
'''hello this is multiline comment
you can write the comment a long as you want
it wont be sisplayed in the output'''
--------------------------------------------------------------
#add two num
a = 35
b = 20
print("The sum of a and b is", a+b)
----------------------------------------------------
#remainder
c = 45
d = 12
print("The remainder when divided by c and d", c%d)

-----------------------------------------------------
#type of input function
a = input("enter a number:")
print(a)
print(type(a)) 
----------------------------------
#comparisono operator
a = 34
b = 80
print(a > b)
--------------------------------------------
# avg of 2 num
a = int(input("Ener num1:"))
b = int(input("enter num2:"))
print((a+b)/2)
------------------------------------------

# square of a num
a = int(input("Enter a number:"))
print(a**2)
------------------------------------

# concatenation
name = "narmada"
greet = "hello, "
print(greet + name)
---------------------------------------------------------
#escape sequ
story = "Narmada is a good girl. \n\tShe is very obidient."
print(story)
--------------------------------------------------------------

# input func
name = input("Enter the name:\n")
print("Good morning, " + name)
----------------------------------------

# letter format
letter = '''Dear, <|NAME|>
You are selected!

Date: <|DATE|>'''

name = input("Enter your name")
date = input("Enter today's date")
letter=letter.replace("<|NAME|>", name)
letter=letter.replace("<|DATE|>", date)

print(letter)
------------------------------------------------------------

# find double space
string = "Let's write a   story to detect  double spaces" 

doubleSpaces = string.find("  ")
print(doubleSpaces)
----------------------------------------------------------------
#replace double spaces
string = "Let's write a  story to detect  double spaces" 

doubleSpaces = string.replace("  ", " ")
print(doubleSpaces)
--------------------------------------------------------------
# fruits list
f1 = input("Enter fruit num 1:")
f2 = input("Enter fruit num 2:")
f3 = input("Enter fruit num 3:")
f4 = input("Enter fruit num 4:")
f5 = input("Enter fruit num 5:")
f6 = input("Enter fruit num 6:")
f7 = input("Enter fruit num 7:")

myFruitsList = [f1, f2, f3, f4, f5, f6, f7]
print(myFruitsList)
-----------------------------------------------------
# sorted marks
m1 = int(input("marks of student 1 m1:"))
m2 = int(input("marks of student 1 m2:"))
m3 = int(input("marks of student 1 m3:"))
m4 = int(input("marks of student 1 m4:"))
m5 = int(input("marks of student 1 m5:"))
m6 = int(input("marks of student 1 m6:"))

marks=[m1, m2, m3, m4, m5, m6]
marks.sort()
print(marks)
-----------------------------------------------------
# sum of list
a = [4, 76, 4, 76, 87,44] 
  #print(a[0]+a[1]+a[2]+a[3]+a[4]+a[5])   #or
print(sum(a))
----------------------------------------------------
# tuple count
#Count zero
tup = (5, 6, 0, 4, 0, 0, 2)
print(tup.count(0))
----------------------------------------------------
#dictionary
myDict = {
    "Narmada":"Coder",
    "Games":"Tennis",
    "Marks":[1,2,3,4],
    "anotherDict" : {"Narmada":"Student"}
}

print(myDict["Games"])
print(myDict["Narmada"])
print(myDict["Marks"])
print(myDict["anotherDict"])
print(myDict["anotherDict"]["Narmada"])

print(myDict)

---------------------------------------------
#dictionary methods
print(myDict.keys())
print(list(myDict.keys()))
print((myDict.values()))
print(list(myDict.values()))
print(myDict.items())
print(list(myDict.items()))

UpdateDict = {
    "good" : "friend",
    "Natural":"Oil"
}

myDict.update(UpdateDict)
print(myDict)

print(myDict.get("Narmada"))
print(myDict["Narmada"])

print(myDict.get("Narmada1"))
print(myDict["Narmada1"])
---------------------------------------------

# empty 
a = [] #empty list
b = () #empty tuple
c = {}  #empty dict
d = set() #empty set

print(type(a))
print(type(b))
print(type(c))
print(type(d))
---------------------------------------------
#dict ex
myDict = {
    "nenu" :"me",
    "nuvvu":"you",
    "enti":"what",
    "ela":"how"
}

print("The available options are", myDict.keys())
a = input("Enter the word tou want to translate\n")
print("The meaning of this word is\n", myDict.get(a))

--------------------------------------------------------
#unique num set
n1 = int(input("Enter the number1 :"))
n2 = int(input("Enter the number2 :"))
n3 = int(input("Enter the number3 :"))
n4 = int(input("Enter the number4 :"))
n5 = int(input("Enter the number5 :"))
n6 = int(input("Enter the number6 :"))
n7 = int(input("Enter the number7 :"))
n8 = int(input("Enter the number8 :"))

a = {n1, n2, n3, n4, n5, n6, n7, n8}  #set
#a = (n1, n2, n3, n4, n5, n6, n7, n8)   tup

print(a)
------------------------------------
#str n in in set
set = {18, "18"}
print(set)
print(len(set))
--------------------------------------

# float and int in set
set = {34, 34.0, "34"}
print(set)                       #float is considered as int in set
print(len(set))
----------------------------------------------------------------

# dict prob ex
favLang = {}
a = input("Enter fav lang of sonali")
b = input("Enter fav lang of rohan")
c = input("Enter fav lang of neethi")
d = input("Enter fav lang of arnav")

favLang["sonali"] = a
favLang["rohan"] = b
favLang["neethi"] = c
favLang["arnav"] = d

print(favLang)

--------------------------------------------
#part 2
favLang = {}
a = input("Enter fav lang of sonali")
b = input("Enter fav lang of rohan")
c = input("Enter fav lang of sonali")
d = input("Enter fav lang of arnav")

favLang["sonali"] = a
favLang["rohan"] = b
favLang["sonali"] = c
favLang["arnav"] = d

print(favLang)

--------------------------------------------
# part 3
favLang = {}
a = input("Enter fav lang of sonali")
b = input("Enter fav lang of rohan")
a = input("Enter fav lang of neethi")
d = input("Enter fav lang of arnav")

favLang["sonali"] = a
favLang["rohan"] = b
favLang["neethi"] = a  #keys are unique but values are not
favLang["arnav"] = d

print(favLang)
----------------------------------------------------
#set
a = {23, 6, 7, "harshitha", [2,3,4,5]}
#a = {23, 6, 7, "harshitha"} this is valid
print(a)

#error because you cannot store list in a set since list is muttable and set is not
--------------------------------------------------------------------------------------
# list in set
a = set(23, 6, 7, "harshitha", [2,3,4,5])
print(a)
---------------------------------------------------
# conditional statment

n1 = int(input("Enter num1: "))
n2 = int(input("Enter num2: "))
n3 = int(input("Enter num3: "))
n4 = int(input("Enter num4: "))

if (n1>n2):
    f1 = n1
else:
    f1 = n2

if (n3>n4):
    f2 = n3
else:
    f2 = n4

if f1>f2:
    print(str(f1) + " is greatest")  
else:
    print(str(f2) + " is greatest")                  

------------------------------------------------
# Marks

sub1 = int(input("enter marks of s1 "))
sub2 = int(input("enter marks of s2 "))
sub3 = int(input("enter marks of s3 "))

if (sub1<33 or sub2<33 or sub3<33):
    print("fail because you have lesss marks in one of these sub")

elif ((sub1 + sub2 + sub3)/3 <40):
    print("fail due to least total marks")    
else:
    print("congrats, you passed!")    

----------------------------------------------------------------
#detect spam

text = input("Enter the text: ")

spam = False

if ("buy now" in text):
    spam = True
elif ("click this" in text):
    spam = True
elif ("subscribe " in text):
    spam = True
elif("make money" in text):
    spam=True
else:
    spam = False            

if (spam):
    print("this is spam")
else:
    print("not spam")      

-------------------------------------------------
#IS AND IN in a code

a = None
if ( a is None):
    print("yes")
else:
    print("no")    


b = [2, 56, 7, 56, 79]
print(76  in b)    
---------------------------------------
# in ex

name = input("Enter the username : ")

a = len(name)

if (a < 10 ):
    print("less than 10 char")
else:
    print("greater than 10 char")    

-----------------------------------------
# IN

nameList = ["nammu", "hemu", "jyo", "deepu", "tom"]

name = input("Enter the name : ")

if name in nameList:
    print("your name is present")
else:
    print("your name doesn't exist in the list")    

----------------------------------------------------
#Grade
marks = int(input("Enter your marks: "))

if marks>=90:
    grade = "O"
elif marks>=80:
    grade = "A"    
elif marks>=70:
    grade = "B"
elif marks>=60:
    grade = "C"    
elif marks>=50:
    grade = "D"
else:
    grade = "F"    

print("Your grade is " + grade)    
-------------------------------------------------

#post

string = "Hey, guys this is Yoyo channel. Today we are going to publish an article about most successful young talent. she's is none other than Miss Narmada"

Name = "Narmada"

if Name in string:
    print("Yes, this post is talking about Narmada")
else:
    print("This post is not talking about Narmada")    
-------------------------------------------------------------
#while loop

i = 0

while i < 10 :
    print("Yes " + str(i))
    i = i+1

print("done")    
---------------------------------
# while ex

i = 1

while i<=50:
    print(i)
    i = i + 1
----------------------------
#ex2
i = 0

while i<5:
    print("Nammu")
    i = i + 1
--------------------------
#ex 3 fruits
fruits = ["mango", "orange", "grapes", "watermelon", "banana "]
i = 0
while i<len(fruits):
    print(fruits[i])
    i = i + 1

-----------------------------------------------
#for fruits

fruits = ["mango", "banana", "orange", "chikku", "grapes"]

for item in fruits:
    print(item)
  -----------------------------------------------
#range func

for i in range(10):
    print(i)
--------------------------
#else in for loop
for i in range(5):
    print(i)
else:
    print("this is else in for loop")
  ----------------------------------------
#break

for i in range(10):
    print("Hello World")
    if i==5:
        break

else:
    print("Break has been applied") 
    #This will execute only when the loop is broken using "break" statement.
--------------------------------------------------------------------------------
# continue 

for i in range(10):
    if i%2!= 0:
        continue
    print(i)
-------------------------
# ex 1
for i in range(10):
    if i == 5:
        continue
    print(i)    
  -------------------------
# ex 2
for i in range(10):
    if i%2==0:
        continue
    print(i)

----------------------------

# for loop for tables

n = int(input("Enter the num: "))

for i in range(1, 11):
   # print(str(n) + "X" + str(i) + "=" + str(n*i))
   print(f"{n}X{i}={n*i}")
  ------------------------------------------------
#Name prob

list = ["nammu", "hemu", "dummu", "simmu", "sushma"]

for name in list:
    if name.startswith("s"):
        print("Hello,"+ name )
-------------------------------------------------------------

# while loop for above prob

n = int(input("Enter a numb"))
i = 1

while i<11:
    print(f"{n} X {i} = {n*i}")
    i = i + 1
----------------------------------------------
# prime or not

num = int(input("Enter the numb: "))
prime = True

for i in range(2, num):
    if num%i ==0:
        prime=False
        break
if prime:
    print("The num is prime")
else:
    print("not prime")    
    
-----------------------------------
# sum of n natural no.s

n = int(input("enter a num: "))
i = 1
sum = 0

while i<=n:
    sum = sum+i
    i = i+1

print(sum)    

-----------------------------------
# factorial of a num

# n! = 1 x 2 x 3 x 4 x 5 x 6......n
# 5! = 1 x 2 x 3 x 4 x 5

n = int(input("enter a num: "))
fact=1

for i in range(1, n+1):
    fact = fact*i

print(f"factorial of the num {n} is {fact}")    

----------------------------------------------
# pattern

n = int(input("enter a nu: "))

for i in range(n):
    for j in range(n):
        print("* ", end="")

    print()        
-------------------------------------
# pattern ex2
n = int(input("enter a num: "))

for i in range(n):
    for j in range(i+1):
        print("* ", end= "")
    print()    

-------------------------------------
# pattern ex 3

n = int(input("enter the num"))

for i in range(n):
    for j in range(n-i):
        print("* ", end="")

    print()    

---------------------------------------------
# tables reverse

num = int(input("enter a num: "))

for i in range(11,0,-1):
    print(f"{num}x{i}={num*i}")

---------------------------------------
# print func

def func(a,b):
    c = a+b
    print(c)

func(3,4)    
----------------------
# return

def func1(x):
    return x+1

def func2(a,b):
    c = a+b
    return c

output = func2(3,4)
final_output = func1(output)
print(final_output)

#here we are passing func2 output as a argument to func1 by the help of return 

--------------------------------------------------------------------
#func 

def func(name):
    print('Good Morning!' + name)

func("narmada")
------------------------------------
# func ex

def percentage(marks):
    return ((marks[0] + marks[1] +marks[2 ])/300)*100

marks1 = [45, 60, 97]
percent1 = percentage(marks1)

marks2 = [23,46,78]
percent2 = percentage(marks2)

print(percent1, percent2)

--------------------------------------------------------
# function using print ex

def percentage(marks):
    return ((marks[0] + marks[1] +marks[2 ])/300)*100

marks1 = [45, 60, 97]
percent1 = percentage(marks1)

marks2 = [23,46,78]
percent2 = percentage(marks2)

print(percent1, percent2)
-----------------------------------------
# function using return keyword

def greet(name):
    return ("Good morning " + name)

def add_sub(x, y):
    z = x+y
    s = x-y
    return z, s

print(greet("nammu"))    
print(add_sub(4,6))

------------------------------------------------
# function with default argument

def greet(name = "Stranger"):
    print("Good day!, " + name)


greet("Nammu")    
greet()
---------------------------------------
#factorial

# n! = 1 x 2 x 3 x 4 x 5......n
# 4! = 1 x 2 x 3 x 4 x 5
n = int(input("Enter a num "))
fact = 1

for i in range(n):           
    fact = fact * (i+1)

print(fact)

------------------------------------
# recusrion factorial

def factorial(n):
    fact = 1
    for i in range(n):
        fact = fact * (i+1)
    return fact                           
    
a = factorial(3)
print(a)   

 
def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n * factorial_recursive(n-1)

a = factorial_recursive(5)
print(a)    

----------------------------------------------
# factorial 

def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x * factorial(x-1)
    
print(factorial(5))    

------------------------------------
# maximum no among 3

def maximum(n1, n2, n3):
    if (n1>n2):
        if (n1>n3):
            return n1
        else:
            return n3
    else:
        if n2>n3:
            return n2
        else:
            return n3    

output = maximum(3, 16, 8)
print(output)       
-----------------------------------------
# celcius to farhenhiet

def farh(cel):
    return (c * (9/5)) + 32

c = 34
f = farh(c)

print(f"farhenhiet of {c} celcius is {f}")
----------------------------------------------
# end keyword

print("Hello", end=" ")
print("world", end=" ")
print("Good morning", end=" ")
print("!", end=" ")
-----------------------------------
# sum of n natural no

#sum(n) = sum(n-1) + n

def sum_recursive(n):
    if n==0:
        return 0
    else:
        return n + sum_recursive(n-1)

a = sum_recursive(5)
print(a)
----------------------------------------
# pattern

n = int(input("Enter a num: "))

for i in range(n):
    print("#" * (n-i))
---------------------------------------

# inch to cm
def cm(inch):
    return inch * 2.54

inch = 2
a = cm(inch)
print(a)
------------------------
# strip

text = "       apple is a fruit      "

print(text)
print(text.strip())
------------------------------------
# strip ex 1

def replace_and_strip(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()


txt = "      Nammu is a good girl.....      "
new = replace_and_strip(txt, "Nammu")
print(new)
------------------------------------------------
# def func of table

n = int(input("Enter a num: "))

def table(n):
    for i in range(1, 11):
        print(f"{n}x{i}={n*i}")

table(n)     
------------------------------------
# input output func

file = open("82 sample.txt", "r")
#data = file.read()   #reads whole context
data = file.read(5)
print(data)
file.close()
--------------------------------------------

# readline

file = open("82 sample.txt","r")

data = file.readline()  #reads first line
print(data)
data = file.readline()   #reads second line
print(data)
file.close()
---------------------------------------------
# sample.txt
------------------------------
# another txt file
------------------------------

# write

file2 = open("82 another.txt", "w")
file2.write("Please write this to the file  ")
file2.close()
-------------------------------------------------------
# append

file3 = open("82 another.txt", "a")
file3.write("i am appending")
file3.close()
-------------------------------------------
# write multiple

file4 = open("82 another.txt" , "w")
file4.write("This is nice")
file4.write("This is not nice")
file4.write("This is insane")
file4.close()
--------------------------------------

----------------------- ##################### FILE HANDLING ###############------------
# with

with open("82 another.txt", "r") as f: 
    a =f.read()
    print(a)
with open("82 another.txt", "w") as f:
    b = f.write("Now i am writing")   
    print(b) 
    
-------------------------------------------

file = open("88 poems.txt")
a = file.read()
if "twinkle" in a:
    print("present")
else:
    print("absent")    
file.close()    
------------------------------------

# POEMS.TXT
----------------------

# GAME HISCORE.PY

def game():
    return 354

score = game()
with open("90 hiscore.txt") as f:
    hiscore = int(f.read())

if hiscore<score :
    with open("90 hiscore.txt", "w" )  as f:
        f.write(str(score)) 

-----------------------------------------------
# HISCORE.TXT
-----------------------







