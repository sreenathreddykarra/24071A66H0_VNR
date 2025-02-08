def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
    
a=int(input("Enter a number: "))
for i in range(0,a):
    print("The fibonacci of",i, "is",fib(i))