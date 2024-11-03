import random
import string


class Password:
    def __init__(
        self,
        length: int,
        exclude_special_chars: bool = False,
        exclude_uppercase_chars: bool = False,
        exclude_numbers: bool = False,
        allow_consecutive_chars: bool = False,
    ):
        if length < 8:
            raise ValueError("The length of the password must be at least 8 characters")

        self.__length = length
        self.__allow_consecutive = allow_consecutive_chars

        self.__character_options: dict[str, list[str]] = {
            "lowercase": list(string.ascii_lowercase),
            "uppercase": []
            if exclude_uppercase_chars
            else list(string.ascii_uppercase),
            "digits": [] if exclude_numbers else list(string.digits),
            "special": [] if exclude_special_chars else [".", ",", "-", "_", "@"],
        }

    def generate(self) -> str:
        chosen_chars: list[str] = (
            self.__character_options["lowercase"]
            + self.__character_options["uppercase"]
        )
        password: str = random.choice(chosen_chars)
        available_char_types: list[str] = [
            key
            for key in self.__character_options
            if (self.__character_options[key] != [])
        ]
        previously_chosen_char_type: str = "uppercase"

        while len(password) < self.__length:
            chosen_chars = []
            char_types: list[str] = available_char_types.copy()

            # Decrease likelihood of consecutive character types by making a 30% chance to remove them as an option
            if (len(char_types) > 1) and (random.random() <= 0.3):
                char_types.remove(previously_chosen_char_type)

            # Decrease likelihood of special characters by making a 60% chance to remove them as an option
            if ("special" in char_types) and (random.random() <= 0.6):
                char_types.remove("special")

            chosen_char_type: str = random.choice(char_types)
            previously_chosen_char_type = chosen_char_type

            chosen_chars.extend(self.__character_options[chosen_char_type])
            next_char: str = random.choice(chosen_chars)

            if (self.__allow_consecutive) or (next_char != password[-1]):
                password += next_char

        return password
