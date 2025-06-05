#!/usr/bin/env python3
# import the needed modules
import random 
# 1st set up the global Variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
# Class for the Card Object
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit + ' with a value of ' + str(self.value)
# Class for a Deck Obkect (Deck of Cards)
class Deck:
    
    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()       
# Class for a Player Object
class Player:
    
    def __init__(self,name):
        self.name = name
        # A new player has no cards
        self.all_cards = [] 
        
    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
# The actual Logic
# create the players
player_one = Player("Harry")
player_two = Player("Joe")
# create a new deck
deck = Deck()
# and shuffle it
deck.shuffle()
#verteilen 52 Karten durch 2 Spieler = 26
for c in range(26):
    player_one.add_cards(deck.deal_one())
    player_two.add_cards(deck.deal_one())
# Games is ready
game_runs = True
round = 0
while game_runs:
    round += 1
    print(f"Round {round}")
    if len(player_one.all_cards) == 0:
        print(f"{player_one.name} has run out of Cards")
        print(f"{player_two.name} Wins the Game")
        game_runs = False
        break
    if len(player_two.all_cards) == 0:
        print(f"{player_two.name} has run out of Cards")
        print(f"{player_one.name} Wins the Game")
        game_runs = False
        break

    if round > 500:
        print("this is going to long")
        game_runs = False
        break
    # Start a new round
    player_one_played_cards = []
    player_two_played_cards = []

    # each Player plays 1 card
    player_one_played_cards.append(player_one.remove_one())
    player_two_played_cards.append(player_two.remove_one())
    # check who wins the round of if we need to war

    in_war = True
    while in_war:
        if player_one_played_cards[-1].value > player_two_played_cards[-1].value:
            # player 1 has won
            print(f"{player_one.name} has won")
            player_one.add_cards(player_one_played_cards)
            player_one.add_cards(player_two_played_cards)
            # no war needed
            in_war = False
        elif player_one_played_cards[-1].value < player_two_played_cards[-1].value:
            # player 2 has won
            print(f"{player_two.name} has won")
            player_two.add_cards(player_one_played_cards)
            player_two.add_cards(player_two_played_cards)
            # no war needed
            in_war = False
        else:           
            print('WAR!')
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.
            
            # First check to see if player has enough cards
            
            # Check to see if a player is out of cards:
            if len(player_one.all_cards) < 5:
                print(f"{player_one.name} is unable to play war! Game Over at War")
                print(f"{player_two.name} Wins!!!")
                game_runs = False
                break

            elif len(player_two.all_cards) < 5:
                print(f"{player_two.name} is unable to play war! Game Over at War")
                print(f"{player_one.name} Wins!!!")
                game_runs = False
                break
            # Otherwise, we're still at war, so we'll add the next cards
            else:
                for num in range(5):
                    player_one_played_cards.append(player_one.remove_one())
                    player_two_played_cards.append(player_two.remove_one())
    print(player_one)
    print(player_two)
    print("="*10)
