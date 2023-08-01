def factorial(n):
    fact = 1
    for i in range(n):
        fact = fact * (i+1)
    return fact                           
    
a = factorial(3)
print(a)   

 
   
    
def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n * factorial_recursive(n-1)

a = factorial_recursive(5)
print(a)    