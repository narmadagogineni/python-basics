file = open("82 sample.txt", "r")
#data = file.read()   #reads whole context
data = file.read(5)
print(data)
file.close()
