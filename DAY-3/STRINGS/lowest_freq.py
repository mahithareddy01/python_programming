ipt=input("Enter a String: ")
freq={}
for ch in ipt:
    freq[ch] = freq.get(ch, 0) + 1
low_freq = float('inf')
key=''
for k,v in freq.items():
    if(v<low_freq):
        low_freq=v
        key = k
print(f"The highest frequency is {low_freq} for {key}")