class Book:
    #intializes variables and makes sure that title, author, and genre are strings
    def __init__(self, title: str, author: str, genre: str = None):
        self.title = title
        self.author = author
        self.genre = genre
        self.checked_out = False  # Indicates status of book

    def display_info(self):
        #creates a variable genre_info and checks if genre has a value. if genre has a value it sets genre_info to the value of genre. if genre doesn't have a value it sets genre_info to Unknown
        genre_info = self.genre if self.genre else "Unknown"
        #prints Title, Author, and Genre on separate lines
        print(f"Title: {self.title}\nAuthor: {self.author}\nGenre: {genre_info}")

class Library:
    def __init__(self):
        #creates a list books that is empty
        self.books = []

    def add_book(self, book: Book):
        #adds book to the list books
        self.books = self.books + [book]
        print(f"'{book.title}' has been added to the library.")

    def remove_book(self, title):
        #for each book in the list books this checks if the title matches the input "title". If so then it removes the book from the list
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"'{title}' has been removed from the library.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def find_book(self, title):
        #for each book in the list books this checks if the title matches the input "title". If so then it prints the title
        for book in self.books:
            if book.title == title:
                print(f"Book found: '{title}'")
                return
        print(f"Book titled '{title}' not found in the library.")
    
    def list_books(self):
        #for each book in the list books this calls the display_info function from the Book Object which prints the Title, Author, and Genre
        for book in self.books:
            book.display_info()
            print()

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.read_book = 0 #indicates desire to check out / return book

    def borrow_book(self, book_title, library):
        for book in library.books:
            if book.title == book_title:
                print(f"Book found: '{book.title}'")

            if book.checked_out == False:
                self.read_book = int(input("Would you like to borrow the book selected? Enter 1 for yes and 2 for no"))

            if self.read_book == 1:
                print(f" '{book_title}' is available for checkout. Enjoy your reading!")
                self.checked_out == True
                return 

            if self.read_book == 2:
                print(f"No problem! There are a ton of great books out there. Happy Browsing!")
                return      

            else:
                print(f"'{book_title}' is already checked out.")
                return

            print(f"Book titled '{book_title}' not found in the library.")


    def return_book(self, book_title, library):
        for book in library.books:
            if book.title == book_title:
                print(f"Book found: '{book_title}'") 

            if self.checked_out == True:
                self.read_book = int(input("Would you like to return '{book_title}'? Enter 1 for yes and 2 for no"))

            if self.read_book == 1:
                print(f"Thank you for returning '{book_title}'. Have a great day!")
                self.checked_out == False
                return 

            if self.read_book == 2:
                print(f"No problem! Enjoy the book!")
                return         

            else:
                print(f"'{book_title}' is not checked out yet.")
                return

            print(f"Book titled '{book_title}' not found in the library.") 

           


#Professor Tolley's Code
def main():
    library = Library()
    book1 = Book("1984", "George Orwell", "Dystopian")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "Drama")

    library.add_book(book1)
    library.add_book(book2)

    print("\nFinding '1984':")
    library.find_book("1984")

    print("\nRemoving 'To Kill a Mockingbird':")
    library.remove_book("To Kill a Mockingbird")

    print("\nTrying to find removed book 'To Kill a Mockingbird':")
    library.find_book("To Kill a Mockingbird")

    print("\nListing all books:")
    library.list_books()

if __name__ == "__main__":
    main()

    

