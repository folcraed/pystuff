"""
This exercise takes a supplied string, and translates it using values stored
in a dictionary. It's very basic, first converting all the text to lower case
and stripping out any punctuation. The result is placed in a list, then is
matched against the dictionary, the result creating a new string with the
translation.
"""

from cleanup import clean

english_dutch = {
    "last": "laatst",
    "week": "week",
    "the": "de",
    "royal": "koninklijk",
    "festival": "feest",
    "hall": "hal",
    "saw": "zaag",
    "first": "eerst",
    "performance": "optreden",
    "of": "van",
    "a": "een",
    "new": "nieuw",
    "symphony": "symphonie",
    "by": "bij",
    "one": "een",
    "world": "wereld",
    "leading": "leidend",
    "modern": "modern",
    "composer": "componist",
    "composers": "componisten",
    "two": "twee",
    "shed": "schuur",
    "sheds": "schuren",
}

string = "Last week The Royal Festival Hall saw the first performance of a new symphony by one of the world's leading modern composers, Arthur 'Two Sheds' Jackson"

newstring = []

for word in clean(string).split():
    newstring.append(word)


dutch = ""
for word in newstring:
    if word in english_dutch.keys():
        dutch += english_dutch[word] + " "
    else:
        dutch += word + " "

print()
print(dutch)
