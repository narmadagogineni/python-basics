myDict = {
    "nenu" :"me",
    "nuvvu":"you",
    "enti":"what",
    "ela":"how"
}

print("The available options are", myDict.keys())
a = input("Enter the word tou want to translate\n")
print("The meaning of this word is\n", myDict.get(a))
