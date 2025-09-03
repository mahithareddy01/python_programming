#program to swap 2 numbers
a=int(input("Enter a: "))
b=int(input("Enter b: "))
print("Before swapping a=",a,"b=",b)
a,b = b,a
print("After swapping a=",a,"b=",b)
sum=a+b
a=sum-a
b=sum-b
print("After swapping again a=",a,"b=",b)