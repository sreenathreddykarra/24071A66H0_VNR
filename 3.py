def lcm(m,n):
    if(m-n>0):
        max=m
    else:
        max=n
    lcm=max
    while(lcm % m !=0) or (lcm%n !=0):
        lcm+=max
    return lcm


x=int(input("Enter the number 1:"))
y=int(input("Enter the number 2:"))

print("The lcm of the two numbers is:",lcm(x,y))
gcd=(x*y)/lcm(x,y)
print("The gcd of the two numbers is:",int(gcd))
