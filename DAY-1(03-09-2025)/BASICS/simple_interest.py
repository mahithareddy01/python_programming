#find simple interest and total amount in hand
p=int(input("Principle Amount: "))
r=int(input("Rate of Interest: "))
t=int(input("Total Number of Months:"))
SI=(p*t*r)/100
amount=SI+p
print("Simple Interest : ",SI)
print("Total amount in hand: ",amount)