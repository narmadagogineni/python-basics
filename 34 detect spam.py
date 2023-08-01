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