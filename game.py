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

    def swap(self, i, j, targ_char, swapper_id):
        self.players[swapper_id].gems -= 3
        self.grid[i][j].char = targ_char
    
    def shuffle(self, swapper_id):
        self.players[swapper_id].gems -= 1
        all_letters = [letter for row in self.grid for letter in row]
        random.shuffle(all_letters)
        self.grid = [all_letters[:5], all_letters[5:10], all_letters[10:15], all_letters[15:20], all_letters[20:]]
      
    def playTurn(self):
        curr_player = self.players[self.curr_turn]
        move, details = curr_player.take_turn(self.grid, self.players)
        while True:
            if move == "timeout":
                break
            elif move == "swap":
                self.swap(details[0], details[1], details[2], self.curr_turn)
            elif move == "shuffle":
                self.shuffle(self.curr_turn)
            elif move == "word":
                gems_obtained = 0
                for i, j in details:
                    used_letter = self.grid[i][j]
                    if used_letter.gem:
                        gems_obtained += 1
                        curr_player.gems = min(10, curr_player.gems + 1)
                    curr_player.pts += used_letter.value
                    self.grid[i][j] = letter.Letter()
                new_gem_spots = [(i // 4, i % 4) for i in range(25)]
                new_gem_spots = filter(lambda x: not self.grid[x[0]][x[1]].gem and x not in details)
                new_gem_spots = random.sample(new_gem_spots, gems_obtained)
                for spot in new_gem_spots:
                    self.grid[spot[0]][spot[1]].gem = True
                break
            else:
                print("ERROR: invalid move")

            move, details = curr_player.take_turn(self.grid, self.players)
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



       


