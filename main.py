def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = input("Enter the publication year: ")
    genre = input("Enter the genre: ")
    read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    book = [title, author, int(year), genre, read]
    library.append(book)
    print("Book added successfully!\n")

def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book[0].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!\n")
            return
    print("Book not found!\n")

def search_book(library):
    query = input("Enter title or author to search: ").lower()
    results = [book for book in library if query in book[0].lower() or query in book[1].lower()]
    
    if results:
        print("Matching Books:")
        for book in results:
            print(f"{book[0]} by {book[1]} ({book[2]}) - {book[3]} - {'Read' if book[4] else 'Unread'}")
    else:
        print("No matching books found!\n")

def display_books(library):
    if not library:
        print("Your library is empty!\n")
        return
    
    print("Your Library:")
    for idx, book in enumerate(library, 1):
        print(f"{idx}. {book[0]} by {book[1]} ({book[2]}) - {book[3]} - {'Read' if book[4] else 'Unread'}")
    print()

def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("No books in the library!\n")
        return
    
    read_books = sum(1 for book in library if book[4])
    percentage_read = (read_books / total_books) * 100
    
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%\n")

def main():
    library = []
    
    while True:
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        print()
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
