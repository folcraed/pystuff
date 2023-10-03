"""
This is a file for things I'm learning, so it will change constantly.
If there's something that I would like to save for the future, I will
save it under a new file name.
"""

PIRATES = 6
coconuts = 0

while True:
    coconuts += 1
    pile = coconuts
    for i in range(PIRATES):
        if pile % PIRATES != 1:
            break
        pile = (PIRATES - 1) * int((pile - 1) / PIRATES)
    if pile % PIRATES == 1:
        break
print(coconuts)
