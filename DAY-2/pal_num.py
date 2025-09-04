def isPalindrome(n):
    sum=0
    temp=n
    while(n>0):
        rem=n%10
        sum=sum*10+rem
        n//=10
    return temp==sum
n=int(input("Enter a number: "))
print("Palindrome numbers are ",end=" ")
for i in range(1,n+1):
    if(isPalindrome(i)):
        print(i,end=" ")