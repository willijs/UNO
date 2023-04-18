from Card import Card as Card

import random as rnd

class CardDeck:
    
    def __init__(self):
        
        self.deck = []
        self.build()
        
    def build(self):
        #Builds a new deck
        card_info = Card.info
        for color in card_info["color"]:
            
            #All the cards apart from the wilds
            for num in card_info["trait"][:13]:
                self.deck.append(Card(color, num))
                if num != "0":
                    self.deck.append(Card(color, num))
                
            #The wild cards    
            for wild in card_info["trait"][-2:]:
                self.deck.append(Card(color,wild))
                
    def draw_top_card(self):
        
        #Draws the top card of the deck
        
        return self.deck.pop()
    
    def shuffle(self):
        #Shuffles the deck
        rnd.shuffle(self.deck)
        
    def print_deck(self):
        #Print the whole deck to the terminal
        
        for card in self.deck:
            
            print(card.get_string() + "\n")
    
    def get_deck_length(self):
        #Get the amount of cards left in the deck
        return len(self.deck)
            
        
