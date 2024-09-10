class Player:
    def __init__(self, id):
        self.pts = 0
        self.gems = 0
        self.id = id # id must match index in players list
    
    def take_turn(self, grid, players):
      # returns one of:
      # * "swap", [i, j, letter]
      # * "shuffle", None
      # * "move", ordered list of tuples representing list of indices corresponding to the chosen word
      # * "timeout", None (timeout)
      # a returned word is guaranteed to be valid
      return "timeout", None
