class Player:
    def __init__(self, id):
        self.pts = 0
        self.gems = 0
        self.id = id # id must match index in players list
    
    # self.id is the curr_player since take_turn is only called for the current player
    def take_turn(self, grid, players, curr_round):
      # returns one of:
      # * "swap", [i, j, character]
      # * "shuffle", None
      # * "word", ordered list of tuples representing list of indices corresponding to the chosen word
      # * "timeout", None (timeout)
      # a returned word is guaranteed to be valid
      return "timeout", None
