from time import sleep
from random import choice, random
from unicodedata import name

class Card:

    values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    def __init__(self):
        self.name = random.choice(Card.values)
        if(self.name == 'J' or self.name == 'Q' or self.name == 'K'):
            self.value = 10
        elif(self.name == 'A'):
            self.value = 11
        else:
            self.value = name
        self.show = False


