def isArmstrong(n):
    temp=n
    sum=0
    while(n>0):
        rem=n%10
        sum+=rem*rem*rem
        n//=10
    return temp==sum
n=int(input("Enter a number: "))
print("Armstrong numbers are ",end=" ")
for i in range(1,n+1):
    if(isArmstrong(i)):
        print(i,end=" ")