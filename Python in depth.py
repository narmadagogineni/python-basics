print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.''')

# playsound
from playsound import playsound
playsound('C:\\Users\\Narmada G\\OneDrive\\Desktop\\python codes 2\\tiktok.mp3')

#list directory
import os
print(os.listdir())


# single line comment
'''hello this is multiline comment
you can write the comment a long as you want
it wont be sisplayed in the output'''

#add two num
a = 35
b = 20
print("The sum of a and b is", a+b)

#remainder
c = 45
d = 12
print("The remainder when divided by c and d", c%d)

#type of input function
a = input("enter a number:")
print(a)
print(type(a)) 

#comparisono operator
a = 34
b = 80
print(a > b)

# avg of 2 num
a = int(input("Ener num1:"))
b = int(input("enter num2:"))
print((a+b)/2)

# square of a num
a = int(input("Enter a number:"))
print(a**2)

# concatenation
name = "narmada"
greet = "hello, "
print(greet + name)

#escape sequ
story = "Narmada is a good girl. \n\tShe is very obidient."
print(story)

# input func
name = input("Enter the name:\n")
print("Good morning, " + name)

# letter format
letter = '''Dear, <|NAME|>
You are selected!

Date: <|DATE|>'''

name = input("Enter your name")
date = input("Enter today's date")
letter=letter.replace("<|NAME|>", name)
letter=letter.replace("<|DATE|>", date)

print(letter)


# find double space
string = "Let's write a   story to detect  double spaces" 

doubleSpaces = string.find("  ")
print(doubleSpaces)

#replace double spaces
string = "Let's write a  story to detect  double spaces" 

doubleSpaces = string.replace("  ", " ")
print(doubleSpaces)

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

# sum of list
a = [4, 76, 4, 76, 87,44] 
  #print(a[0]+a[1]+a[2]+a[3]+a[4]+a[5])   #or
print(sum(a))

# tuple count
#Count zero
tup = (5, 6, 0, 4, 0, 0, 2)
print(tup.count(0))

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

# empty 
a = [] #empty list
b = () #empty tuple
c = {}  #empty dict
d = set() #empty set

print(type(a))
print(type(b))
print(type(c))
print(type(d))

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

#str n in in set
set = {18, "18"}
print(set)
print(len(set))


# float and int in set
set = {34, 34.0, "34"}
print(set)                       #float is considered as int in set
print(len(set))

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

a = {23, 6, 7, "harshitha", [2,3,4,5]}
#a = {23, 6, 7, "harshitha"} this is valid
print(a)

#error because you cannot store list in a set since list is muttable and set is not



