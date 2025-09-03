def areEqual(a,b,c):
    if a==b and b==c and c==a:
        return True
    return False
print("10,'10',10 are equal is: ",areEqual(10,'10',10)) #false
print("10,20,30 are equal is: ",areEqual(10,20,30))     #false