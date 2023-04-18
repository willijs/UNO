
class Player():


    def __init__(self, player_id):
        self.hand = []
        self.player_id = player_id
        self.stack = []

    def get_player_id(self):
        return self.player_id
    

    def draw_card(self, card):
        self.hand.append(card)
        
    def get_hand(self):
        return self.hand

    # def play_card(self, cardIndex):
    #     self.hand.pop(cardIndex)
    


    






