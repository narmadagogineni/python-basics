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