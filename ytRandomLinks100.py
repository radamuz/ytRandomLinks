import random
import subprocess

# Character array
ascii_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z', '_','-']

# Making a variable that we can use to enter in while loop
x = 0

# User input
y = int(input('\nHow many links do you want to generate?: '))

while x < y:
    x += 1
    # Array of created links
    created_links = []
    
    # if x != '':
    #     break

    str = ''
    for i in range(11):
        t = random.randint(0,len(ascii_char)-1)
        r = ascii_char[t]
        str = str + r
    link = 'https://youtu.be/' + str
    created_links.append(link)

    # Output
    print()
    print(link)
    print()

    # We open the link with firefox
    print("Opening link with firefox...")
    print()
    subprocess.Popen(['firefox', link])
