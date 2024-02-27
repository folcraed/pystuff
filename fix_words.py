"""
An example of how to search through words in a sentence of paragraph and
fix errors in spelling found. Think of a very basic spelling or grammar
checker. The example text of course is known, so the error checking is
tailored to it. But it does provide ideas for methods of parsing text to
make corrections.
"""

text = """
as it turns out our chance meeting with REverend aRTHUR BElling was was
to change our whole way of life, and every sunday we'd hurry along to
St lOONY up the Cream BUn and Jam...
"""

wordlist = text.split()
lastword = ""
newtext = ""


for word in wordlist:
    # Correct any errant capitalization
    if len(word) > 2 and "A" <= word[0] <= "Z" and "A" <= word[1:] <= "Z":
        word = word[0] + word[1:].lower()

    # Capitalize any day of the week reference
    if word[3:] == "day":
        word = word[0].upper() + word[1:]

    # Correct any reverse capitalization
    if "a" <= word[0] <= "z":
        allcaps = True
        for c in word[1:]:
            if not ("A" <= c <= "Z"):
                allcaps = False
                break
        if allcaps:
            word = word[0].upper() + word[1:].lower()

    # Spring the trap set below for any duplicated words
    if word == lastword:
        continue

    newtext += word + " "
    # Set a trap for any duplicated words
    lastword = word


newtext = newtext.strip()
# Ensure first letter of sentence is capitalized
final = newtext[0].upper() + newtext[1:]
print(final)
