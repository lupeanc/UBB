class Client:
    def __init__(self, client_id, name):
        try:
            self.__id = int(client_id)
            self.__name = name
        except ValueError:
            raise ValueError("id has to be an integer")

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @id.setter
    def id(self, new_value: int):
        self.__id = new_value

    @name.setter
    def name(self, new_value):
        self.__name = new_value

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.id} : {self.name}"

    def to_dict(self):
        return self.__dict__

def test_client():
    new_client = Client(200, 'John MacTavish')
    assert new_client.id == 200
    assert new_client.name == 'John MacTavish'

test_client()