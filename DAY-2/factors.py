def factors(n):
    for i in range(1,n):
        if n%i==0:
            print(i,end=" ")
n=int(input("Enter a number: "))
print("Factors are ",end=" ")
factors(n)