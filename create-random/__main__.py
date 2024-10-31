import argparse
from password import Password

def run_program():

  parser = argparse.ArgumentParser(description="A CLI tool used to create various outputs")
  subparsers = parser.add_subparsers(dest="command")

  # The subparser for the 'password' command
  password_parser = subparsers.add_parser("password", help = "Output a random password that includes uppercase, lowercase, and special characters and numbers.")
  password_parser.add_argument("length", type = int, help = "The desired length of the password")
  password_parser.add_argument("--no-numbers", "-n", action = "store_true", dest = "numbers", help = "Exclude numbers from the password")
  password_parser.add_argument("--no-special", "-s", action = "store_true", dest = "special", help = "Exclude special characters from the password")
  password_parser.add_argument("--no-uppercase", "-u", action = "store_true", dest = "uppercase", help = "Exclude uppercase characters from the password")

  args = parser.parse_args()

  if args.command == "password":
    password = Password(args.length, exclude_uppercase_chars = args.uppercase, exclude_special_chars = args.special, exclude_numbers = args.numbers)
    print(password.generate())
    
  else:
    parser.print_help()

# If the file is being run directly, run the main function
if (__name__ == "__main__"):
  run_program()
