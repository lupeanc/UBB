from datetime import date

class Rental:
    def __init__(self, rental_id: int, book, start: date, end: date, client):
        self.__id = rental_id
        self.__client = client
        self.__book = book
        self.__start = start
        self.__end = end

    @property
    def id(self):
        return self.__id

    @property
    def client(self):
        return self.__client

    @property
    def book(self):
        return self.__book

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

    # len(rental)
    def __len__(self):
        if self.__end is not None:
            return (self.__end - self.__start).days + 1
        today = date.today()
        return (today - self.__start).days + 1

    def __repr__(self):
        return str(self)

    def __str__(self):
        # return
        from_date = self.__start.strftime("%Y-%m-%d")
        to_date = self.__end.strftime("%Y-%m-%d")
        return f"{self.id} - [book {self.book}] - [client {self.client}] - from {from_date} to {to_date}"

    def to_dict(self):
        self.__start = str(self.__start)
        self.__end = str(self.__end)
        return self.__dict__
