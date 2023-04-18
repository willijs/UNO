

class Card:
    
    def __init__(self, color, trait):
        
        info =  {"color": ["r", "g", "b", "y"],
                "trait": ["0","1","2","3","4","5","6","7","8","9", "skip", "reverse", "draw_2", "wild", "wild_draw_4"]
            }

        self.color = color
        self.trait = trait
        
    def get_string(self):
        
        return self.color + "-" + self.trait