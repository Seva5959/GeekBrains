class BookNotFoundError(Exception):
    def __init__(self):
        super().__init__('Books not founded !')

class Library:
    def __init__(self,storage_book):
        self.storage_book = storage_book

    def add_book(self, title):
        self.storage_book.append(title)

    def list_books(self):
        return self.storage_book

    def remove_book(self, title):
        if title not in self.storage_book:
            raise BookNotFoundError
        else:
            self.storage_book.remove(title)
