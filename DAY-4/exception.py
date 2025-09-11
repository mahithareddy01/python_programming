a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
try:
    print(f"Divison is: {a/b}")
except ZeroDivisionError:
    print("Error:Division by zero is not allowed")
else:
    print("No exception occured")
finally:
    print("Finally block")