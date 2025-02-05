def  calci(m,n,operator):
    if(operator=='+'):
        return print("sum is ",m+n)
    elif(operator=='-'):
        return print("difference is ",m-n)
    elif(operator=='*'):
        return print("product is ",m*n)
    elif(operator=='%'):
        return print("Remainder is",m%n)
    else:
        return print("Invalid operator")
    
x=int(input("Enter the number 1:"))
y=int(input("Enter the number 2:"))
z=input("Enter the operator: ")
result =calci(x,y,z)
