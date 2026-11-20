
class LibraryManagement:
    def __init__(self):
        self.books = []
        self.borrowed_books = []
        self.book_id = 1

    def book_registration(self):
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        for book in self.books:
            if book["Title"].lower() == title.lower():
                print("This book is already registered.")
                return

        copies = input("Enter Number of Copies: ")

        if not copies.isdigit():
            print("Please enter a valid number.")
            return

        book = {
            "ID": "B00" + str(self.book_id),
            "Title": title,
            "Author": author,
            "Copies": int(copies)
        }

        self.books.append(book)
        self.book_id += 1

        print("Book added successfully.")
        print("Book ID:", book["ID"])

    def view_books(self):
        if len(self.books) == 0:
            print("No books available.")
            return

        for book in self.books:
            print("--------------------------------")
            print("Book ID:", book["ID"])
            print("Title:", book["Title"])
            print("Author:", book["Author"])
            print("Available Copies:", book["Copies"])

    def update_copies(self):
        book_id = input("Enter Book ID: ").upper()

        for book in self.books:
            if book["ID"] == book_id:
                copies = input("Enter New Number of Copies: ")

                if not copies.isdigit():
                    print("Invalid number of copies.")
                    return

                book["Copies"] = int(copies)

                print("Available copies updated successfully.")
                print("Available Copies:", book["Copies"])
                return

        print("Book ID not found.")

    def borrow_book(self):
        book_id = input("Enter Book ID: ").upper()

        for book in self.books:
            if book["ID"] == book_id:
                quantity = input("Enter Borrowing Quantity: ")

                if not quantity.isdigit():
                    print("Please enter a valid quantity.")
                    return

                quantity = int(quantity)

                if quantity == 0:
                    print("Quantity must be greater than zero.")
                    return

                if quantity > book["Copies"]:
                    print("Insufficient copies available.")
                    return

                book["Copies"] = book["Copies"] - quantity

                borrowed = {
                    "ID": book["ID"],
                    "Title": book["Title"],
                    "Quantity": quantity
                }

                self.borrowed_books.append(borrowed)

                print("Book borrowed successfully.")
                print("Book Title:", book["Title"])
                print("Borrowed Copies:", quantity)
                print("Remaining Copies:", book["Copies"])
                return

        print("Book ID not found.")

    def search_book(self):
        book_id = input("Enter Book ID to Search: ").upper()

        for book in self.books:
            if book["ID"] == book_id:
                print("Book found.")
                print("Book ID:", book["ID"])
                print("Title:", book["Title"])
                print("Author:", book["Author"])
                print("Available Copies:", book["Copies"])
                return

        print("Book not found.")

    def display_summary(self):
        total_books = len(self.books)
        total_borrowed = 0
        total_available = 0

        for borrowed in self.borrowed_books:
            total_borrowed += borrowed["Quantity"]

        for book in self.books:
            total_available += book["Copies"]

        print("========== Library Summary ==========")
        print("Total Registered Book Titles:", total_books)
        print("Total Borrowed Copies:", total_borrowed)
        print("Total Available Copies:", total_available)

        print("========== Available Books ==========")

        for book in self.books:
            print(book["Title"], ":", book["Copies"], "copies")

    def menu_system(self):
        while True:
            print("========== Campus Library System ==========")
            print("1. Register Book")
            print("2. Display All Books")
            print("3. Update Available Copies")
            print("4. Borrow Book")
            print("5. Search Book")
            print("6. Library Summary")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.book_registration()

            elif choice == "2":
                self.view_books()

            elif choice == "3":
                self.update_copies()

            elif choice == "4":
                self.borrow_book()

            elif choice == "5":
                self.search_book()

            elif choice == "6":
                self.display_summary()

            elif choice == "7":
                print("Thank you for using the Library System.")
                break

            else:
                print("Please enter a valid choice.")


library = LibraryManagement()
library.menu_system()
