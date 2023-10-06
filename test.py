"""
This is a file for things I'm learning, so it will change constantly.
If there's something that I would like to save for the future, I will
save it under a new file name.
"""

from pcinput import get_string


def findCommon(word1, word2):
    """
    This takes two words the user enters and compares them to each other,
    looking for matching characters. The number of matches are returned."""
    common = ""
    for letter in word1:
        if (letter in word2) and (letter not in common):
            common += letter
    if common == "":
        return 0
    else:
        return len(common)


def main():
    word1 = get_string("Enter a word: ")
    word2 = get_string("Enter another word: ")
    print(f"The words have {findCommon(word1, word2)} letters in common.")


if __name__ == "__main__":
    main()
