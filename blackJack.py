import time
from random import choice
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

menu_option = 0


def play(n):
    for i in range(n):
        print("Game {}".format(i+1))

#Function to say goodbye to our player
def goodbye():
    print("Thank you for playing {}!".format(player_name))
    print("This program was developed by AdrianMReds")
    print("Github User: @AdrianMReds")
    time.sleep(1.5)
    exit()

def instructions():
    print("We're still building this function come back later...")

def credits():
    print(
        """
        This game was made by AdrianMReds
        This program was made for practicing and there were no intentions of copying or stealing a real game
        This program was made with what I learned in Codecademy's CS101: Introduction to Programming
        If you enjoyed the game, you can go to my Github user to see the code :) 
        My Github username is @AdrianMReds
        Thanks for reading and for playing, have a nice week!
        """
    )

def menu():
    global menu_option
    global player_name
    print("Hello stranger, what's your name?")
    player_name = input()
    print("\nWell hello {}!".format(player_name))
    print("Welcome to the Terminal Blackjack game")
    while menu_option != 4:
        print("Type the number of what you want to do")
        print("1. Play\n2. Print Instructions\n3. Credits\n4. Exit game")
        menu_option = input()
        try:
            menu_option = int(menu_option)
        except ValueError:
            print("You have a type a number from 1 to 4, try again")
            continue
        
        if(menu_option == 1):
            
            n = input("How many times would you like to play against the computer?\n")
            while(type(n) != int):
                n = int(n)
            play(n)
        elif(menu_option == 2):
            instructions()
        elif(menu_option == 3):
            credits()
        elif(menu_option == 4):
            break


menu()
goodbye()

