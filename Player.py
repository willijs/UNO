
class Player():


    def __init__(self, player_id):
        self.hand = []
        self.player_id = player_id


    def draw_card(self):
        self.hand.append(cardDeck.drawCard())

    def play_card(self, cardIndex):
        self.hand.pop(cardIndex)
    
    

    






