#print ASCII character with their values
def print_ascii():
    for i in range(0,256):
        print(i," - ", chr(i),end=" ")
print_ascii()