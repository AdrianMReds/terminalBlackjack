import time
import random
from unicodedata import name

class Card:

    values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    def __init__(self, show=True):
        self.name = random.choice(Card.values)
        if(self.name == 'J' or self.name == 'Q' or self.name == 'K'):
            self.value = 10
        elif(self.name == 'A'):
            self.value = 11
        else:
            self.value = self.name
        self.show = show
    
    def __repr__(self):
        description = "This is a {name} card with a value of {value}".format(name = self.name, value = self.value)
        return description

menu_option = 0

def current_results(dealer, player):
    return "\n Dealer: {d}\n{name} {p}\n\n".format(d = dealer, name=player_name, p=player)

def play_submenu():
    option = 0
    while(option != 1 and option != 2):
        print("\nWhat will you do?")
        print("1. Hit\n2. Stand")
        option = input()
        try:
            option = int(option)
        except ValueError:
            print("You have to write number 1 or 2")
            continue
    return option

def there_is_name(cards, name):
    for c in cards:
        if(c.name == name):
            #There is an A in your cards
            return True
    #There is no A in your cards
    return False

def get_value(cards):
    total = 0
    if(there_is_name(cards, 'A') == False):
        for c in cards:
            total += c.value
    else:
        for c in cards:
            total += c.value
        if(total > 21):
            total -= 10
    return total

def play_dealer_cards(cards):
    dealer_value = get_value(cards)
    print("Dealer cards are: {} and {}".format(cards[0].name, cards[1].name))
    print("A value of {}".format(dealer_value))
    if(dealer_value >= 17):
        print("Dealer stands.")
        return cards
    else:
        print("Dealer hits.")
        cards.append(Card())
    

def play_your_cards(cards):
    not_finished = True
    while(get_value(cards) < 21):
        opt = play_submenu()
        if(opt == 1):
            cards.append(Card())
            print("Your new card is {}".format(cards[-1].name))
            print("Total value is {}".format(get_value(cards)))
            if(get_value(cards)>21):
                break
        else:
            print("Fine, you stand with {}".format(get_value(cards)))
            break
    return cards

def play(n):
    d_wins = 0
    your_wins = 0
    ties = 0
    for i in range(n):
        print("\nGame number {}".format(i+1))
        #Player cards are shown
        your_cards = [Card(), Card()]
        #One dealer card is shown and the other is not
        d_cards = [Card(), Card(False)]
        #Some special effects :p
        print("Dealer giving cards...\n")
        time.sleep(1.5)
        print("Dealer cards are: {} and [Secret card]\n\n".format(d_cards[0].name))
        print("Your cards are: {} and {}".format(your_cards[0].name, your_cards[1].name))
        #Checamos si ya acabó el juego
        if(get_value(d_cards) == 21 and get_value(your_cards) == 21):
            print("Dealer and {} have 21, push".format(player_name))
            ties += 1
            continue
        elif(get_value(d_cards) == 21):
            print("Dealer has 21, you lose")
            d_wins += 1
            continue
        elif(get_value(your_cards) == 21):
            print("You have 21, you win")
            your_wins += 1
            continue
        print("Hint: your current value is {}\n".format(get_value(your_cards)))
        #The list of cards updates if you hit, if not it returns the same list
        your_cards = play_your_cards(your_cards)
        
        #Checamos si el jugador ya perdió o ganó
        if(get_value(your_cards) > 21):
            print("You bust!")
            d_wins += 1
            continue

        #Dealer plays depending on the game it has
        d_cards = play_dealer_cards(d_cards)


#Function to say goodbye to our player
def goodbye():
    print("Thank you for playing {}!".format(player_name))
    print("This program was developed by AdrianMReds")
    print("Github User: @AdrianMReds")
    time.sleep(1)
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
    print("Welcome to the Terminal Blackjack game\n")
    while menu_option != 4:
        print("\nType the number of what you want to do")
        print("1. Play\n2. Print Instructions\n3. Credits\n4. Exit game")
        menu_option = input()
        try:
            menu_option = int(menu_option)
        except ValueError:
            print("You have a type a number from 1 to 4, try again")
            continue
        
        if(menu_option == 1):
            
            n = input("How many times would you like to play against the computer? (Maximum games: 10)\n")
            while(type(n) != int):
                n = int(n)
            if(n > 10):
                n = 10
            play(n)
        elif(menu_option == 2):
            instructions()
        elif(menu_option == 3):
            credits()
        elif(menu_option == 4):
            break


menu()
goodbye()

