def isVowel(c):
    if c in ['a','e','i','o','u']:
        return "Vowel"
    else:
        return "Consonant"
ch=input("Enter any alphabet: ")
print(f"{ch} is : {isVowel(ch)}")