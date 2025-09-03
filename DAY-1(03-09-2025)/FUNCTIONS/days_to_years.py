#A function with argument list and no return types
def convert(a):
    b=a/365
    c=a/30
    print(f"{a} days is {round(b,2)} years,{round(c,2)} months")
x=int(input("Enter days : "))
convert(x)