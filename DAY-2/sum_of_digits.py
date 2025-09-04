def sum(num):
    sum=0
    while(num>0):
        rem=num%10
        sum+=rem
        num//=10
    return sum
n=int(input("enter number: "))
print(f"sum of digits of {n} is:\n {sum(n)}")