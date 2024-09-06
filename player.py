class Player:
    def __init__(self):
        self.pts = 0
        self.gems = 0
    
    def take_turn(self, grid, gems, players, my_index):
        # returns one of:
        # * "swap"
        # * "shuffle"
        # * ordered list of tuples representing list of indices corresponding to the chosen word
        # * None (timeout)
        # a returned word is guaranteed to be valid
        return None
