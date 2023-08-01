# n! = 1 x 2 x 3 x 4 x 5 x 6......n
# 5! = 1 x 2 x 3 x 4 x 5

n = int(input("enter a num: "))
fact=1

for i in range(1, n+1):
    fact = fact*i

print(f"factorial of the num {n} is {fact}")    

