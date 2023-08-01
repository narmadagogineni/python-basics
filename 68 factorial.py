# n! = 1 x 2 x 3 x 4 x 5......n
# 4! = 1 x 2 x 3 x 4 x 5
n = int(input("Enter a num "))
fact = 1

for i in range(n):           
    fact = fact * (i+1)

print(fact)
