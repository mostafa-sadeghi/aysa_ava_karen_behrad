import string
CHARACTERS = string.ascii_lowercase

my_password = input('enter a password: ')
for char in my_password:
    if char in CHARACTERS:
        x = CHARACTERS.index(char)
        x = x + 4
        if x > 26:
            x = x - 26

    char2 = CHARACTERS[x]
    print(char2, end='')


# my_password = input('enter a password: ')
# for char in my_password:
#     x = ord(char)
#     x = x + 1
#     char2 = chr(x)
#     print(char2, end='')


# for char in my_password:
#     x = ord(char)
#     x = x - 1
#     char2 = chr(x)
#     print(char2, end='')
