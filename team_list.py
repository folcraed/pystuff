# This was something I copied from r/learnpython on reddit.
# It looked interesting, wanted to see if I could get it working.

from collections import defaultdict

# The point of it is to have a list of some kind that one needs to find
# the lowest value in. At the same time it needs to find unique values and
# check for duplicates. Works with lists or tuples.
data = (['team1', 'john', 80],
        ['team1', 'john', 90],
        ['team1', 'john', 60],
        ['team2', 'tim', 8],
        ['team2', 'tim', 10])


# Create a dictionary to hold our parsed values.
data_dict = defaultdict(list)


# Parse the original list into the new dictionary
for team, name, score in data:
    data_dict[(team, name)].append(score)

# Finally we output the values we wanted from the dictionary.
# Here the value we were looking for was the lowest scores.
print([(key[0], key[1], min(value)) for key, value in data_dict.items()])
