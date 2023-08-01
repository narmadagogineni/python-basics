def func1(x):
    return x+1

def func2(a,b):
    c = a+b
    return c

output = func2(3,4)
final_output = func1(output)
print(final_output)

#here we are passing func2 output as a argument to func1 by the help of return 