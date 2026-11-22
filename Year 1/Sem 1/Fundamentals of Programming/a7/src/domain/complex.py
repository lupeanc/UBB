from dataclasses import dataclass

@dataclass
class ComplexNumber:
    """
      Domain of the problem: complex number
      This class contains methods regarding:
          1. Getting the real/complex part of a number
          2. The structure of how the numbers will be printed out

      """

    def __init__(self, real_part, complex_part):
        self._real_part = real_part
        self._complex_part = complex_part

    def return_number(self):
        return [self._real_part, self._complex_part]

    def real(self):
        return self._real_part

    def complex(self):
        return self._complex_part

    def __str__(self):
        return f"{self.real()} + {self.complex()} * i"

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
