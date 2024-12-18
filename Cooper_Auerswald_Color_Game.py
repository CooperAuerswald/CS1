import random

def colored_text(text, color_name):
    color_codes = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'reset':'\033[30m',
        'cyan': '\033[36m',
        'white': '\033[37m'
    }

    print(f'{color_codes.get(color_name)}{text}{color_codes.get("reset")}')

name=input("What is your Name?")
print (f"Hello {name}, the objective of this game is to simply type the color of the text, rather than the text itself")
colors = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
rounds = 0
correct = 0

while True:
    text_color = random.choice(colors)
    print_color = random.choice(colors)
    colored_text(text_color,print_color)
    user=input ("Quick! Enter the color of the text!")
    if user==print_color:
        print ("YOU GOT IT!")
        correct += 1
    else:
        print ("Wrong")
    rounds += 1
    play_again=input (f"You have gotten {correct} of {rounds} correct! Would you like to play again? y/n")
    if play_again=="n":
        break
    else:
        print ("Invalid Response")