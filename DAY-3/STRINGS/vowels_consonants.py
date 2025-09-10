ipt=input("Enter a String: ")
vow='aeiouAEIOU'
vow_count=0
cons_count=0
for ch in ipt:
    if ch in vow:
        vow_count+=1
    else:
        cons_count+=1
print(f"no. of vowels,consonants in {ipt}: {(vow_count,cons_count)}")