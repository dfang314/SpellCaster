import player
import letter
import random

class Game:
    def __init__(self, players, randomize=True): 
        self.grid = []
        for i in range(5):
            self.grid.append([])
            for j in range(5):
                self.grid[i].append(letter.Letter())

        # TODO: figure out how gems are distributed
        
        self.players = players
        self.curr_turn = 0
        self.curr_round = 1

    def swap(self, i, j, targ_letter, swapper_id):
        self.players[swapper_id].gems -= 3
        self.grid[i][j] = targ_letter
    
    def shuffle(self, swapper_id):
        self.players[swapper_id].gems -= 1
        all_letters = [letter for row in self.grid for letter in row]
        random.shuffle(all_letters)
        self.grid = [all_letters[:5], all_letters[5:10], all_letters[10:15], all_letters[15:20], all_letters[20:]]
      
    def playTurn(self):
        move, details = self.players[self.curr_turn].take_turn(self.grid, self.players)
        while True:
            if move == "timeout":
                break
            elif move == "swap":
                self.swap(details[0], details[1], details[2], self.curr_turn)
            elif move == "shuffle":
                self.shuffle(self.curr_turn)
            elif move == "word":
                # TODO
                pass
            else:
                print("ERROR: invalid move")
            move, details = self.players[self.curr_turn].take_turn(self.grid, self.players)
        self.curr_turn += 1
        if self.curr_turn == len(self.players):
            self.curr_turn = 0
            self.curr_round += 1
            # TODO: round end actions: modify dl, tl, double
            if self.curr_round == 6:
                # TODO: end the game
                print("game has ended")
        
    def playGame(self):
        while self.curr_round < 6:
            self.playTurn()



       


