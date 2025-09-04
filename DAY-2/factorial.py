def factorial(n):
    fact=1
    for i in range(n,0,-1):
        fact*=i
        if(i!=1):
            print(i,end='*')
        else:
            print(1)
    return fact
        
       
input_num=int(input("Enter a number: "))
print(f"factorial of {input_num} is {factorial(input_num)}")