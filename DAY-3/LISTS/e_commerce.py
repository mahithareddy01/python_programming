def add(cart,item):
    if item not in cart:
        cart.append(item)
        print(f"{item} is added\n Cart is:{cart}")
    else:
        print(f"{item} already exists in Cart")
def remove_ele(lst,ele):
    if ele in lst:
        lst.remove(ele)
        print(f"{ele} is remove\n Cart is:{lst}")
    else:
        print(f"{ele} doesn't exist in list")
def search(lst,ele):
    if ele not in lst:
        print(f"{ele} is not present in cart")
    else:
        pos=0
        for i in lst:
            if i==ele:
                print(f"{ele} is present at postion {pos}")
            pos+=1
def sort_items(lst):
    lst.sort()
    sorted(lst)
    print(f"Cart sorted successfully: {lst}")
def clear_items(lst):
    lst.clear()
    print(f"Cart: {lst}")
def display(lst):
    print(f"The Cart is: {lst}")
def count_prods(lst):
    print(f"Number of products in cart: {len(cart)}")
print("Cart Operations:\n1. Add Product\n2. Remove Product\n3. Search Product\n4. Display Cart\n5. Count Products\n6.Sort the cart alphabetically\n7.Clear the cart\n8. Exit")

cart=[]
while True:
    ch=int(input("Enter your choice: "))
    if(ch==1):
        item=input("Enter item to add to the cart: ")
        add(cart,item)
    elif ch==2:
        item=input("Enter item to remove from the cart: ")
        remove_ele(cart,item)
    elif ch==3:
        item=input("Enter item to search in the cart: ")
        search(cart,item)
    elif ch==4:
        display(cart)
    elif ch==5:
        count_prods(cart)
    elif ch==6:
        sort_items(cart)
    elif ch==7:
        clear_items(cart)
    else:
        break