class Book:
    def __init__(self, title="", author="", publication_year=0, genre="", read_status=False):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.read_status = read_status
        
    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year}) - Genre: {self.genre} - Read: {'Yes' if self.read_status else 'No'}"
           
        
    
    
library: list[Book] = []

def add_a_book():
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    publication_year = int(input("Enter Publication Year: "))
    genre = input("Enter Genre: ")
    read_status_str = input("Enter Read Status (yes/no): ")
    
    read_status: bool
    
    if read_status_str.lower() == "yes":
        read_status = True
    elif read_status_str.lower() == "no":
        read_status = False
    
    
    
    new_book = Book(title, author, publication_year, genre, read_status)

    library.append(new_book)
    print("Book added successfully.\n")
    print("Library: ", library)


def remove_a_book():
    book_title = input("Enter a Book Title Which You Want To Remove: ")
    
    for book in library:
        if book.title.lower() == book_title.lower():
            library.remove(book)
            print(f"'{book_title}' has been removed from the library.\n")
            return
    print(f"No book found with the title '{book_title}'.\n")

def search_for_book():
    book_title = input("Enter a Book Title: ")
    
    for book in library:
        if book.title.lower() == book_title.lower():
            print(
                f"""
                    Book Title: {book.title}
                    Author Name: {book.author}
                    Publication Year: {book.publication_year}
                    Genre: {book.genre}
                    Read Status: {book.read_status}
                """
            )
            return
    print("No Book Found for this Title!!!")

def display_all_book():
    for book in library: 
        print(
            f"""
                Book Title: {book.title}
                Author Name: {book.author}
                Publication Year: {book.publication_year}
                Genre: {book.genre}
                Read Status: {book.read_status}
            """
        )
    
def display_statistics():
    total_books = len(library)
    read_books = 0

    for book in library:
        if book.read_status:
            read_books += 1

    if total_books == 0:
        print("No Books have been added till now!")
        return

    percentage_of_read_books = (read_books * 100) / total_books

    print("Statistics of your library: ")
    print(f"Total Books: {total_books}")
    print(f"Books Read: {read_books}")
    print(f"Books Unread: {total_books - read_books}")
    print(f"Percentage of Read Books: {percentage_of_read_books:.2f}%\n")

def exit_program():
    print("Exiting Library Manager.")
    quit()

def choices():
    print(
        """
        Select the operation that you want to perform:
        1 - Add a Book
        2 - Remove a Book
        3 - Search for a Book
        4 - Display all Books
        5 - Display Statistics
        6 - Exit
        """
    )
    try:
        choice = int(input("What Operation do you want to do: "))

        if choice == 1:
            add_a_book()
        elif choice == 2:
            remove_a_book()
        elif choice == 3:
            search_for_book()
        elif choice == 4:
            display_all_book()
        elif choice == 5:
            display_statistics()
        elif choice == 6:
            exit_program()
        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")
    except ValueError:
        print("Please enter a valid number.\n")

while True:
    choices()
