from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])

blue = Color(0, 0, 255)
red = Color(255, 0, 0)
magenta = Color(170, 0, 255)
ltyellow = Color(255, 255, 127)


# Since Python doesn't have a switch/case function, we create one.
def switch():
    askfor = input("What color do you want? ")
#   Make sure all is lowercase to match dictionary
    option = askfor.lower()

    def Blue():
        result = blue
        values = ''
        for item in result:
            values = values + f'{item} '
        print("Blue is: ", values)

    def ltYellow():
        result = ltyellow
        values = ''
        for item in result:
            values = values + f'{item} '
        print("Light Yellow is: ", values)

    def Red():
        result = red
        values = ''
        for item in result:
            values = values + f'{item} '
        print("Red is: ", values)

    def Magenta():
        result = magenta
        values = ''
        for item in result:
            values = values + f'{item} '
        print("Red is: ", values)

    def default():
        print("Sorry, no such color.")

    dict = {
        "blue": Blue,
        "lightyellow": ltYellow,
        "red": Red,
        "magenta": Magenta,
    }
    dict.get(option, default)()


switch()
