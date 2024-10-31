import random
import string

class Password:

  def __init__(self, length:int, exclude_special_chars:bool = False, exclude_uppercase_chars:bool = False, exclude_numbers:bool = False):
    self.__length = length

    self.__character_options: dict[str, list[str]] = {
        "Lowercase Letters": list(string.ascii_lowercase),
        "Uppercase Letters": [] if exclude_uppercase_chars else list(string.ascii_uppercase),
        "Numbers": [] if exclude_numbers else list(string.digits),
        "Special Characters": [] if exclude_special_chars else [".", ",", "-", "_", "@"]
    }

  def generate(self) -> str:
    new_password = ""

    for _ in range(self.__length):
      characters: list[str] = []

      if (new_password == ""):
        characters.extend(self.__character_options["Uppercase Letters"])
        characters.extend(self.__character_options["Lowercase Letters"])

      while (characters == []):
        characters.extend(random.choice(list(self.__character_options.values())))

      new_password += random.choice(characters)

    return new_password
