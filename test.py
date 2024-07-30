import sys, random
from pyfiglet import Figlet

figlet = Figlet()

prompt = input('Input: ')

# Zero if the user would like to output text in a random font.
if len(sys.argv) == 0:
    f = random.choice(figlet.getFonts())
    figlet.setFont(font = f)

# Lenght is 2. The first is -f or --font and the second is the name of a font
elif len(sys.argv) == 2 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    f = sys.argv[2]
    figlet.setFont(font = f)

else:
    sys.exit('Invalid')

if f in figlet.getFonts():
    s = input('Input: ')
    print('Output: ')
    print(figlet.renderText(s))

# You can then get a list of available fonts with code like this:
#figlet.getFonts()
# You can set the font with code like this, wherein f is the font’s name as a str:
#figlet.setFont(font=f)
# And you can output text in that font with code like this, wherein s is that text as a str:
#print(figlet.renderText(s))
