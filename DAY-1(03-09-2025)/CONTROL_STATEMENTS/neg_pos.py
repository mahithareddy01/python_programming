def check(num):
    if(num<0):
        return "Negative"
    else:
        return "Postive"
n=int(input("Enter a number:"))
print(f"{n} is {check(n)}")