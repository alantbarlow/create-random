import random


class Passcode:
    def __init__(self, length: int, allow_consecutive_integers: bool = False):
        if not (4 <= length <= 6):
            raise ValueError(
                "The length of the passcode must be between 4 and 6 characters inclusive"
            )

        self.__length = length
        self.__allow_consecutive = allow_consecutive_integers

    def generate(self) -> str:
        passcode = str(random.randint(0, 9))

        while len(passcode) < self.__length:
            next_digit = str(random.randint(0, 9))
            if (self.__allow_consecutive) or (next_digit != passcode[-1]):
                passcode += next_digit

        return passcode
