class libarary:
    def __init__ (self, book_title, author_name, copies_available):
        self.book_title = book_title
        self.author_name = author_name
        self.copies_available = copies_available
    def display_book(self):
        print("Book Title: ",self.book_title)
        print("Author Name: ",self.author_name)
        print("Number of copies available: ",self.copies_available)
    def borrow_book(self,ammount):
        if self.copies_available >= ammount:
            self.copies_available = self.copies_available-ammount
            print(self.copies_available)
            print("Book borrowed successfully")
        else:
            print("No copies available")
    def return_book(self, ammount):
        self.copies_available = self.copies_available + ammount
        print("Book returned successfully")
        print("Current available book: ",self.copies_available)
student1 = libarary("Lord of the Rings", "Abdullah", 10)
student1.display_book()
student2 = libarary("Harry Potter", "Emran", 15)
student2.display_book()
student3 = libarary("Rich dad Poor dad", "Khaled", 5)
student3.display_book()
student2.return_book(2)