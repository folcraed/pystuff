# Example of getting an item from a list
from pcinput import get_string

name = ["Fred", "Wilma", "Barney", "Betty", "Dino", "Bam-Bam"]

while True:
    try:
        query = get_string("Enter from 1 to 6 to get a Flinstone name (q to quit): ")
        if query == "q":
            break
        else:
            num = int(query) - 1
            print(name[num])
    except ValueError:
        print('Must enter 1 to 5 or "q" to exit.')

print("Thanks for playing!")
