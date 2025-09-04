def print_nums(n):
    i=1
    sum=0
    while i<=n:
        sum+=i
        if(i!=n):
            print(i,end='+')
        else:
            print(n)
        i+=1
    return sum
num=int(input("Enter a number: "))
print(f"the sum of first{num} natural numbers is: {print_nums(num)}")