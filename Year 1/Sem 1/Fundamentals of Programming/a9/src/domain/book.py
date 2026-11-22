class Book:
    def __init__(self, book_id, title, author):
        try:
            self.__id = int(book_id)
            self.__title = title
            self.__author = author
        except ValueError:
            raise ValueError("id has to be an integer")

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @id.setter
    def id(self, new_value: int):
        self.__id = new_value

    @title.setter
    def title(self, new_value):
        self.__title = new_value

    @author.setter
    def author(self, new_value):
        self.__author = new_value

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'{self.id} : "{self.title}" by {self.author}'

    def to_dict(self):
        return self.__dict__

def test_book():
    new_book = Book(100, "Modern Warfare 2: Ghost", "David Lapham/Kevin West")
    assert new_book.id == 100
    assert new_book.title == "Modern Warfare 2: Ghost"

test_book()