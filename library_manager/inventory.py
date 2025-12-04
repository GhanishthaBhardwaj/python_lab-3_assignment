import json
import logging
from pathlib import Path

from .book import Book

CATALOG_FILE = Path("books_catalog.json")

logger = logging.getLogger(__name__)


class LibraryInventory:
    def __init__(self):
        self.book_list = []
        self.load_catalog()

    def add_book(self, title, author, isbn):
        for existing_book in self.book_list:
            if existing_book.isbn == isbn:
                logger.warning("Book with same ISBN already exists")
                return False
        new_book = Book(title, author, isbn)
        self.book_list.append(new_book)
        logger.info(f"Book added: {title}")
        self.save_catalog()
        return True

    def search_by_title(self, title):
        result = []
        for single_book in self.book_list:
            if title.lower() in single_book.title.lower():
                result.append(single_book)
        return result

    def search_by_isbn(self, isbn):
        for single_book in self.book_list:
            if single_book.isbn == isbn:
                return single_book
        return None

    def display_all(self):
        if not self.book_list:
            print("No books in library yet.")
        else:
            for one_book in self.book_list:
                print(one_book)

    def issue_book(self, isbn):
        book = self.search_by_isbn(isbn)
        if book is None:
            print("Book not found.")
            logger.error("Issue failed. Book not found.")
            return
        if book.issue():
            print("Book issued successfully.")
            logger.info(f"Book issued: {isbn}")
            self.save_catalog()
        else:
            print("Book is already issued.")
            logger.warning(f"Book already issued: {isbn}")

    def return_book(self, isbn):
        book = self.search_by_isbn(isbn)
        if book is None:
            print("Book not found.")
            logger.error("Return failed. Book not found.")
            return
        if book.return_book():
            print("Book returned successfully.")
            logger.info(f"Book returned: {isbn}")
            self.save_catalog()
        else:
            print("Book was not issued.")
            logger.warning(f"Book was not issued: {isbn}")

    def to_list_of_dicts(self):
        return [book_obj.to_dict() for book_obj in self.book_list]

    def save_catalog(self):
        try:
            data = self.to_list_of_dicts()
            with CATALOG_FILE.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            logger.info("Catalog saved to file")
        except Exception as e:
            logger.error(f"Error saving catalog: {e}")

    def load_catalog(self):
        if not CATALOG_FILE.exists():
            logger.info("Catalog file not found. Starting with empty list.")
            self.book_list = []
            return
        try:
            with CATALOG_FILE.open("r", encoding="utf-8") as f:
                data = json.load(f)
            self.book_list = []
            for item in data:
                book_obj = Book(
                    item.get("title", ""),
                    item.get("author", ""),
                    item.get("isbn", ""),
                    item.get("status", "available"),
                )
                self.book_list.append(book_obj)
            logger.info("Catalog loaded from file")
        except json.JSONDecodeError:
            logger.error("Catalog file is corrupted. Starting fresh.")
            self.book_list = []
        except Exception as e:
            logger.error(f"Error loading catalog: {e}")
            self.book_list = []
