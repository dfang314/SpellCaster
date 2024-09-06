import player
import letter
import random

class Game:
    def __init__(self, num_players, randomize=True):
        self.grid = []
        for i in range(5):
            self.grid.append([])
            for j in range(5):
                self.grid[i].append(letter.Letter())

        # TODO: figure out how gems are distributed
        
        self.players = []
        for i in range(num_players):
            self.players.append(player.Player())
          
        self.curr_turn = 0

    def swap(self, i, j, targ_letter, swapper_id):
        self.players[swapper_id].gems -= 3
        self.grid[i][j] = targ_letter
    
    def shuffle(self, swapper_id):
        self.players[swapper_id].gems -= 1
        all_letters = [letter for row in self.grid for letter in row]
        random.shuffle(all_letters)
        self.grid = [all_letters[:5], all_letters[5:10], all_letters[10:15], all_letters[15:20], all_letters[20:]]



       


