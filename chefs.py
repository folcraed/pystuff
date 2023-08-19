# This is working with inheritance


class Chef:
    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The chef makes a salad")

    def make_special_dish(self):
        print("The chef makes BBQ ribs")


class ChineseChef(Chef):
    def make_fried_rice(self):
        print("The chef makes fried rice")

    def make_special_dish(self):
        print("The chef makes orange duck")


my_chef = Chef()
my_chef.make_special_dish()

my_chinese_chef = ChineseChef()
my_chinese_chef.make_special_dish()
