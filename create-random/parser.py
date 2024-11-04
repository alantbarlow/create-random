import argparse
import json


class Parser:
    def __init__(self):
        self.__parser = argparse.ArgumentParser(description="A CLI tool used to create various outputs")
        subparsers = self.__parser.add_subparsers(dest="command")

        # The subparser for the 'password' command
        password_parser = subparsers.add_parser("password", help = "Output a random password that includes uppercase, lowercase, and special characters and numbers.")
        password_parser.add_argument("length", type = self.__password_length_validator, help = "The desired length of the password")
        password_parser.add_argument("--no-numbers", "-n", action = "store_true", dest = "numbers", help = "Exclude numbers from the password")
        password_parser.add_argument("--no-uppercase", "-u", action = "store_true", dest = "uppercase", help = "Exclude uppercase characters from the password")
        password_parser.add_argument("--allow-consecutive", "-c", action = "store_true", dest = "consecutive", help = "Allow consecutive individual characters in the password")
        
        special_char_group = password_parser.add_mutually_exclusive_group()
        special_char_group.add_argument("--no-special", "-s", action = "store_true", dest = "exclude_special", help = "Exclude special characters from the password")
        special_char_group.add_argument("--special-path", "-p", type = self.__json_path_to_list, dest = "custom_special_list", metavar = "JSON_FILE_PATH", help = "The path to a JSON file that contains a JSON array of special characters")

        # The subparser for the 'passcode' command
        passcode_parser = subparsers.add_parser("passcode", help = "Output a random passcode with a given number of digets")
        passcode_parser.add_argument("length", type = int, choices = [4, 5, 6], help = "The desired passcode length (must be either 4, 5, or 6)")
        passcode_parser.add_argument("--allow-consecutive", "-c", action = "store_true", dest = "consecutive", help = "Allow consecutive individual integers (0-9) in the passcode")
    
    def __password_length_validator(self, value):
        i = int(value)
        if i < 8:
            raise argparse.ArgumentTypeError("Value must be greater than or equal to 8")
        return i
    
    def __json_path_to_list(self, path):
        if not path.lower().endswith('.json'):
            raise argparse.ArgumentTypeError("The JSON_FILE_PATH must be a path to a file that has the extension of '.json'")
        
        try:
            with open(path, 'r') as file:
                data = json.load(file)

                # Raise error if the json data can not be parsed into a python list of strings
                if not isinstance(data, list) or not all(isinstance(item, str) for item in data):
                    raise argparse.ArgumentTypeError("The JSON file specified in the JSON_FILE_PATH must contain a single array of strings")
                return data
            
        except json.JSONDecodeError as decode_error:
            raise argparse.ArgumentTypeError("The JSON file specified in the JSON_FILE_PATH does not contain valid JSON data") from decode_error
        except FileNotFoundError as file_error:
            raise argparse.ArgumentTypeError("The JSON file specified in the JSON_FILE_PATH was not found at that location") from file_error

    
    def parse(self) -> argparse.Namespace:
        print()
        try:
            return self.__parser.parse_args()
        except SystemExit as exit:
            print("\n")  # Print a newline after the error message
            raise exit

    def print_help(self):
        self.__parser.print_help()
