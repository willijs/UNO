

class Game():


    def __init__(self):
        self.players = []
        self.cardDeck = new carddeck


    def get_legal_actions(self, players, player_id):
        
        wild_flag = 0
        wild_draw_4_flag = 0
        legal_actions = []
        wild_4_actions = []
        hand = players[player_id].hand
        target = self.target
        
        if target.type == 'wild':
            for card in hand:
                if card.type == 'wild':
                    if card.trait == 'wild_draw_4':
                        if wild_draw_4_flag == 0:
                            wild_draw_4_flag = 1
                            wild_4_actions.extend(WILD_DRAW_4)
                    else:
                        if wild_flag == 0:
                            wild_flag = 1
                            legal_actions.extend(WILD)
                elif card.color == target.color:
                    legal_actions.append(card.str)

        # target is action card or number card
        else:
            for card in hand:
                if card.type == 'wild':
                    if card.trait == 'wild_draw_4':
                        if wild_draw_4_flag == 0:
                            wild_draw_4_flag = 1
                            wild_4_actions.extend(WILD_DRAW_4)
                    else:
                        if wild_flag == 0:
                            wild_flag = 1
                            legal_actions.extend(WILD)
                elif card.color == target.color or card.trait == target.trait:
                    legal_actions.append(card.str)
        if not legal_actions:
            legal_actions = wild_4_actions
        if not legal_actions:
            legal_actions = ['draw']
        return legal_actions