import random


def generate_random_number(number_system):
    # Define the highest 6-digit number for each number system
    if number_system == "binary":
        max_number = int("111111", 2)
    elif number_system == "octal":
        max_number = int("77777", 8)
    elif number_system == "hexadecimal":
        max_number = int("FFFFFF", 16)
    else:
        raise ValueError("Invalid number system")

    # Generate a random number between 0 and the max number
    random_number = random.randint(0, max_number)

    # Convert the random number to the chosen number system if necessary
    if number_system == "binary":
        random_number = bin(random_number)[2:]
    elif number_system == "octal":
        random_number = oct(random_number)[2:]
    elif number_system == "hexadecimal":
        random_number = hex(random_number)[2:]

    # Add leading zeroes if necessary to make it a 6-digit number
    while len(random_number) < 6:
        random_number = "0" + random_number

    return random_number


def main():
    number_system = input("Enter the number system (binary, octal, or hexadecimal): ")
    while number_system.lower() in ["binary", "octal", "hexadecimal"]:
        try:
            # Generate a random 6-digit number in the chosen number system
            random_number = generate_random_number(number_system.lower())
            print(f"Your random 6-digit number in {number_system} is: {random_number}")
        except ValueError:
            print("Invalid number system")

        number_system = input("\nEnter the number system (binary, octal, or hexadecimal): ")

    print("Goodbye!")


if __name__ == "__main__":
    main()
