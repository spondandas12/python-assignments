class library:
    def __init__(self, book_name, author, available=True):
        self.book_name = book_name
        self.author = author
        self.available = available
    def check_out(self):
        if self.available:
            self.available = False
            print(f"'{self.book_name}' has been checked out.")
        else:
            print(f"sorry,'{self.book_name}' is currently not available.")
    def return_book(self):
        if self.available:
            self.available = True
            print(f"'{self.book_name}' has been returned. Thank You!")
        else:
            print(f"'{self.book_name}' was not checked out.")
    def display_info(self):
        status = "Available" if self.available else "Not available"
        print(f"Book:{self.book_name}, Author: {self.author}, Status: {status}")

book1 = library("the alchemist", "paulo ceolho")
book1.display_info()
print()
book1.check_out()
print()
book1.return_book()
print()