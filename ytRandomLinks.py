import random

# Character array
ascii_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z']

# Making a variable that we can use to enter in while loop
x = ''

while x == '':

    # Array of created links
    created_links = []
    
    # User input
    x = input('Hit enter to generate a random Youtube link: ')

    if x != '':
        break

    str = ''
    for i in range(11):
        t = random.randint(0,61)
        r = ascii_char[t]
        str = str + r
    link = 'https://youtu.be/' + str
    created_links.append(link)

    # Output
    print()
    print(link)
    print()
