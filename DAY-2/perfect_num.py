def isPerfect(n):
    temp=n
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum==temp
n=int(input("Enter a number: "))
print("Perfect numbers are ",end=" ")
for i in range(1,n+1):
    if(isPerfect(i)):
        print(i,end=" ")