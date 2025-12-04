class Book:
    def __init__(self, book_title, book_author, book_isbn, status="available"):
        self.title = book_title
        self.author = book_author
        self.isbn = book_isbn
        self.status = status

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {self.status}"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            return True
        return False

    def is_available(self):
        return self.status == "available"
