# Create a menu driven library books using functions and while loop(Add book, display book, update price of book,
# delete book) In Add book inputs are: Book id, Book name, Book author, Book price, Book publisher

l = {}
def addbook():
    a = int(input("How many to enter: "))
    for i in range(a):
        print(f'enter {i+1} book details: ')
        id = int(input("Enter the book id: "))
        name = input("Enter the Name: ")
        auther = input("Enter the Name: ")
        price = float(input("Enter the price: "))
        publisher = input("Enter the book publisher: ")
        l[id] = {'name': name, 'auther': auther, 'price': price, 'publisher':
            publisher}
def displaybook():
    c = 0
    for i in l:
        print(f'enter {c + 1} book details: ')
        print('id', i)
        print("name: ", l[i]['name'])
        print("auther: ", l[i]['auther'])
        print("price: ", l[i]['price'])
        print("publisher: ", l[i]['publisher'])

def updateprice():
    id = int(input("Enter the book id to update price: "))
    if id in l:
        price = float(input("Enter the New price: "))
        l[id]['price'] = price
        print("Price updated successfully")

def deletebook():
    id = int(input("Enter the id to delete the book: "))
    if id in l:
        del [id]
        print("Book deleted successfully")

while True:
    print("Choose option: ")
    print("1. Add Book")
    print("2. Display Book")
    print("3. Update Book Price")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter Your Choice(1-5): ")
    if choice == "1":
        addbook()
    elif choice == "2":
        displaybook()
    elif choice == "3":
        updateprice()
    elif choice == "4":
        deletebook()
    elif choice == "5":
        print("exit")
        break
    else:
        print("Invalid Choice")