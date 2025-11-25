from src.domain.complex import ComplexNumber
from src.services.functions import Functions


class Tests:
    def __init__(self):
        self.service = Functions()

    def test_add(self):
        number = ComplexNumber(9, 8)
        self.service.add(number.return_number())
        assert self.service.return_list() == [[9, 8]]

        number = ComplexNumber(1, 2)
        self.service.add(number.return_number())
        assert self.service.return_list() == [[9, 8], [1, 2]]

        number = ComplexNumber(3, 9)
        self.service.add(number.return_number())
        assert self.service.return_list() == [[9, 8], [1, 2], [3, 9]]

    def test_filter(self):
        number = ComplexNumber(9, 8)
        self.service.add(number.return_number())
        number = ComplexNumber(1, 2)
        self.service.add(number.return_number())
        number = ComplexNumber(3, 9)
        self.service.add(number.return_number())


        self.service.filter(2, 3)
        assert self.service.return_list() == [[1, 2], [3, 9]]

    def test_undo(self):
        number = ComplexNumber(9, 8)
        self.service.add(number.return_number())
        number = ComplexNumber(1, 2)
        self.service.add(number.return_number())
        number = ComplexNumber(3, 9)
        self.service.add(number.return_number())

        self.service.undo()
        assert self.service.return_list() == [[9, 8], [1, 2]]


if __name__ == "__main__":
    test = Tests()
    test.test_add()
    test.test_filter()

    #comment ^ before the undo
    # test.test_undo()