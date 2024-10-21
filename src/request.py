# request.py
# This file is used to request user input.

# Create function to request yes or no input from the user that accepts and returns a string
def request_yes_or_no_input(message: str) -> str:
    
    # Create placeholder variable to hold the value of the string input
    input_result: str = ""

    # Create infinite loop to keep asking the user for input until they enter either "yes" or "no"
    while True:

        # Set input_result to the string representation of the user's input and set it to lowercase
        input_result = str(input(message)).lower()

        # If the user's input is either "yes" or "no", break the infinite loop else print an error message and continue looping
        if (input_result == "yes") or (input_result == "no"):
            break
        else:
            print("\n----------> Error: Please enter either 'yes' or 'no' <----------")
    
    # Return the user's input either "yes" or "no"
    return input_result


# Create function to request a number input from the user that accepts two integers and a string and returns an integer
def request_number_input(start: int, end: int, message: str) -> int:
    
    # Creat placeholder variable to hold the value of the integer input
    input_result: int = 0

    # Create infinite loop to keep asking the user for input until they enter a number between the start and end values
    while True:

        # try to set input_result to the integer representation of the user's input and verify that it is between the start and end values
        try:
            input_result = int(input(message))

            # if input is between start and end values, break the infinite loop else raise a ValueError
            if (input_result >= start) and (input_result <= end):
                break
            else:
                raise ValueError

        # Catch any ValueError, either from the try block or raised manually and print an error message and continue looping
        except ValueError:
            print(
                f"\n----------> Error: Please enter a number from {start}-{end} <----------"
            )

    # Return the user's integer input
    return input_result
