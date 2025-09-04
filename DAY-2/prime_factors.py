def factors(n):
    for i in range(1,n):
        if n%i==0 and isPrime(i):
            print(i,end=" ")
def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
n=int(input("Enter a number: "))
print("Prime Factors are ",end=" ")
factors(n)