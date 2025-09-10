s=input("Enter a String: ")
c=0
for i in s:
    c+=1

print(f"length of {s} is {c}")
#concat
s2=input("Enter another string: ")
print(f"Concatenation of {s} and {s2} is: {s+s2}")
#compare
if(s==s2):
    print(f"String {s} and {s2} are equal")
else:
    print(f"String {s} and {s2} are not equal")