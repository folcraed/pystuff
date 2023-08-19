from pcinput import get_string
# def get_string(prompt):
#     line = input(prompt)
#     return line.strip()

name = ['Fred', 'Wilma', 'Barney', 'Betty', 'Dino', 'Bam-Bam']
# sorted_names = sorted(names)

# countdown = len(sorted_names) - 1

# while countdown >= 0:
#     print(sorted_names[countdown])
#    countdown -= 1

# for index, name in enumerate(sorted_names, start=1):
#     print(index, name)

# name_str = ', '.join(sorted_names)
# print(name_str)

while True:
    try:
        query = get_string(
            "Enter from 1 to 6 to get a Flinstone name (q to quit): ")
        if query == "q":
            break
        else:
            num = int(query) - 1
            print(name[num])
    except ValueError:
        print("Must enter 1 to 5 or \"q\" to exit.")

print("Thanks for playing!")
