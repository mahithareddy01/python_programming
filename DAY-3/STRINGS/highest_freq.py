ipt=input("Enter a String: ")
freq={}
for ch in ipt:
    freq[ch] = freq.get(ch, 0) + 1
high_freq=0
key=''
for k,v in freq.items():
    if(v>high_freq):
        high_freq=v
        key = k
print(f"The highest frequency is {high_freq} for {key}")