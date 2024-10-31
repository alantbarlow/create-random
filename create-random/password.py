# password.py
# This file is used for the password class.

# import random which is used in the generate method to choose randome characters from the character list
import random

# Import string which is used by the password class to get lists of characters needed for password generation
import string

# Import the request module which is used to request user input
from request import request_yes_or_no_input, request_number_input

# Create the password class which stores the settings for the password generation and provides a method to generate a password
class Password:

  # Create the constructor method which initializes the class with default values
  def __init__(self):

    # Create a private class variable to store the length of the password by calling the request_number_input method and setting the password range to 4-50 characters.
    self.__length: int = request_number_input(
        4, 50, "\n\tEnter your desired password length: ")

    # Create a private class variable to store the different character types, initially set to empty lists. 
    self.__character_options: dict[str, list[str]] = {
        "Upper-case Letters": [],
        "Lower-case Letters": [],
        "Numbers": [],
        "Special Characters": []
    }

    # Print a message to the user to indicate that the character types will be requested
    print(
        "\n\n\tTo decide which character types you want to include in your password, please enter 'yes' or 'no' for each of the following options.\n"
    )

    # Create an infinite loop to keep looping until the user chooses at least one character type
    while True:
      # loop through each character type and ask the user if they want to include it in the password
      for key in self.__character_options:

        # Create a variable to store the user's 'yes' or 'no' input
        result: str = request_yes_or_no_input(f"\n\t\t{key}: ")

        # If the user wants to include the character type, add it to the list of character options
        if (result == "yes"):
          if (key == "Upper-case Letters"):
            self.__character_options["Upper-case Letters"] = list(
                string.ascii_uppercase)
          elif (key == "Lower-case Letters"):
            self.__character_options["Lower-case Letters"] = list(
                string.ascii_lowercase)
          elif (key == "Numbers"):
            self.__character_options["Numbers"] = list(string.digits)
          else:
            self.__character_options["Special Characters"] = [
                ".", ",", "-", "_", "@"
            ]

      # If the user has chosen at least one character type, break the infinite loop, else print an error message and continue looping
      if any(bool(value) for value in self.__character_options.values()):
        break
      else:
        print("\n\tError: You must include at least one character type in your new password.\n")

  # Create the generate method which returns a password based on the class's attributes
  def generate(self) -> str:

    # Create the placeholder for the new password
    new_password = ""

    # Create Loop that goes until the new password is the desired length
    for _ in range(self.__length):

      # Create placeholder variable to store the list of characters to choose from
      characters: list[str] = []

      # If this is the first iteration and therefore the new_password is empty, add all letter characters to the list of characters.
      # We do this because of our rule that the first character must always be a letter unless they dont want any letter characters.
      if (new_password == ""):
        characters.extend(self.__character_options["Upper-case Letters"])
        characters.extend(self.__character_options["Lower-case Letters"])

      # while the characters list is empty, pick a random character type and add it to the list of characters, repeating until a non-empty list is added
      while (characters == []):
        characters.extend(random.choice(list(self.__character_options.values())))

      # Add a random character from the list of characters to the end of the new password
      new_password += random.choice(characters)

    # Return the password when everything is finished
    return new_password
