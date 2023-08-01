n = int(input("enter the num"))

for i in range(n):
    for j in range(n-i):
        print("* ", end="")

    print()    