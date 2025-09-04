def table(num):
    i=1
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
n=int(input("Enter a number: "))
print(f"table of {n} is :")
table(n)