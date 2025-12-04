import logging
from library_manager.inventory import LibraryInventory

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def print_menu():
    print("\n===== Library Inventory Menu =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")


def add_book_flow(lib_inv):
    book_title = input("Enter book title: ").strip()
    book_author = input("Enter author name: ").strip()
    book_isbn = input("Enter ISBN: ").strip()

    if not book_title or not book_author or not book_isbn:
        print("All fields are required.")
        return

    book_added = lib_inv.add_book(book_title, book_author, book_isbn)
    if book_added:
        print("Book added successfully.")
    else:
        print("Could not add book. Maybe ISBN already exists?")


def issue_book_flow(lib_inv):
    issue_isbn = input("Enter ISBN to issue: ").strip()
    if not issue_isbn:
        print("ISBN cannot be empty.")
        return
    lib_inv.issue_book(issue_isbn)


def return_book_flow(lib_inv):
    return_isbn = input("Enter ISBN to return: ").strip()
    if not return_isbn:
        print("ISBN cannot be empty.")
        return
    lib_inv.return_book(return_isbn)


def search_book_flow(lib_inv):
    print("1. Search by Title")
    print("2. Search by ISBN")
    search_choice = input("Enter your choice: ").strip()

    if search_choice == "1":
        title_part = input("Enter part of title: ").strip()
        matched_books = lib_inv.search_by_title(title_part)
        if not matched_books:
            print("No books found with that title.")
        else:
            print("Search results:")
            for single_book in matched_books:
                print(single_book)

    elif search_choice == "2":
        search_isbn = input("Enter ISBN: ").strip()
        found_book = lib_inv.search_by_isbn(search_isbn)
        if found_book is None:
            print("No book found with that ISBN.")
        else:
            print("Book found:")
            print(found_book)
    else:
        print("Invalid choice.")


def main():
    library_inventory = LibraryInventory()
    while True:
        print_menu()
        user_choice = input("Enter your choice: ").strip()
        if user_choice == "1":
            add_book_flow(library_inventory)
        elif user_choice == "2":
            issue_book_flow(library_inventory)
        elif user_choice == "3":
            return_book_flow(library_inventory)
        elif user_choice == "4":
            library_inventory.display_all()
        elif user_choice == "5":
            search_book_flow(library_inventory)
        elif user_choice == "6":
            print("Exiting program. Goodbye.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
