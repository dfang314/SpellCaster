import player
import letter

dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1] # includes 0, 0 since we are checking visited anyways
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

def find(grid, word, path):
    if len(word) == 0:
        return True, path
    if len(path) == 0:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j].char == word[0]:
                    found, indices = find(grid, word[1:], [(i, j)])
                    if found:
                        return found, indices
        return False, None
    else:
        lastx, lasty = path[-1]
        for i in range(9):
            newx, newy = lastx + dx[i], lasty + dy[i]
            if newx < 0 or newy < 0 or newx >= 5 or newy >= 5 or (newx, newy) in path:
                continue
            if grid[newx][newy].char != word[0]:
                continue
            path.append((newx, newy))
            found, indices = find(grid, word[1:], path)
            if found:
                return found, indices
            path = path[:-1]
        return False, None

class PointsPlayer(player.Player):
    def take_turn(self, grid, double, dl, tl, players, curr_round):
        path = []
        for word in letter.WORDS:
            found, indices = find(grid, word, path)
            if found:
                print("Found word", word)
                return "word", indices
        return super().take_turn(grid, players, curr_round)