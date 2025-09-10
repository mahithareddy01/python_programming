ipt=input("Enter a String: ")
freq={}
for ch in ipt:
    freq[ch] = freq.get(ch, 0) + 1
for ch in freq:
    print(f"{ch}{freq[ch]}",end="")