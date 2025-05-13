import letter
import random

class Game:
    def __init__(self, players, randomize=True): 
        self.grid = []
        for i in range(5):
            self.grid.append([])
            for j in range(5):
                self.grid[i].append(letter.Letter())
        
        self.letter_boost = (-1, -1) # dl in first 2 rounds, tl afterwards
        self.double = (-1, -1) # not set until round 2

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
      
    def play_turn(self):
        curr_player = self.players[self.curr_turn]
        move, details = curr_player.take_turn(self.grid, self.players, self.curr_round)
        while True:
            # print(f"Player {curr_player.id} made move {move}")
            if move == "timeout":
                break
            elif move == "swap":
                self.swap(details[0], details[1], details[2], self.curr_turn)
            elif move == "shuffle":
                self.shuffle(self.curr_turn)
            elif move == "word":
                gems_obtained = 0
                pts_obtained = 0
                double = False
                for i, j in details:
                    if (i, j) == self.double:
                        double = True
                    used_letter = self.grid[i][j]
                    if used_letter.gem:
                        gems_obtained += 1
                    if (i, j) == self.letter_boost:
                        if self.curr_round <= 2:
                            pts_obtained += 2 * used_letter.value
                        else:
                            pts_obtained += 3 * used_letter.value
                    else:
                        pts_obtained += used_letter.value
                    # TODO: new tl/dl tile
                    self.grid[i][j] = letter.Letter()
                curr_player.gems = min(10, curr_player.gems + gems_obtained)
                curr_player.pts += 2*pts_obtained if double else pts_obtained

                new_gem_spots = [(i // 5, i % 5) for i in range(25)]
                new_gem_spots = filter(lambda x: not self.grid[x[0]][x[1]].gem and x not in details, new_gem_spots)
                new_gem_spots = random.sample(list(new_gem_spots), gems_obtained)
                for spot in new_gem_spots:
                    self.grid[spot[0]][spot[1]].gem = True
                break
            else:
                print("ERROR: invalid move")

            move, details = curr_player.take_turn(self.grid, self.players, self.curr_round)
        self.curr_turn += 1
        if self.curr_turn == len(self.players):
            self.curr_turn = 0
            self.curr_round += 1
            # TODO: round end actions: modify dl, tl, double
            if self.curr_round == 6:
                # TODO: end the game
                print("game has ended")
                print("Player points:", [str(x.pts + x.gems) for x in self.players])
                print("Final board:", self.grid)
        
    def play_game(self):
        while self.curr_round < 6:
            self.play_turn()
