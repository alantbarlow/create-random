import argparse


class Parser:
    def __init__(self):
        self.__parser = argparse.ArgumentParser(description="A CLI tool used to create various outputs")
        subparsers = self.__parser.add_subparsers(dest="command")

        # The subparser for the 'password' command
        password_parser = subparsers.add_parser("password", help = "Output a random password that includes uppercase, lowercase, and special characters and numbers.")
        password_parser.add_argument("length", type = self.__password_length_validator, help = "The desired length of the password")
        password_parser.add_argument("--no-numbers", "-n", action = "store_true", dest = "numbers", help = "Exclude numbers from the password")
        password_parser.add_argument("--no-special", "-s", action = "store_true", dest = "special", help = "Exclude special characters from the password")
        password_parser.add_argument("--no-uppercase", "-u", action = "store_true", dest = "uppercase", help = "Exclude uppercase characters from the password")

        # The subparser for the 'passcode' command
        passcode_parser = subparsers.add_parser("passcode", help = "Output a random passcode with a given number of digets")
        passcode_parser.add_argument("length", type = int, choices = [4, 5, 6], help = "The desired passcode length (must be either 4, 5, or 6)")
        passcode_parser.add_argument("--allow-consecutive", "-c", action = "store_true", dest = "consecutive", help = "Allow consecutive individual integers (0-9) in the passcode")
    
    def __password_length_validator(self, value):
        i = int(value)
        if i < 8:
            raise argparse.ArgumentTypeError("Value must be greater than or equal to 8")
        return i
    
    def parse(self) -> argparse.Namespace:
        return self.__parser.parse_args()

    def print_help(self):
        self.__parser.print_help()
