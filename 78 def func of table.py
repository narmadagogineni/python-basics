n = int(input("Enter a num: "))

def table(n):
    for i in range(1, 11):
        print(f"{n}x{i}={n*i}")

table(n)     