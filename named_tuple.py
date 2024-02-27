from collections import namedtuple

Color = namedtuple("Color", ["red", "green", "blue"])

blue = Color(0, 0, 255)
red = Color(255, 0, 0)
magenta = Color(170, 0, 255)
ltyellow = Color(255, 255, 127)


# Since Python doesn't have a switch/case function, we create one.
def switch():
    askfor = input("What color do you want? ")
    #   Make sure all is lowercase to match dictionary
    option = askfor.lower()

    def show_blue():
        result = blue
        values = ""
        for item in result:
            values = values + f"{item} "
        print("Blue is: ", values)

    def show_ltyellow():
        result = ltyellow
        values = ""
        for item in result:
            values = values + f"{item} "
        print("Light Yellow is: ", values)

    def show_red():
        result = red
        values = ""
        for item in result:
            values = values + f"{item} "
        print("Red is: ", values)

    def show_magenta():
        result = magenta
        values = ""
        for item in result:
            values = values + f"{item} "
        print("Red is: ", values)

    def default():
        print("Sorry, no such color.")

    dictionary = {
        "blue": show_blue,
        "lightyellow": show_ltyellow,
        "red": show_red,
        "magenta": show_magenta,
    }
    dictionary.get(option, default)()


switch()
