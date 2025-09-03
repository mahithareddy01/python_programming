def isLeapYear(year):
    if(year%400==0):
        return True
    elif(year%100==0):
        return False
    elif(year%4==0):
        return True
    else:
        return False
n=int(input("Enter an year:"))
print(f"{n} is leapyear? : {isLeapYear(n)}")