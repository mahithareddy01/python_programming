def add(dict1,key,value):
    dict1[key]=value
    print(f"After adding: {dict1}")
def remove_book(dict1, key):
    if key in dict1:
        removed = dict1.pop(key)
        print(f"After removing book '{removed}': {dict1}")
    else:
        print(f"Book ID {key} not found.")
def search(book,key):
    if key not in book.keys():
        print(f"{key} is not present ")
    else:
        print(f"{key}:{book[key]} is present")
def update(book,key,value):
    if key not in book.keys():
         print(f"{key} is not present ")
    else:
        book[key]=value
        print(f"Updated is : {book}")
def display(dict1):
    print(f"{dict1}")
def count_books(dict1):
    count=0
    for key in dict1.keys():
        count+=1
    print(f"Number of books is {count}")
def check(dict1,value):
    if value in dict1.values():
        print(f"{value} is present")
    else:
        print(f"{value} is not present")
print("--------LIBRARY MANAGEMNET-------")
print("1.Add a book to the library")
print("2.Remove a book using Book ID")
print("3.Search for a book by Book ID and display the title.")
print("4.Update the title of a book")
print("5.Display all books in the library.")
print("6.Count the total number of books in the library.")
print("7.Check if a book title exists in the library")
lib={}
while True:
    ch=int(input("Enter your choice: "))
    if ch==1:
        book_id=input("Enter Book id: ")
        book_title=input("Enter book title:")
        add(lib,book_id,book_title)
    elif ch==2:
        rem=input("Enter Book Id to remove: ")
        remove_book(lib,rem)
    elif ch==3:
        srch=input("Enter Book Id to search: ")
        search(lib,srch)
    elif ch==4:
        id=input("Enter Id of the book: ")
        title=input("Enter new title: ")
        update(lib,id,title)
    elif ch==5:
        display(lib)
    elif ch==6:
        count_books(lib)
    elif ch==7:
        b_title=input("Enter title to search: ")
        check(lib,b_title)
    else:
        break
