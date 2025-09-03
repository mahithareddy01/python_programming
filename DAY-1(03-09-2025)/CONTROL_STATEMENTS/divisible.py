def divisible(num):
    if num%5==0 and num%11==0:
        return True
    else:
        return False
n=int(input("Enter a number:"))
print(f"{n} divisible by 5 and 11 is {divisible(n)}")
