def alphabets(s):
    cnt=0
    for ch in s:
        if(ch.isalpha()):
            cnt+=1
    return cnt

def digits(s):
    cnt=0
    for ch in s:
        if(ch.isdigit()):
            cnt+=1
    return cnt
def spl_chars(s):
    cnt=0
    for ch in s:
        if(not ch.isalpha() and not ch.isdigit()):
            cnt+=1
    return cnt
ipt=input("Enter a String: ")
print(f"(digits:{digits(ipt)} , alphabets:{alphabets(ipt)} ,special characters:{spl_chars(ipt)} )")