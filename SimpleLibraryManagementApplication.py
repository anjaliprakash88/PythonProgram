class LibrarySystem:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.admin_credentials = {'username': 'admin', 'password': '1234'}

    def admin_menu(self):
        while True:
            print("ADMIN Menu: ")
            print(" 1.Add Book\n 2.Update Book\n 3.Delete Book\n 4.Display Book\n 5.Exit")
            choice = input("Enter Your Choice: ")
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.update_book()
            elif choice == "3":
                self.delete_book()
            elif choice == "4":
                self.display_book()
            elif choice == "5":
                exit()
            else:
                print("invalid number, please enter correct number...")

    def add_book(self):
        book_id = input("Enter book ID: ")
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        quantity = int(input("Enter book quantity: "))

        self.books[book_id] = {'title': title, 'author': author, 'quantity': quantity}
        print("Book added successfully.")

    def update_book(self):
        id = input("Enter the book id:")
        if id in self.books:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            quantity = int(input("Enter book quantity: "))
            if title:
                self.books['book_id']['title'] = title
            if author:
                self.books['book_id']['author'] = author
            if quantity:
                self.books['book_id']['quantity'] = quantity
            print("Book updated successfully")
        else:
            print("Book id is not found")

    def delete_book(self):
        id = input("Enter the bool id")
        if id in self.books:
            del self.books[id]
            print("Book deleted successfully")
        else:
            print("Id is not found")

    def display_book(self):
        for i, j in self.books.items():
            print(i, j)

    def user_section(self):
        while True:
            print("ADMIN Section: ")
            print(" 1.Registration\n 2.Login\n 3.Exit")
            choice = input("Enter Your Choice: ")
            if choice == "1":
                self.register_user()
            elif choice == "2":
                if self.login_user():
                    self.user_menu()
            elif choice == "3":
                exit()
            else:
                print("invalid number, please enter correct number...")

    def register_user(self):
        print("\n--- User Registration ---")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        address = input("Enter Address: ")
        phone_number = input("Enter Phone Number: ")

        if phone_number in self.users:
            print("Phone number already registered!")
            return

        username = input("Enter Username: ")

        if any(user['username'] == username for user in self.users.values()):
            print("Username already exists!")
            return

        password = input("Enter Password: ")

        self.users[phone_number] = {
            'name': name,
            'age': age,
            'address': address,
            'username': username,
            'password': password
        }
        print(f"User '{username}' registered successfully!")

    def login_user(self):
        print("\n--- User Login ---")
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        for user in self.users.values():
            if user['username'] == username and user['password'] == password:
                print(f"Welcome, {username}!")
                return True
        print("Invalid credentials!")
        return False

    def user_menu(self):
        while True:
            print("\n--- User Menu ---")
            print(" 1. Display All Books\n 2. Search Book by Title\n 3. Exit")
            choice = input("Enter Your Choice: ")

            if choice == "1":
                self.display_book()
            elif choice == "2":
                title = input("Enter book title to search: ")
                self.search_book_by_title(title)
            elif choice == "3":
                print("Exiting to main menu.")
                break
            else:
                print("Invalid choice! Please try again.")

    def search_book_by_title(self, title):
        found = False
        for book_id, details in self.books.items():
            if title.lower() in details['title'].lower():
                print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Quantity: {details['quantity']}")
                found = True

        if not found:
            print(f"No book found with title '{title}'.")
    def main_menu(self):
        while True:
            print("Main Menu: ")
            print(" 1.Admin\n 2.User\n 3.Exit")
            choice = input("Enter Your Choice: ")

            if choice == "1":
                username = input("Enter Admin Username: ")
                password = input("Enter Admin Password: ")
                if self.admin_credentials['username'] == username and self.admin_credentials['password'] == password:
                    self.admin_menu()
            elif choice == "2":
                self.user_section()
            elif choice == "3":
                pass
            else:
                print("invalid number")


system = LibrarySystem()
system.main_menu()
