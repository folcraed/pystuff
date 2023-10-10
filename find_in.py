"""
An example of how to find text contained in some type of delimiters, in this example "[]".
The code sets a type of null starting point, and searches for the first delimiter. If found,
it looks for the next delimiter, and stores what is contained between them, adding it to
a string for later printing. It then sets the starting point to the last found index and
continues on until all the text has been searched. It then prints out the string of found
characters.
"""

text = """
And sending tinted postcards of places they don't realize they haven't even visited to 'All
at nu[m]ber 22, weather w[on]derful, our room is marked with an 'X'. Wish you were here.
Food very greasy but we've found a charming li[t]tle local place hidden awa[y] in the back
streets where they serve Watney's Red Barrel and cheese and onion cris[p]s and the
accordionist pla[y]s "Maybe i[t]'s because I'm a Londoner"' and spending four days on the
tarmac at Luton airport on a five-day package tour wit[h] n[o]thing to eat but dried
Watney's sa[n]dwiches...
"""

start = -1  # Set start to not be "0" so it can be tested for
while True:
    start = text.find("[", start + 1)  # If "[" is found, set start to first letter
    if start < 0:  # If not found, keep looking
        break
    finish = text.find("]", start)  # If start found "[", grab what's between
    if finish < 0:  # If there's nothing there, keep looking
        break
    print(text[start + 1 : finish], end="")  # If letter(s) found, add them to string
    start = finish  # Reset the search to start from last thing found
print()
