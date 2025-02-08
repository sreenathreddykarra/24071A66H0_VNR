def checkprime(n):
    count = 0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
        else:
            continue
    
    if(count==2):
        return print(f"{n} is a prime number")
    else:
       return print(f"{n} is not a prime number")
        
x=int(input("Enter a number: "))
res=checkprime(x)
