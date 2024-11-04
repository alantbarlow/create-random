from parser import Parser  # noqa: I001
from passcode import Passcode
from password import Password


def run_program():
    parser = Parser()
    args = parser.parse()

    if args.command == "password":
        
        special_chars: list[str] = args.custom_special_list
        if args.exclude_special:
            special_chars = []

        password = Password(
            args.length,
            exclude_uppercase_chars=args.uppercase,
            custom_special_chars=special_chars,
            exclude_numbers=args.numbers,
            allow_consecutive_chars=args.consecutive,
        )
        print(password.generate())

    elif args.command == "passcode":
        passcode = Passcode(args.length, allow_consecutive_integers=args.consecutive)
        print(passcode.generate())

    else:
        parser.print_help()

    # Print 2 new lines at the end of the output
    print("\n")

# If the file is being run directly, run the main function
if __name__ == "__main__":
    run_program()
