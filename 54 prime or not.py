num = int(input("Enter the numb: "))
prime = True

for i in range(2, num):
    if num%i ==0:
        prime=False
        break
if prime:
    print("The num is prime")
else:
    print("not prime")    
    


