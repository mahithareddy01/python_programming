def to_word(num):
    dict={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:'zero'}
    for dig in str(num):
        print(dict[int(dig)],end=" ")
n=int(input("Enter a number: "))
print(f"{n} in words: ")
to_word(n)