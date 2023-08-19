norm_string = input("Enter a string to hide: ")
secret_string = ""

for char in norm_string:
    if char == " ":
        secret_string += str(20)
    else:
        secret_string += str(ord(char) - 23)

print("Secret Message :", secret_string)

norm_string = ""
for i in range(0, len(secret_string) - 1, 2):
    char_code = secret_string[i] + secret_string[i+1]
    if char_code == "20":
        norm_string += " "
    else:
        norm_string += chr(int(char_code) + 23)

print("Original Message: ", norm_string)
