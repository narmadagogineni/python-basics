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