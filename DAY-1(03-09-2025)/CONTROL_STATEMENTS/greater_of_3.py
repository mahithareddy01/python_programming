def greatest(a,b,c):
    if(a>b):
        if(a>c):
            return a
        else:
            return b
    else:
        if(b>c):
            return b
        else:
            return c
a,b,c=map(int,(input("Enter 3 numbers: ").split()))
print(f"greatest of {a,b,c} is: {greatest(a,b,c)}")