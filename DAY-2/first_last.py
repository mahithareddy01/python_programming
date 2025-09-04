def first(num):
    rem=0
    while(num>0):
        rem=num%10    
        num//=10
    return rem
n=int(input("enter number: "))
print(f"last digit:{n%10} , first digit={first(n)}")
print(f"sum of first digit and last digit: {(n%10)+first(n)}")