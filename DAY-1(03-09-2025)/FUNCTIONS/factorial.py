#A function with both argument list and return types
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
input_num=int(input("Enter a number: "))
print(f"factorial of {input_num} is {factorial(input_num)}")