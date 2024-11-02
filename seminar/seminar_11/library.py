class Book:
    def __init__(self,title,author,pages,isbn):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn

    def __str__(self):
        return f'Произведение {self.title} в авторстве от {self.author}, ISBN: {self.isbn}'

    def __eq__(self, other):
        return self.isbn == other.isbn

    def __repr__(self):
        return f'title = "{self.title}", author = "{self.author}", isbn = {self.isbn}'


world_and_war = Book("Война и мир","Лев Толстой",700,57183)
hour_mool = Book("Час Быка","Иван Ефремов",500,65892)

class Library:
    def __init__(self):
        self.books = []
    def add_book(self,book):
        if book in self.books:
            return f'{book.title} уже есть в библеотеке'
        else:
            self.books.append(book)

    def delite_book(self,book):
        if not book in self.books:
            return f'{book.title} нельзя удалить, так как ее нет в библиотеке!'
        else:
            self.books.remove(book)

    def find_to_author(self,author):
        book_by_author = [book.author == author for book in self.books]
        for i_book in self.books:
            if i_book.author == author:
                break
        if i_book:
            return f'Книга в авторстве от {author} найдена. Вот подробная информация: {i_book}'
        else:
            return f'Книгa в авторстве от {author} не найденa'

    def __str__(self):
        return f'Библиотека имеет {len(self.books)} книг. Вот список книг {", ".join(book.title for book in self.books)}'    #{self.__name__}

    def __len__(self):
        return len(self.books)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.books[item]
        else:
            raise TypeError("Пошел нахуй")

    def __contains__(self, isbn):
        return any(book.isbn == isbn for book in self.books)

big_moscow_library = Library()
print(big_moscow_library.add_book(world_and_war))
print(big_moscow_library.add_book(hour_mool))
print(big_moscow_library)
print(big_moscow_library[1])
print(57183 in big_moscow_library)
print()
print(big_moscow_library.find_to_author("Иван Ефремов"))















