def isAlphabet(char):
    if char.isalpha():
        return True
    else:
        return False
char=input("Enter a character:")
print(f"{char} is alphabet is : {isAlphabet(char)}")