"""
Just a fun exercise that I thought I'd keep. A CLI twist on the old Magic
8-Ball game. It asks the user to enter a question, then randomly pulls from
a list of possible answers. The user can exit the program by just hitting
ENTER without asking a question.
"""

from random import randint

answers = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
    "You seriously want an answer?",
]

while True:
    print()
    question = input("Ask the Magic 8-Ball a question, <ENTER> to quit: ")
    if question == "":
        break
    theanswer = randint(1, 21)
    reply = answers[theanswer]
    print()
    print(reply)

print()
print("The Magic 8-Ball is done!")
