def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

def isStrong(n):
    temp=n
    sum=0
    while(n>0):
        rem=n%10
        sum+=fact(rem)
        n//=10
    return sum==temp
n=int(input("Enter a number: "))
print("Strong numbers are ",end=" ")
for i in range(1,n+1):
    if(isStrong(i)):
        print(i,end=" ")