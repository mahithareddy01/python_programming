def type(ch):
    if(ch.isalpha()):
        
        if ch.isupper():
            return "Alphabet (upper case)"
        else:
            return "Alphabet (lower case)"
    
    elif ch.isdigit():
        return "digit"
    else:
        return "special character"
char=input("Enter character: ")
print(f"character {char} is {type(char)}")
