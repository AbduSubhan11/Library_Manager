BOOKS_FILE = "library.txt"

def Add_Book():
    book_title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    
    try:
        publication_year = int(input("Enter the publication year: "))
    except ValueError:
        print("Invalid year! Please enter a number.")
        return
    
    genre = input("Enter the genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower()

    if read_status not in ["yes", "no"]:
        print("Invalid input for read status! Use 'yes' or 'no'.")
        return

    with open(BOOKS_FILE, "a") as file:
        file.write(f"{book_title} | {author} | {publication_year} | {genre} | {read_status}\n")

    print(f"Book '{book_title}' added successfully!")


def Remove_Book():
    search_term = input("Enter the title of the book to remove: ").strip().lower()
    try:
        with open(BOOKS_FILE, "r") as file:
            books = file.readlines()
        
        new_books = [book for book in books if search_term not in book.lower()]
        
        if len(new_books) == len(books):
            print("No book found with that title.")
        else:
            with open(BOOKS_FILE, "w") as file:
                file.writelines(new_books)
            print("Book removed successfully!")
    
    except FileNotFoundError:
        print("No books found!")


def Search_Book():
    print("Search by: ")
    print("1. Title")
    print("2. Author")
    
    choice = input("Enter your choice (1/2): ").strip()
    if choice not in ["1", "2"]:
        print("Invalid choice! Please enter 1 or 2.")
        return

    search_term = input("Enter the search keyword: ").strip().lower()
    
    try:
        with open(BOOKS_FILE, "r") as file:
            books = file.readlines()
            matching_books = [book for book in books if search_term in book.lower()]
            
            if matching_books:
                print("\nMatching Books:")
                for book in matching_books:
                    print(book.strip())
            else:
                print("No matching books found.")
    except FileNotFoundError:
        print("No books found!")


def Display_Book():
    print("\nYour Library:")
    try:
        with open(BOOKS_FILE, "r") as file:
            books = file.readlines()
            if not books:
                print("No books found!")
            else:
                for book in books:
                    print(book.strip())
    except FileNotFoundError:
        print("No books found!")


def Display_Statistics():
    try:
        with open(BOOKS_FILE, "r") as file:
            books = file.readlines()
        
        if not books:
            print("No books found!")
            return
        
        total_books = len(books)
        read_books = sum(1 for book in books if "yes" in book.lower().split("|")[-1].strip())

        percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
        print(f"Total Books: {total_books}")
        print(f"Percentage Read: {percentage_read:.2f}%")
    
    except FileNotFoundError:
        print("No books found!")


def Exit():
    print("Library saved to file. Goodbye.")


def main():
    while True:
        print("\nWelcome to your Personal Library Manager.")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            Add_Book()
        elif choice == 2:
            Remove_Book()
        elif choice == 3:
            Search_Book()
        elif choice == 4:
            Display_Book()
        elif choice == 5:
            Display_Statistics()
        elif choice == 6:
            Exit()
            break
        else:
            print("Please type a correct choice.")

main()
