"""
CTEC 121
<Brandon Norton>
lab 5-2
practice 1
"""

""" IPO template
Input(s): None
Process: Prints the finger song
Output: outputs to terminal
"""
     
def firstVerse(name):
    print()
    print(name,"finger,", name,"finger, where are you?")
    print("Here I am, here I am. How do you do?")

def fingerSong():
    firstVerse("daddy")
    firstVerse("mommy")
    firstVerse("brother")
    firstVerse("sister")
    firstVerse("baby")


def main():

    fingerSong()
    print()

main()    