from CardDeck import CardDeck as Deck
from Player import Player
from Card import Card
import re

class Game():


    def __init__(self, num_players):
        self.players = []
        self.cardDeck = Deck()
        self.discardPile = []
        self.current_player = 0
        self.card_drawn_flag = False
        self.rotation = False
        
        self.init_players_deal_cards(num_players)
        self.draw_first_discard_pile_card()
        
        

    def init_players_deal_cards(self, num_players):
        """
        Creates the specified number of players, and deals cards 7 cards to each of them.
        """

        for i in range(num_players):
            self.players.append(Player(i))
        
        for i in range(num_players):
            for j in range(7):
                self.players[i].add_card(self.cardDeck.draw_top_card(self.discardPile))

    def draw_first_discard_pile_card(self):
        """
        There is a rule which says that the first card cannot be a draw-4.
        Also, the effects of all other cards should apply.
        """
        drawn_card = self.cardDeck.draw_top_card(self.discardPile)


        while (True):
            if drawn_card.trait == "wild_draw_4":
                self.cardDeck.return_card(drawn_card)
                self.cardDeck.shuffle()
                drawn_card = self.cardDeck.draw_top_card(self.discardPile)
                continue
            self.discardPile.append(drawn_card)
            break

        self.process_played_card()

    
    def get_next_player(self):
        """
        This method is used to find the player who is next in line.
        """

        num_players = len(self.players)

        if self.rotation:
            self.current_player -= 1
            if self.current_player < 0:
                self.current_player = num_players - 1
        else:
            self.current_player += 1
            if self.current_player >= num_players:
                self.current_player = 0
        
        return self.players[self.current_player]

    def process_played_card(self):
        """
        Handles all of the stuff which happens when a special card is played.
        """
        pattern = re.compile(r'^[0-9]{1}$')
        top_card = self.discardPile[-1]
        text = top_card.trait

        if pattern.match(text):
            return

        elif (top_card.trait == "skip"):
            self.get_next_player()
        
        elif (top_card.trait == "reverse"):
            self.rotation = not self.rotation

        elif (top_card.trait == "draw_2"):
            self.get_next_player()
            for i in range(2):
                self.player_draw_card(self.current_player)


        elif (top_card.trait == "wild"):
            self.wild_card_played()
        
        elif (top_card.trait == "wild_draw_4"):
            self.wild_card_played()
            self.get_next_player()
            for i in range(4):
                self.player_draw_card(self.current_player)

    def is_valid_play(self, card):
        """
        Checks if a card can be played.
        """
        
        top_card = self.discardPile[-1]
        color = card.color
        trait = card.trait
        number = -1

        if (trait == "wild" or trait == "wild_draw_4"):
            return True
        
        elif (color == top_card.color):
            return True

        elif (trait == top_card.trait):
            return True
        
        return False

    def wild_card_played(self):
        """
        Makes the player able to choose which color they want to switch to.
        """

        top_card = self.discardPile[-1]

        print("You played a Wild card. Choose a color to continue:")
        print("1. Red\n2. Blue\n3. Green\n4. Yellow")
        
        choice = 0
        while (choice < 1 or choice > 4):
            choice = Game.int_input()

        color_map = {1: "r", 2: "b", 3: "g", 4: "y"}
        top_card.color = color_map[choice]


    def player_draw_card(self, player_id):
        """
        Makes the player draw the top card from the deck.
        """
        card = self.cardDeck.draw_top_card(self.discardPile)
        player = self.players[player_id]
        player.add_card(card)

    def get_valid_cards(self, player_id):
        """
        Gets a list of the cards the player can play.
        """
        player = self.players[player_id]
        valid_cards = []
        
        for card in player.get_hand():
            if self.is_valid_play(card):
                valid_cards.append(card)
        
        return valid_cards



    def play_turn(self, player_id):
        
        """
        Handle a single turn for a player.
        """

        player = self.players[player_id]

        if (self.card_drawn_flag):
            
            self.card_drawn_flag = False
            print(str(self.current_player) + "'s hand: " + ", ".join([str(card) for card in player.get_hand()]))
            
            if self.is_valid_play(player.get_hand()[-1]):
                
                print ("You have the following options: ", end=" ")
                print("0: pass", end="  ")
                print("1: " + str(player.get_hand()[-1]), end="    ")
                print("Pick your action: ")

                choice = -1
                while (choice < 0 or choice > 1):
                    choice = Game.int_input()
                
                if choice == 0:
                    return
                
                else:
                    player.play_card(len(player.get_hand()) - 1, self.discardPile)
                    self.process_played_card()
                    return

            else:
                print("No valid moves, enter 0 to continue.")
                choice = -1
                while (choice != 0):
                    choice = Game.int_input()
                return

        valid_cards = self.get_valid_cards(self.current_player)

        if (valid_cards):
            print(str(self.current_player) + "'s hand: " + ", ".join([str(card) for card in player.get_hand()]))
            print ("You have the following options:", end = " ")
            print("0: draw card", end="  ")
            
            for i in range (1, len(valid_cards) + 1):
                print(str(i) + ": " + valid_cards[i-1].get_string(), end="    ")
            
            print("Pick your action: ")
            choice = -1
            while (choice < 0 or choice > len(valid_cards)):
                choice = Game.int_input()
            
            if choice == 0:
                self.player_draw_card(self.current_player)
                self.card_drawn_flag = True
                self.play_turn(self.current_player)
            
            else:
                card = valid_cards[choice - 1]
                player.play_card(player.get_hand().index(card), self.discardPile)
                self.process_played_card()
                return
        
        
        else:
            print("No valid moves, you must draw a card. Enter 0 to continue.")
            choice = -1
            while (choice != 0):
                choice = Game.int_input()
            self.player_draw_card(self.current_player)
            self.card_drawn_flag = True
            self.play_turn(self.current_player)

        
        
    def is_winner(self):
        """
        Checks if the current player has won the game.
        """
        for i in range (len(self.players)):
            if len(self.players[i].get_hand()) == 0:
                return True
        
        return False



    

    
    def play_game(self):
        """
        This method is used to play a game of uno.
        """

        game_over = False
        
        while not game_over:
            
            print("Latest card: " + self.discardPile[-1].get_string())
            self.play_turn(self.current_player)
        
            if self.is_winner():
                print(f"Player {self.current_player} won the game!")
                game_over = True
            else:
                self.get_next_player()


    @staticmethod
    def int_input():
        """
        This method is used to validate inputs.
        """
        input_str = input("Enter a number: ")

        while True:
            if input_str.isdigit():
                choice = int(input_str)
                print("You entered:", choice)
                return choice

            else:
                print("Invalid input. Please enter a valid number.")
                input_str = input("Enter a number: ")
    
if __name__ == "__main__":
    num_players = 2
    game = Game(num_players)
    game.play_game()
