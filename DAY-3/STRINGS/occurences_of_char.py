ipt=input("Enter a String: ")
char= input("Enter a character to search ocuurences in string:")
pos=0
l=[]
for ch in ipt:
    if ch==char:
        l.append(pos)
    pos+=1
print(f"Occurences of {char} in {ipt} are at positions: {l}")