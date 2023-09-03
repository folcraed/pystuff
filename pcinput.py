def get_float(prompt):
    """Prompts for a floating number and ensures the input is a float"""
    while True:
        try:
            num = float(input(prompt))
        except ValueError:
            print("That is not a number -- please try again")
            continue
        return num


def get_integer(prompt):
    """Prompts for an integer and ensures the input is an integer"""
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            print("That is not an integer -- please try again")
            continue
        return num


def get_string(prompt):
    """Prompts for a string of any kind, be it characters or numerals"""
    line = input(prompt)
    return line.strip()


def get_letter(prompt):
    """Prompts for a single character ensuring only a single one is entered"""
    while True:
        line = input(prompt)
        line = line.strip()
        line = line.upper()
        if len(line) != 1:
            print("Please enter exactly one character")
            continue
        if line < 'A' or line > 'Z':
            print("Please enter a letter from the alphabet")
            continue
        return line
