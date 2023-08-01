file = open("82 sample.txt","r")

data = file.readline()  #reads first line
print(data)
data = file.readline()   #reads second line
print(data)
file.close()