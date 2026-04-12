books=[]
issued_books=[]
# Add BOOks
def Add_Books():
    name=input("Enter the name of the books")
    books.append(name)
    print("Books added")
#show view books
def view_books():
    print("Books in the library")
    for book in books:
        print("books")
#Isssue Books
def issue_books():
    name=input("Enter the name of the books")
    if name in books:
        books.remove(name)
        print("books issued")
    else:
        print("books not issued")
#Return Books
def return_books():
    name=input("Enter the name of the books")
    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print("books returned")
    else:
        print("Books not returned")

# ! main Body
def library ():
    while True:
        print("\n1. Add Books")
        print("\n2. View Books")
        print("\n3. Issue Books")
        print("\n4. Return Books")
        print("\n5. Exit")

        choice = int(input("Enter your choice"))
        if choice == 1:
            Add_Books()
        elif choice == 2:
            view_books()
        elif choice == 3:
            issue_books()
        elif choice == 4:
            return_books()
        elif choice == 5:
            print("exit")
            break
        else:
            print("Invalid Choice")
            break

library()